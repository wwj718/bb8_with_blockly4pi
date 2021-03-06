# 说明
fork自[SpheroBB8-python](https://github.com/jjinking/SpheroBB8-python)

为其加上web api，使其可以被blockly以及微信控制

这部分的通信原理可以参考我之前的项目:[wechat_bot](https://github.com/wwj718/wechat_bot/blob/master/wechat_bot.py)、[raspberrypi_api](https://github.com/wwj718/raspberrypi_api)

blockly中直接generate为js代码，发送http请求操作BB8

![](https://raw.githubusercontent.com/wwj718/gif_bed/master/bb8.png)

注意:蓝牙连接的时候可能需要先使用命令行连接，然后断开，再启动脚本

# 按照依赖

```
sudo apt-get install python-pip libglib2.0-dev
#虚拟环境中
pip install bluepy bottle
```
# SpheroBB8-python

[Youtube Video](https://youtu.be/1Rkq6M9SdCc)

**Sphero's BB8 droid** 
*The droid you've been looking for.*

Now even better with a python API library!

Use "sudo hcitool lescan" to find BB8's MAC address 
input it at "`deviceAddress =`" (line 244) in the Sphero class in BB8_driver.py

**

***Included Scripts:***

**
**BB8Test.py**
A simple program that connects to BB8 and flashes the internal RGB LED red to green to blue. You can take it a step further and add `bb8.roll` commands to make him move using the API. 

**BB8joyDrive.py**
*requires PyGame library* 

Allow you to drive BB8 with a joystick/gamepad.
Shows on screen feedback of analog stick as well as speed and heading
Currently setup for a Xbox 360 controller.

 - Left analog stick controls BB8's movement, much the like app!   
 - Holding the Left trigger stops BB8.
 - Tapping the Left bumper changes BB8's heading - used to calibration.   
 -  Holding the Right bumper turns on BB8's blue 'tail light' to aid in calibration.

> Adapted the sphero driver library from:
> https://github.com/mmwise/sphero_ros/tree/groovy-devel/sphero_driver/src/sphero_driver
> 
> Used the bluetooth 'stuff' from:
> https://gist.github.com/ali1234/5e5758d9c591090291d6

**TODO:**
Tie in the btle handleNotifcations to Sphero response API
    

 - getting sensor info, command responses, etc. back from BB8

