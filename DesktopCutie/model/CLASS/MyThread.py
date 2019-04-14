# -*- coding: utf-8 -*-
'''
Created on 2019年1月26日

@author: RecluseXu
'''
from PyQt5.Qt import QThread

class MyThread(QThread):
    '''
    初始化的时候传入运行时  执行的函数 和 函数参数，然后运行就完事。
    最后能通过getResoult方法来获取运行结果
    '''
    def __init__(self,runFunction, parameter=None):
        super(MyThread,self).__init__()
        self.runFunction = runFunction
        self.parameter = parameter
        self.working = True
        self.result = None
    def __del__(self):
        self.working = False
    def run(self):
        if(self.parameter is not None):
            self.result = self.runFunction(self.parameter)
        else:
            self.result = self.runFunction()
    def getResoult(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None