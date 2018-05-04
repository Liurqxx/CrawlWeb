# _*_ coding:utf-8 _*_
# Author:liu

import re
import uuid
import subprocess

import requests

'''
安装ffmpeg：sudo apt install ffmpeg
'''

def download(url):
    video_ids = get_video_ids_from_url(url)
    m3u8_list = list(yield_video_m3u8_url_from_video_ids(video_ids))
    filename = '{}.mp4'.format(uuid.uuid4())
    for idx, m3u8_url in enumerate(m3u8_list):
        print('download {}'.format(m3u8_url))
        subprocess.call(['ffmpeg', '-i', m3u8_url, filename.format(str(idx))])




if __name__ == '__main__':


