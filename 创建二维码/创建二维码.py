# -*- coding: utf-8 -*-

import qrcode  # 导入模块
import io


def get_code_by_str(text):
    # 判断用户输入的类型
    if not isinstance(text, str):
        print('请输入字符串参数')
        return None
    # 设置图案样式
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 设置二维码数据
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img_data = io.BytesIO()
    img.save(img_data)
    return img_data


if __name__ == '__main__':
    info = input("请输入信息:")
    img_data = get_code_by_str(info)
    # 保存到本地图片中
    with open('info.png', 'wb') as file:
        file.write(img_data.getvalue())
    print("保存成功")
