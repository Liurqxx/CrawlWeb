# _*_ coding:utf-8 _*_
# Author:liu

import re
import uuid
import subprocess

import requests

'''
安装ffmpeg：sudo apt install ffmpeg
'''
# 下边 cookie 请打开知乎打开浏览器开发者工具随便找一个请求复制 cookie，千万不要泄露出去
HEADERS = {
    'cookie': '_zap=65393e71-bcc0-429d-871d-1c74805d989a; __DAYU_PP=77nUFjuZjfYu23Z7yebz56bcef1bdf50; capsion_ticket="2|1:0|10:1524892969|14:capsion_ticket|44:MGM1MzFlZGQ1OGUyNGM1ODliZTA4NWY0OWE0OGNjNmM=|5855da176ef070ff9ff4727cf55b695c317cd5a8447a2aaf59afe587364e3716"; z_c0="2|1:0|10:1524892981|4:z_c0|92:Mi4xRVh4VENBQUFBQUFBWUdCbG9jQ0NEU1lBQUFCZ0FsVk5OVlBSV3dBVm9JS3pTSjJoNlo0QzVXU2lGdXpYcURJTkRR|9e139201211ea12391a35ba534cf9c99b3d334046350d92bcec70f66f835799d"; q_c1=5feee446a2e3409d8d76aef10ee28400|1524892981000|1519728315000; __utma=51854390.1538887566.1524892996.1524892996.1524892996.1; __utmz=51854390.1524892996.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20180322=1^3=entry_date=20180322=1; d_c0="AJBuiu8oiQ2PTnqRAe5mi2_B81ZKAmwlnHw=|1525322944"; aliyungf_tc=AQAAAHqKx37gxAsAeUxI34QWsvp9kmMS; _xsrf=7cfed968-f422-4f92-b617-af3747821e30',
    # TODO
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

QUALITY = 'ld'  # 支持是 'ld' 'sd' 'hd' 分别是低清、中清、高清
def download(url):
    video_ids = get_video_ids_from_url(url)
    m3u8_list = list(yield_video_m3u8_url_from_video_ids(video_ids))
    filename = '{}.mp4'.format(uuid.uuid4())
    for idx, m3u8_url in enumerate(m3u8_list):
        print('download {}'.format(m3u8_url))
        subprocess.call(['ffmpeg', '-i', m3u8_url, filename.format(str(idx))])


def yield_video_m3u8_url_from_video_ids(video_ids):
    for video_id in video_ids:
        api_video_url = 'https://lens.zhihu.com/api/videos/{}'.format(int(video_id))
        r = requests.get(api_video_url, headers=HEADERS)
        playlist = r.json()['playlist']
        m3u8_url = playlist[QUALITY]['play_url']
        yield m3u8_url

def get_video_ids_from_url(url):
    """
    回答或者文章的 url
    """
    html = requests.get(url, headers=HEADERS).text
    # print(html)
    video_ids = re.findall(r'data-lens-id="(\d+)"', html)
    # print('11111', video_ids)
    if video_ids:
        return set([int(video_id) for video_id in video_ids])
    return []


if __name__ == '__main__':


