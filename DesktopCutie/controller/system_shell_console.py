# -*- coding: utf-8 -*-
'''
Created on 2019年2月12日

@author: RecluseXu
'''

from infoTool.cmd_helper import system_shell

def _change_char(the_input):
    return the_input.replace("/","\\")

def _cmd_command_transmit(command):
    '''传递命令'''
    return system_shell(command)
    
def _open_or_run_something(location):
    '''传入一个位置，打开对应的 文件/文件夹/程序'''
    print(location)
    if(location.find("::") == -1):
        a = _cmd_command_transmit("dir find " + _change_char(location))
        if(a.find("1 个文件") == -1):
            return a
    
    command = "start "+location
    return system_shell(command)

def _copy_file(source_file_location,aim_location):
    '''传入一个文件路径与目标路径，将文件复制到目标路径
        传入路径均是带文件名的。
    '''
    command = "copy " + source_file_location + " " + aim_location
    command = command.replace('/',"\\")
    print(command)
    print(system_shell(command))





def cmd_command_tansmit(parameter):
    command = parameter.get("command")
    return _cmd_command_transmit(command)

def open_or_run(parameter):
    software_location = parameter.get("softwareLocation")
    return _open_or_run_something(software_location)

def copy_file_to_resource(source_file_location):
    file_name = source_file_location.split("/")[-1]
    from infoTool.load_Project_Location import get_resourceLocation
    _copy_file(source_file_location, get_resourceLocation()+file_name)