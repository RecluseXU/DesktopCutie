# -*- coding: utf-8 -*-
'''
Created on 2019年2月12日

@author: RecluseXu
'''

import os
from subprocess import Popen, PIPE, STDOUT

def coding():
    '''系统默认编码'''
    import platform
    name = platform.uname()
    p = platform.architecture()
    print (name,p) #系统默认编码

def system_shell(command):
    
    # 函数参考:  https://blog.csdn.net/sinat_36219858/article/details/70186649
    b = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    
    b.wait()
    
    a = b.stdout.read()
#     print(a)
    # 读取得到的对象是bytes类型
    # 返回结果 windows: encoding='gbk'    linux/mac:默认uft-8
#     print(type(a),a)
    a = a.decode('gbk')
    a = a.replace("\r\n","\n")
#     print(a)
    return a

if __name__ == "__main__":
#     coding()
    print(system_shell("dir find E:/Software/WeChat/WeChat.exe"))