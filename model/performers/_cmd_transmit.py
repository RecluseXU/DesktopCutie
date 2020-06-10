# -*- coding: utf-8 -*-
'''
Created on 2019年2月28日

@author: RecluseXu
'''

def _performent_cmd_command_transmit(JudgeResoult):
    from controller.system_shell_console import cmd_command_tansmit
    JudgeResoult.set_perform_function(cmd_command_tansmit)
    JudgeResoult.add_perform_parameter("command", JudgeResoult.parameter)
    return JudgeResoult

def add_performer(JudgeResoult):
    '''传入一个JudgeResoult，此函数会为之添加 传递命令到cmd 的执行函数'''
    return _performent_cmd_command_transmit(JudgeResoult)