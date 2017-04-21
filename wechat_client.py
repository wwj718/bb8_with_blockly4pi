#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from itchat.content import *
import itchat

# 微信公众号放到本地 语音转文字
# ngrok

@itchat.msg_register(TEXT)
def get_friend(msg):
    if msg['ToUserName'] != 'filehelper': return

    content = msg.text
    print(content)
    if "前" in
    #friendStatus = get_friend_status(msg['RecommendInfo'])
    #itchat.send(friendStatus['NickName'], 'filehelper')

itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
