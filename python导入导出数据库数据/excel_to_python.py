# _*_ coding:utf-8 _*_
# Author:liu
import xlrd
import pymysql

try:
    # # 创建连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='python_data',
                           charset='utf8')
    # # 创建游标
    cur = conn.cursor()

    # 打开excel表格文件
    excel_data = xlrd.open_workbook('./data.xlsx')

    # 获取sheet页
    sheet1 = excel_data.sheet_by_index(0)

    # 获取sheet1页面中所有的数据
    for index_row in range(1, int(sheet1.nrows)):
        user_name = sheet1.cell_value(index_row, 1)
        user_pwd = sheet1.cell_value(index_row, 2)
        sql = 'insert into user(name,password) values(%s,%s)'
        # cur.execute('insert into user values(0,{},{})'.format(user_name, user_pwd))
        cur.execute(sql, [user_name, user_pwd])
    # 获取所有的行数
    # print(sheet1.nrows)
    # 获取对应的单元格值
    # print(sheet1.cell_value(1, 1))

    # 提交
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)

finally:
    # 关闭连接
    cur.close()
    conn.close()
