#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

import werobot
import re
from BB8_http_client import BB8HttpClient
#from werobot.replies import VoiceReply,SuccessReply

robot = werobot.WeRoBot(token='xyyldjs_test_token', #环境变量
                        #session_storage=session_storage,
                        enable_session=True)

bb8_client = BB8HttpClient(ip="192.168.0.120")

@robot.filter(re.compile(".*?[(帮助)|(help)].*?"))
def help():
    return "help OK"

@robot.voice
def reply_voice(message,session):
    recognition = message.recognition
    print(recognition)

    if '左转' in recognition:
        bb8_client.post("action=turn_left")
        return "ok"
    if '右转' in recognition:
        bb8_client.post("action=turn_right")
        return "ok"


    if '前' in recognition:
        print("go_forward")
        bb8_client.post("action=displace&arg1=100&arg2=0")
    if '后' in recognition:
        bb8_client.post("action=displace&arg1=100&arg2=180")
    if '右' in recognition:
        bb8_client.post("action=displace&arg1=100&arg2=90")
    if '左' in recognition:
        bb8_client.post("action=displace&arg1=100&arg2=270")
    if '红' in recognition:
        bb8_client.post("action=flash_color&arg1=1&arg2=ff0000")
    if '绿' in recognition:
        bb8_client.post("action=flash_color&arg1=1&arg2=33ff33")
    return "ok"
    #return "你说了 %s" %recognition

robot.run(port=8889, host="0.0.0.0")
