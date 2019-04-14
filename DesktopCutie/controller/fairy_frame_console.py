# -*- coding: utf-8 -*-
'''
Created on 2019年4月1日

@author: RecluseXu
'''
from model.CLASS.Situation import check_all_condiction_in_list
from infoTool.load_Fairy_From_XML_File import get_FairyInfo 
from infoTool.load_Animation_from_xml import load_animation_from_xml as load_animation

def load_animation_from_xml(fairy_id):
    return load_animation(fairy_id)

def get_fairy_info(fairyID):
    return get_FairyInfo(fairyID)

def check_condition_list(condition_list):
    return check_all_condiction_in_list(condition_list)