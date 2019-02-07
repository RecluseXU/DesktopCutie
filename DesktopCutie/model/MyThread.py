# -*- coding: utf-8 -*-
'''
Created on 2019年1月26日

@author: RecluseXu
'''
from PyQt5.Qt import QThread

class MyThread(QThread):
    def __init__(self,runFunction, parameter):
        super(MyThread,self).__init__()
        self.runFunction = runFunction
        self.parameter = parameter
        self.working = True
        self.result = None
    def __del__(self):
        self.working = False
    def run(self):
        self.result = self.runFunction(self.parameter)
    def getResoult(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None