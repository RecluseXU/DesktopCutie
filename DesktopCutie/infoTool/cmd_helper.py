# -*- coding: utf-8 -*-
'''
Created on 2019年2月12日

@author: RecluseXu
'''

import os
from subprocess import Popen, PIPE

def coding():
    '''系统默认编码'''
    import platform
    name = platform.uname()
    p = platform.architecture()
    print (name,p) #系统默认编码

def system_shell(command):
    b = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    b.wait()
    a = b.stdout.read()
    # 读取得到的对象是bytes类型
    # 返回结果 windows: encoding='gbk'    linux/mac:默认uft-8
#     print(type(a),a)
    a = a.decode('gbk')
    a = a.replace("\r\n","\n")
    return a
    print(r"%s" %(a))
if __name__ == "__main__":
    coding()
    print(system_shell("dir"))