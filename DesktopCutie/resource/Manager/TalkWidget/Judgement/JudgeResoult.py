# -*- coding: utf-8 -*-

'''
Created on 2019年2月21日

@author: RecluseXu
'''

class JudgeResoult(object):
    '''判断结果类'''
    input_str = None  # 输入的字符
    is_succeed = None  # 此次判断成功与否 
    operation_str = None # 判断出来的操作类型的名称
    parameter = None  # 判断出来的操作参数
    judge_type = None # 判断方式
    
    perform_function = None # 执行函数
    perform_parameter = None # 执行函数参数
    perform_resoult = None # 执行函数返回结果
    
    reply = None
    
    def __init__(self, input_str, is_succeed):
        '''
        传入输入的字符、判断是否成功(boolean)即可
        '''
        self.input_str = input_str
        self.is_succeed = is_succeed
    
    def set_perform_function(self,func):
        '''
        设置执行函数，应传入一个函数名，作为执行函数。
        若需要参数，那么请调用add_perform_parameter来添加参数，将来运行执行函数的时候，你可以从这里获取参数。
        '''
        self.perform_function = func
        
    def add_perform_parameter(self, key, value):
        '''
        添加执行参数，执行参数会被保存在一个dict中，参数会在 执行函数 运行的 时候传入 执行函数，所以执行函数如果需要什么参数，应该事先放入此处。
        '''
        if(self.perform_parameter is None):
            self.perform_parameter = {}
        self.perform_parameter[key] = value
    
    def get_resoult_info(self):
        '''
        获取结果信息，实际上是将类成员按照字符串的方式组合在一起，然后返回。
        '''
        info = "input:"+self.input_str + "\n判断是否成功:"+str(self.is_succeed)
        if(self.is_succeed):
            info = info + "\n判断方式:"+str(self.judge_type) + "\n判断操作类型:"+str(self.operation_str)
        if(self.perform_function is not None):
            info = info + "\n执行参数:"+str(self.perform_parameter)
        if(self.reply is not None):
            info = info + "\n回复:"+str(self.reply)
        info = info + "\n"
        return info
    
    def perform(self):
        '''运行执行函数'''
        if(self.perform_function is None):
            return
        self.perform_resoult = self.perform_function(self.perform_parameter)
    