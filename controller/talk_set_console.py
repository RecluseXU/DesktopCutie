# -*- coding: utf-8 -*-

'''
Created on 2019年3月6日

@author: RecluseXu
'''




def open_judgement_folder():
    '''
    打开判断模型文件夹
    '''
    from infoTool.load_Project_Location import get_resourceLocation
    from infoTool.cmd_helper import system_shell
    location = get_resourceLocation()+"Manager/TalkWidget/Judgement/JudgeModel"
    command = "start "+location
    system_shell(command)

def get_aim_introduce(aim):
    '''
    传入目标，获取对应的简介
    '''
    from infoTool.judge_introduce_helper import get_introduce
    return get_introduce(aim)

def get_icon(icon_name):
    '''
    传入图标名称，返回图标 QIcon
    '''
    from infoTool.load_icon import get_icon_by_key
    return get_icon_by_key(icon_name)

def judge_step_move_down(judge_step_name):
    '''
    将判断列表中的一个判断步骤往前移一个位置
    '''
    from model.judge.judge_console import move_down_a_judge_step
    move_down_a_judge_step(judge_step_name)

def judge_step_move_up(judge_step_name):
    '''
    将判断列表中的一个判断步骤往前移一个位置
    '''
    from model.judge.judge_console import move_up_a_judge_step
    move_up_a_judge_step(judge_step_name)
            

def open_software_mapper_file():
    '''
    用系统文本软件打开  软件mapper.json
    '''
    from infoTool.load_Project_Location import get_resourceLocation
    location = get_resourceLocation()+"/Manager/TalkWidget/SoftwareMapper.json"
    from controller.system_shell_console import open_or_run
    open_or_run({"softwareLocation":location})

def open_command_matching_mapper_file():
    '''
    用系统文本软件打开  命令匹配mapper.json
    '''
    from infoTool.load_Project_Location import get_resourceLocation
    location = get_resourceLocation()+"/Manager/TalkWidget/Judgement/CommandMatchingMapper.json"
    from controller.system_shell_console import open_or_run
    open_or_run({"softwareLocation":location})

def open_turing_ai_set_file():
    '''
    用系统文本软件打开  图灵AI设置文件.json
    '''
    from infoTool.load_Project_Location import get_resourceLocation
    location = get_resourceLocation()+"/Manager/TalkWidget/Judgement/TuringAI.json"
    from controller.system_shell_console import open_or_run
    open_or_run({"softwareLocation":location})

def enable_a_judge_step(judge_name):
    '''
    启用一个判断步骤
    '''
#     JudgeConsole.enable_judge_step(judge_name)
    from model.judge.judge_console import enable_judge_step
    enable_judge_step(judge_name)

def disable_a_judge_step(judge_name):
    '''
    禁用一个判断步骤
    '''
#     JudgeConsole.disable_judge_step(judge_name)
    from model.judge.judge_console import disable_judge_step
    disable_judge_step(judge_name)

def get_the_judge_step_list():
    '''
    获取判断步骤列表
    '''
    from model.judge.judge_console import get_judge_step_list
    return get_judge_step_list()

def disable_a_command_matching(matching_name):
    '''
    禁用一个命令匹配
    '''
    from model.judge.judge_console import get_a_judgement
    command_matching_judgement = get_a_judgement("CommandMatching")
    command_matching_judgement.disable_matching(matching_name)

def enable_a_command_matching(matching_name):
    '''
    启用一个命令匹配
    '''
    from model.judge.judge_console import get_a_judgement
    command_matching_judgement = get_a_judgement("CommandMatching")
    command_matching_judgement.enable_matching(matching_name)

def get_the_command_matching_mapper():
    '''
    获得命令匹配mapper
    '''
    from model.judge.judge_console import get_a_judgement
    command_matching_judgement = get_a_judgement("CommandMatching")
    return command_matching_judgement.get_matching_dict()

def get_the_software_mapper():
    '''
    得到软件mapper (dict)
    '''
    from infoTool.load_software_mapper import get_software_mapper_dict
    return get_software_mapper_dict()


def delete_a_selected_judgement(judge_name):
    '''
    删除一个插件
    '''
    from model.judge.judge_console import delete_a_judgement
    delete_a_judgement(judge_name)

def copy_file_to_judgement_folder(file_location, aim_location):
    '''
    将文件复制到模组文件夹
    '''
    from controller.system_shell_console import copy_file
    copy_file(file_location, aim_location)