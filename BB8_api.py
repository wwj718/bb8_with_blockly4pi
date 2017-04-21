#!/usr/bin/env python
# encoding: utf-8

# https://github.com/wwj718/wechat_bot/blob/master/wechat_bot.py
import BB8_simple
# 先连好蓝牙 可能需要命令行连接
# c.flash_red() # 闪烁红灯 次数
# c.flash_green() #可以加一个数字表示次数


'''
说明 任何设备不能连接bb8，包括树莓派本身，不需要手动连接，这个脚本会自行连接
首先要启动server
'''

from bottle import Bottle,run
from bottle import response,request
from json import dumps


c = BB8_simple.BB8Controller()
app = Bottle()

action_map = {}
#http://192.168.0.118:8000/bb8?action=flash_color #ok

# light
action_map["flash_color"] = c.flash_color #flash_color(self, color=(255, 255, 255), ntimes=3)
action_map["flash_blue"] = c.flash_blue #flash_blue(self, ntimes=3) #self.flash_color(color=(0, 0, 255), ntimes=ntimes)
action_map["flash_red"] = c.flash_red
action_map["flash_green"] = c.flash_green

# turn right/left
action_map["turn_right"] = c.turn_right #turn_right(self)
action_map["turn_left"] = c.turn_left

# Move and stop
#displace(self, speed, direction, duration)

action_map["stop"] = c.stop #stop(self)
action_map["displace"] = c.displace#go_forward(self, speed=SLOW, duration=1.5) #self.displace(speed, 0, duration)
action_map["go_forward"] = c.go_forward #go_forward(self, speed=SLOW, duration=1.5) #self.displace(speed, 0, duration)
action_map["go_back"] = c.go_back
action_map["go_right"] = c.go_right
action_map["go_left"] = c.go_left

action_map["disconnect"] = c.disconnect

# todo 微信 http 直接发送http请求
# blockly  websocket 另一个进程


def hex2rgb(hex):
    #h = hex.lstrip('#')
    rgb=tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
    print(rgb)
    return rgb

app = Bottle()
@app.route('/bb8')
def bb8():
    action = request.query.action #如果不存在为''
    action_arg1 = request.query.arg1#int
    action_arg2 = request.query.arg2
    if action:
        bb8_action = action_map.get(action)
        if bb8_action:
                #action_arg2 是#xxxxxx 十六进制的数
            if action_arg1:
                action_arg1 = int(action_arg1)
                if action_arg2:
                    if  action == "flash_color": #http://192.168.0.118:8000/bb8?action=flash_color&arg1=2&arg2=#ff0000
                        action_arg2 = hex2rgb(action_arg2)
                    if  action == "displace":
                        action_arg2 = int(action_arg2) #color  duration #todo  action需要拆开
                    bb8_action(action_arg1,action_arg2) #color  duration #todo  action需要拆开
                else:
                    bb8_action(action_arg1) #次数 speed MEDIUM(100) fast 160 slow 50 #http://192.168.0.118:8000/bb8?action=go_right&arg1=160 fast
            else:
                bb8_action()
    response.content_type = 'application/json'
    res = {"response":"ok"}
    return dumps(res)
try:
    run(app, host='0.0.0.0', port=8000)
except KeyboardInterrupt:
    c.disconnect()
