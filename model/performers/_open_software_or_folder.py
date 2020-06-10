# -*- coding: utf-8 -*-
'''
Created on 2019年2月28日

@author: RecluseXu
'''

from infoTool.string_similarity_calculation import calculate_ratio_proportion

def _parameter_nalysis_count_now_ratio_point(input_str ,softwareName):
    '''大小写各与软件名匹配一次，将更相似的匹配值返回'''   
    
    nowRatioPoint1 = calculate_ratio_proportion(input_str, softwareName)
    nowRatioPoint2 = calculate_ratio_proportion(input_str, softwareName.lower())
    if(nowRatioPoint1 > nowRatioPoint2):
        return nowRatioPoint1
    else:
        return nowRatioPoint2

def _find_the_most_similar_software_name_from_the_mapper(AIM_SOFTWARE_NAME, software_mapper):
    # 遍历软件名称列表，运用字符串相似度算法，与输入软件名进行比较。计算最相似的软件名字符串
    # 进行软件名相似度计算
    mostSimilar = ""
    maxRatioPoint = 99
        
    for software_name in list(software_mapper.keys()):
        
        nowRatioPoint = _parameter_nalysis_count_now_ratio_point(AIM_SOFTWARE_NAME, software_name)
        #print(software[0],nowRatioPoint)
        if(len(mostSimilar)==0 and maxRatioPoint==99):#如果是第一个
            mostSimilar = software_name
            maxRatioPoint = nowRatioPoint
        elif(nowRatioPoint > maxRatioPoint):#如果不是第一个，就判断哪个相似度大
            mostSimilar = software_name
            maxRatioPoint = nowRatioPoint
    return [mostSimilar,maxRatioPoint]

def _performent_open_software(JudgeResoult):
    '''打开软件函数导入结果之中'''
    
    # 获取软件mapper
    from infoTool.load_software_mapper import get_software_mapper_dict
    software_mapper = get_software_mapper_dict()
        
    AIM_SOFTWARE_NAME = JudgeResoult.parameter
    
    # 尝试直接获取，看看有没有与输入软件名完全一致的对应项
    software_location = software_mapper.get(AIM_SOFTWARE_NAME)
    if(software_location is not None):
        JudgeResoult.add_perform_parameter("ConsiderPoint", 1)
        JudgeResoult.add_perform_parameter("SoftwareName", AIM_SOFTWARE_NAME)
    
    # 没有完全一致的，那么就进行相似度匹配
    if(software_location is None):
        most_similar_name, ratioPoint = _find_the_most_similar_software_name_from_the_mapper(AIM_SOFTWARE_NAME, software_mapper)
        JudgeResoult.add_perform_parameter("ConsiderPoint", ratioPoint)
        software_location = software_mapper[most_similar_name]
        JudgeResoult.add_perform_parameter("SoftwareName", most_similar_name)
    
    JudgeResoult.add_perform_parameter("softwareLocation", software_location)
#         print(software_location,ratioPoint)
    
    # 为这个结果添加执行函数
    from controller.system_shell_console import open_or_run
    JudgeResoult.set_perform_function(open_or_run)
    
    return JudgeResoult

def add_performer(JudgeResoult):
    '''传入一个JudgeResoult，此函数会为之添加 打开软件或目录 的执行函数'''
    return _performent_open_software(JudgeResoult)