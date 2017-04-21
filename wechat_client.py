#!/usr/bin/env python
# encoding: utf-8

import itchat

@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    if msg['ToUserName'] != 'filehelper': return
    print msg['Text']
    #friendStatus = get_friend_status(msg['RecommendInfo'])
    #itchat.send(friendStatus['NickName'], 'filehelper')

itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
