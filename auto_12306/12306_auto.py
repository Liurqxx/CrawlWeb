from favorite_name import statiom_names
from urllib import request
from json import loads
import ssl

# 取消/跳过证书验证
# ssl._create_default_https_context = ssl._create_unverified_context()

city = {}
for i in statiom_names.split('@'):
    if i:
        city[i.split('|')[1]] = i.split('|')[2]

from_name = input("请输入始发站(长沙):")
to_name = input("请输入终点站(成都):")
train_date = input("请输入乘车日期(格式:2018-02-02):")
from_station = city[from_name]
to_station = city[to_name]


def getList():
    '''请求访问12306，得到返回数据'''
    # 创建请求对象
    req = request.urlopen(
        "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (
            train_date, from_station, to_station))
    # 打开请求对象并获取源代码
    html = req.read()
    dict = loads(html.decode('utf8'))
    return dict['data']['result']


# 软卧:23  硬卧:26  硬座:28  无座：29   一等座:31  二等座:30
# 出发时间:8   到达时间:9

def getData():
    # a = 0
    printTitle()
    for _ in getList():
        car_list = i.split('|')
        # print('  ├─────┴─────────┴─────────┴─────┴─────┴──────┴─────┴───┴────┴───┴────┤')
        print('  │%5s│%7s│%8s│%5s|%5s|%5s|%4s|%4s|%4s|%3s|%4s|' % (
            car_list[3], from_name, to_name, car_list[8], car_list[9], car_list[31], car_list[30], car_list[23],
            car_list[26], car_list[28], car_list[29]))

        print('  ├─────┼─────────┼─────────┼─────┼─────┼──────┼─────┼───┼────┼───┼────┤')


seat_dict = {'一等座': 31, '二等座': 30, '软卧': 23, '硬卧': 26, '硬座': 28, '无座': 29}


def select_pick():
    """监听余票信息"""
    flg = True
    while flg:
        car_num = input("请输入车次:")
        car_seat = input("请输入座位:")
        print("正在监听中，一旦有票，电话通知你...")
        for i in getList():
            car_list = i.split('|')
            if car_list[3] == car_num:
                if not car_list[seat_dict[car_seat]] or car_list[seat_dict[car_seat]] == u'无':
                    continue
                else:
                    print('电话通知...')
                    flg = False
                    break


def printTitle():
    # print('车次\t\t出发站\t\t到达站\t\t出发时间\t\t到达时间\t\t一等座\t\t二等座\t\t软卧\t\t硬卧\t\t硬座\t\t无座')
    print('  ┌──┬────────┬────────┬───┬───┬───┬──┬─────┬─────┬────┬───┬────┬────┬─┐')
    print('  │ 车次 │始发站名称│终点站名称│出发时│到站时│一等座│二等座│软卧│硬卧│硬座│无座│')
    print('  ├─────┴─────────┴─────────┴─────┴─────┴──────┴─────┴───┴────┴───┴────┤')
    print('  ├─────┬─────────┬─────────┬─────┬─────┬──────┬─────┬───┬────┬───┬────┤')


def main():
    getData()
    select_pick()


if __name__ == "__main__":
    main()
