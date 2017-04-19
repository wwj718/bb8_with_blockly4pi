#!/usr/bin/env python
# encoding: utf-8

#能发送http get请求就行
import urllib

def bb8_http_client(action,ip="127.0.0.1",port=8000,arg1=0,arg2=0):
    '''
    BB8_http_client.bb8_http_client("flash_blue",arg1=2)
    '''
    return urllib.urlopen('http://{}:{}/bb8?action={}&arg1={}&arg2={}'.format(ip,port,action,arg1,arg2)).read()

