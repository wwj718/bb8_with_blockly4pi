#!/usr/bin/env python
# encoding: utf-8

#能发送http get请求就行
import urllib
class BB8HttpClient():
  def __init__(self,ip='192.168.12.1',port=8000):
      self.ip=ip
      self.port=port
  #def post(self,action,arg1=0,arg2=0):
  #def post(self,action,arg1=None,arg2=None):
  def post(self,args):
    '''
    BB8_http_client.bb8_http_client("flash_blue",arg1=2)

    if arg1 and arg2:
        return urllib.urlopen('http://{}:{}/bb8?action={}&arg1={}&arg2={}'.format(self.ip,self.port,action,arg1,arg2)).read()
    else:
        print 'http://{}:{}/bb8?action={}'.format(self.ip,self.port,action)
        return urllib.urlopen('http://{}:{}/bb8?action={}'.format(self.ip,self.port,action)).read()
    '''
    return urllib.urlopen('http://{}:{}/bb8?{}'.format(self.ip,self.port,args)).read()


def main():
    # test
    c= BB8HttpClient()
    #c.post(action="go_forward")
    #c.post(action="go_back")

if __name__ == '__main__':
    main()
