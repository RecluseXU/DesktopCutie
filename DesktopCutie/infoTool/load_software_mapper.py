# -*- coding: utf-8 -*-
'''
Created on 2019年3月4日

@author: RecluseXu
'''
from infoTool.load_Project_Location import get_SoftwareMapper_location
import json

software_mapper_dict = None

def _load_software_mapper():
    ''''''
    global software_mapper_dict
    mapper_location = get_SoftwareMapper_location()
    with open(mapper_location, "r")as f:
        software_mapper_dict = json.load(f)

def reload_software_mapper():
    _load_software_mapper()

def set_software_mapper_dict(new_mapper):
    global software_mapper_dict
    software_mapper_dict = new_mapper

def get_software_mapper_dict():
    '''获取软件mapper'''
    global software_mapper_dict
    if(software_mapper_dict is None):
        _load_software_mapper()
    return software_mapper_dict

def save_software_mapper():
    '''保存软件mapper到文件中'''
    global software_mapper_dict
    mapper_location = get_SoftwareMapper_location()
    with open(mapper_location, "w")as f:
        json.dump(software_mapper_dict, f, ensure_ascii=False,indent=4)

if __name__ == '__main__':
    mapper = get_software_mapper_dict()
    save_software_mapper()