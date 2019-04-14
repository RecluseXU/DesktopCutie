# -*- coding: utf-8 -*-
'''
Created on 2019年3月26日

@author: RecluseXu
官方说明：https://tinypng.com/developers/reference/python
'''
import tinify
import json
from infoTool.load_Project_Location import get_resourceLocation

tinypng_api_key = None

def _load_tinyPNG_api_key():
    '''
    读取TinyPNG的API_key，API_key需要去官网获取（一个月免费用500次）
    '''
    global tinypng_api_key
    if(tinypng_api_key is not None):
        return tinypng_api_key
    
    apikey_file_location = get_resourceLocation()+"Manager/Tool/TinyPNG/TinyPNG_api_key.ini"
    with open(apikey_file_location ,"r")as f:
        api_key = f.read()
    tinypng_api_key = api_key
    return api_key
    
def compressing_image_from_file_to_file(source_picture_file_location, resoult_picture_file_location):
    '''
    压缩图片，传入源文件路径与压缩后文件存放的路径
    '''
    tinify.key = _load_tinyPNG_api_key()
    source = tinify.from_file(source_picture_file_location)
    source.to_file(resoult_picture_file_location)

def compressing_image_overwrite_source_file(source_picture_file_location):
    '''
    传入一个图片的地址，图片经过压缩后，覆盖原来的图片文件
    '''
    tinify.key = _load_tinyPNG_api_key()
    try:
        with open(source_picture_file_location, 'rb') as source:
            source_data = source.read()
            result_data = tinify.from_buffer(source_data).to_buffer()
        
        with open(source_picture_file_location,"wb") as source:
            source.write(result_data)
    except:
        try:
            compressing_image_overwrite_source_file(source_picture_file_location)
        except:
            return

def compressing_image_overwirte_source_file_list(source_picture_location_list):
    '''
    传入一个装了图片地址(str)的list，压缩图片，覆盖原文件
    '''
    n=0
    for picture_loaction in source_picture_location_list:
        n=n+1
        print(n,len(source_picture_location_list))
        compressing_image_overwrite_source_file(picture_loaction)

def add_compressed_id(the_id):
    '''
    添加id到已经被tinyPNG压缩的记录表中
    '''
    location = get_resourceLocation()+"Manager/Tool/TinyPNG/TinyNote.json"
    with open(location, "r")as f:
        have_compress_dict = json.load(f)
    have_compress_dict[the_id]=1
    with open(location, "w")as f:
        json.dump(have_compress_dict, f)

def is_id_had_compressed(the_id):
    '''
    检查传入的id是否已经被添加到压缩记录中
    '''
    location = get_resourceLocation()+"Manager/Tool/TinyPNG/TinyNote.json"
    with open(location, "r")as f:
        have_compress_dict = json.load(f)
    if(have_compress_dict.get(the_id)is None):
        return False
    else:
        return True

if __name__ == '__main__':
    a = "F:/MyDocument/Desktop/11.png"
    compressing_image_overwrite_source_file(a)