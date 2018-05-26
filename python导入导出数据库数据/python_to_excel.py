# _*_ coding:utf-8 _*_
# Author:liu
import xlwt
import pymysql

'''
把数据库中的数据导出到excel文件
'''


def connection(sql):
    '''数据中获取数据'''
    # 创建连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='python_data',
                           charset='utf8')
    # 创建游标
    cur = conn.cursor()

    # 执行sql语句
    cur.execute(sql)

    # 提交
    conn.commit()

    # 关闭连接
    cur.close()
    conn.close()
    # 元祖形式返回
    return cur


def create_excel(all_user, attributes):
    '''创建excel文件'''
    # 获取excel文件
    workbook = xlwt.Workbook()

    # 添加sheet页 参数:sheet名称,单元格覆盖
    sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    # sheet页第一行保存数据库字段
    for index, attribute in enumerate(attributes):
        sheet.write(0, index, attribute[0])

    num = 1
    # 写入数据
    for user_row in all_user:
        for index_col, user_col in enumerate(user_row):
            sheet.write(num, index_col, user_col)
        num += 1

    # 保存excel文件
    workbook.save('./data.xlsx')


def main():
    # 获取数据库数据
    result = connection('select * from user')
    # result.fetchall():获取所有的数据
    # result.description:获取所有的字段属性
    # (('id', 3, None, 10, 10, 0, False), ('name', 253, None, 32, 32, 0, True), ('password', 253, None, 64, 64, 0, True))
    # 获取数据库所有的字段
    attribute_list = result.description
    user_info = result.fetchall()
    # ((1, '张三', '123456'), (2, '李四', '0000000'))

    # 把字段列表传入create_excel内
    create_excel(user_info, attribute_list)
    # 写入成功
    print('写入成功')


if __name__ == '__main__':
    main()
