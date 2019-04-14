# -*- coding: utf-8 -*-
'''
Created on 2019年2月22日

@author: RecluseXu
'''
from model.performers._open_software_or_folder import add_performer as openthings_add_performer
from model.performers._cmd_transmit import add_performer as cmdtransmit_add_performer

def add_performent(JudgeResoult):
    if(JudgeResoult.is_succeed == False):
        return JudgeResoult
    if(JudgeResoult.operation_str == "OpenSoftwareOrFolder"):
        return openthings_add_performer(JudgeResoult)
    elif(JudgeResoult.operation_str == "cmdCommandTransmit"):
        return cmdtransmit_add_performer(JudgeResoult)
    return JudgeResoult
    

if __name__=="__main__":
    from model.judge.judge_console import judge_process
    judge_resoult = judge_process("./我的文档")
    a = add_performent(judge_resoult)
    a.perform()
    print(a.perform_parameter)
    
    judge_resoult2 = judge_process("cmd dir")
    b = add_performent(judge_resoult2)
    b.perform()
    print(b.perform_parameter,b.perform_resoult)
    