# encoding:utf-8
"""
人脸库结构
|- 人脸库(appid)
   |- 用户组一（group_id）
      |- 用户01（uid）
         |- 人脸（faceid）
      |- 用户02（uid）
         |- 人脸（faceid）
         |- 人脸（faceid）
         ....
       ....
   |- 用户组二（group_id）
   |- 用户组三（group_id）
   ....
"""

import requests
import os
import time


def send_request(img_base64, group_id, user_id):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    json_data = {
        "image": img_base64,
        "image_type": "BASE64",
        "group_id": group_id,
        "user_id": user_id,
        "quality_control": "NONE"
    }
    params = json_data
    access_token = '24.0b02f32908f5be9c46348bd3223b3f1d.2592000.1653398339.282335-26063997'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())


if __name__ == '__main__':
    yt_base64_path = '../cover_img/yt_base64/'
    tt_base64_path = '../cover_img/tt_base64'

    yt_base64_list = os.listdir(yt_base64_path)
    yt_base64_list.remove('no face')
    tt_base64_list = os.listdir(tt_base64_path)
    tt_base64_list.remove('no face')

    for yt_base64_file in yt_base64_list:
        f=open(yt_base64_path+yt_base64_file,"r",encoding='UTF-8')
