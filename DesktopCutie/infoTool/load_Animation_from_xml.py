# -*- coding: utf-8 -*-
'''
Created on 2019年1月8日

@author: RecluseXu
'''


import xml.etree.cElementTree as ET
from model.CLASS.AnimationLogic import AnimationLogic
from model.CLASS.AnimationConsole import AnimationConsole
from model.CLASS.AnimationResource import AnimationResource
from model.CLASS.AnimationMouse import AnimationMouse
from model.CLASS.Situation import Situation
from model.CLASS.AnimationSignal import AnimationSignal
from model.CLASS.AnimationRegister import AnimationRegister
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt
from PyQt5.Qt import QPoint
from infoTool.load_Fairy_From_XML_File import get_FairyInfo 
from infoTool.load_Project_Location import get_TheCuiteFolderLocation, get_resourceLocation
from infoTool.fairy_animation_general_info_helper import save_general_fairy_info_to_file

def transform_chinese_to_bool(chinese_str):
    # 将中文字的是否转换为bool变量返回
    if(chinese_str == "是"):
        return True
    elif(chinese_str == "否" or "不是"):
        return False
    print("转换bool变量失败，失败值:",chinese_str)

def transform_chinese_to_english(chinese_str):
    if(chinese_str == "开始"):
        return "start"
    elif(chinese_str == "结束"):
        return "end"

def transform_chinese_to_Qt_object(chinese_str):
    if(chinese_str == "左键"):
        return Qt.LeftButton
    elif(chinese_str == "右键"):
        return Qt.RightButton

def str_strip_split_map_list(things_str, map_function):
    '''
    传入一个字符串, 依次执行strip(), split(","), map(func), list()操作，返回结果
    '''
    return list(map(map_function, things_str.strip().split(",")))
    
def _imageScale(img,scaleProportion):
    # 按比例缩放图片
    newWidth = int(img.size().width()* scaleProportion)
    newHeight = int(img.size().height()* scaleProportion)
    # 变更图片大小，按比例缩放，平滑缩放
    return img.scaled(newWidth, newHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)

def _load_animation_register_info(root):
    '''
    读取动画注册信息
    
    返回:{Animation类实例}
    '''
    print("读取动画注册信息")
    animation_dict = {}
    for child in root.find("动作注册"):
        animation_register = AnimationRegister(child.attrib.get("id"), child.attrib.get("逻辑id"), child.attrib.get("资源id"))
#         print("id:",child.attrib.get("id"), "\t逻辑id:", child.attrib.get("逻辑id").split(","), "\t资源id:",child.attrib.get("资源id"))
        animation_dict[animation_register.animation_id] = animation_register
    print(list(animation_dict.keys()))
    return animation_dict

def _load_animation_logic_info(root, situation):
    '''
    读取动画逻辑信息
        situation：传入的状态类实例
    
    返回:{AnimationLogic类实例}
    '''
    print("读取动画逻辑信息")
    logicDict = {}
    for log_child in root.find("动作逻辑"):
        logic_id = log_child.attrib.get("id")
        a_logic = AnimationLogic(logic_id)
        
        for logic_info in log_child:
            if(logic_info.tag == "下一个动作"):
                next_animation_id_str = logic_info.get("动作id")
                now_Probability_str = logic_info.get("发生频率")
                a_logic.add_next_animation(next_animation_id=next_animation_id_str, probability_str=now_Probability_str)
            
            elif(logic_info.tag == "逻辑更替"):
                replace_condition = logic_info.get("发生条件")
                replace_condition = replace_condition.strip().split(",")# 清理空白字符，分割条件
                replace_condition = situation.transform_condition_str_list_to_judge_function_list(replace_condition) # 将条件list转化为对应的判断函数list
                
                replace_logic_id = logic_info.get("逻辑id")
                
                compel_replace = logic_info.get("强制更替")
                compel_replace = transform_chinese_to_bool(compel_replace) # 将中文转化为bool变量
                
                a_logic.add_logic_replace(replace_logic_id, replace_condition, compel_replace) # 增加逻辑更替
            
            elif(logic_info.tag == "动作更替"):
                replace_condition = logic_info.get("发生条件")
                replace_condition = replace_condition.strip().split(",")# 清理空白字符，分割条件
                replace_condition = situation.transform_condition_str_list_to_judge_function_list(replace_condition) # 将条件list转化为对应的判断函数list
                
                replace_animation_id = logic_info.get("动作id")
                
                compel_replace = logic_info.get("强制更替")
                compel_replace = transform_chinese_to_bool(compel_replace) # 将中文转化为bool变量
                
                a_logic.add_animation_replace(replace_animation_id, replace_condition, compel_replace) # 增加动画更替
                
            elif(logic_info.tag == "状态修改"):
                situation_name = logic_info.get("状态名")
                situation_value = logic_info.get("状态值")
                situation_change_moment = logic_info.get("修改时机")
                if(situation_change_moment is not None):
                    situation_change_moment = transform_chinese_to_english(situation_change_moment) # 转为英文，能节约内存
                change_condition = logic_info.get("发生条件")
                if(change_condition is not None):
                    change_condition = change_condition.strip().split(",")# 清理空白字符，分割条件
                    change_condition = situation.transform_condition_str_list_to_judge_function_list(replace_condition) # 将条件list转化为对应的判断函数list
                
                # 根据状态名与状态值获取 对应的状态设置函数
                set_function = situation.transform_set_str_to_set_function(situation_name, situation_value)
                
                a_logic.add_situation_change(set_function, situation_change_moment, change_condition)
                
        logicDict[a_logic.logicID] = a_logic
    print(list(logicDict.keys()))
    return logicDict

def _load_animation_resource(root, fairyID):
    '''
    读取鼠标动画信息
    fairyID：精灵id
    
    返回:{AnimationResource类实例}
    '''
    print("读取动画资源信息")
    animation_resource_dict = {}
    
    scale_point = root.find("动作资源").get("缩放比例")
    if(scale_point is None):
        scale_point = 1
    else:
        scale_point = float(scale_point)
    
    for resource_set in root.find("动作资源"):  
        # 资源id获取
        resource_set_id = resource_set.attrib.get("id")
        # 资源集路径获取
        resource_set_location = get_TheCuiteFolderLocation(fairyID) + resource_set.attrib.get("资源地址")
        
        resource_set_picture_excursion = resource_set.attrib.get("图像偏移") #资源集图像偏移
        if(resource_set_picture_excursion is not None):
            resource_set_picture_excursion = str_strip_split_map_list(resource_set_picture_excursion, int)
        else:
            resource_set_picture_excursion = [0,0]
        
        resource_set_picture_mirror_excursion = resource_set.attrib.get("镜像图像偏移") #资源集图像偏移
        if(resource_set_picture_mirror_excursion is not None):
            resource_set_picture_mirror_excursion = str_strip_split_map_list(resource_set_picture_mirror_excursion, int)
        else:
            resource_set_picture_mirror_excursion = [0,0]
        
                    
        a_resource_set = AnimationResource(resource_set_id, resource_set_location)
        for picture_node in resource_set:
            if(picture_node.tag == "资源"):
                picture_file_name = picture_node.get("图像")
                picture_location = resource_set_location+picture_file_name # 计算资源路径
                picture = QImage(picture_location)
                picture = _imageScale(picture, scale_point) # 按比例缩放图片
                
                window_excursion = picture_node.get("窗口偏移")
                if(window_excursion is not None):
                    window_excursion = str_strip_split_map_list(window_excursion, int)
                
                
                picture_excursion = picture_node.get("图像偏移")
                
                if(picture_excursion is not None):
                    picture_excursion = str_strip_split_map_list(picture_excursion, int)
                    # 将资源集的图像偏移与单个资源的图像偏移相加后保存
                    picture_excursion = [picture_excursion[i]+resource_set_picture_excursion[i] for i in range(0,2)]
                elif(resource_set_picture_excursion != [0,0]): # 在<资源集合>中填了图像偏移，而在<资源>中没填入时
                    picture_excursion = resource_set_picture_excursion
                
                
                mirror_picture_excursion = picture_node.get("镜像图像偏移")
                if(mirror_picture_excursion is not None):
                    mirror_picture_excursion = str_strip_split_map_list(mirror_picture_excursion, int)
                    # 将<资源集合>[镜像图像偏移]与单个<资源>[镜像图像偏移]相加后保存
                    mirror_picture_excursion = [mirror_picture_excursion[i]+resource_set_picture_mirror_excursion[i] for i in range(0,2)]
                elif(resource_set_picture_mirror_excursion !=[0,0]):
                    mirror_picture_excursion = resource_set_picture_mirror_excursion
                
                sleep_time_extended = picture_node.get("时延")
                if(sleep_time_extended is not None):
                    sleep_time_extended = float(sleep_time_extended)
                    
                frame_amount_extended = picture_node.get("帧延")
                if(frame_amount_extended is not None):
                    frame_amount_extended = int(frame_amount_extended)
            
                a_resource_set.add_resouce(picture, window_excursion, picture_excursion, mirror_picture_excursion, sleep_time_extended, frame_amount_extended, picture_location)
            
            animation_resource_dict[a_resource_set.resource_id] = a_resource_set
    
    print(list(animation_resource_dict.keys()))
    return animation_resource_dict
    
def _load_mouse_animation(root, situation):
    '''
    读取鼠标动画信息
    situation：传入的状态类实例
    
    返回:AnimationMouse类实例
    '''
    print("读取鼠标动画信息")
#     mouseAnimationDict={}
    
    mouseAnimationELE = root.find("鼠标动画")
    if(mouseAnimationELE is None):
        return
    
    mouse_animation = AnimationMouse()
    for ami in mouseAnimationELE:
        if(ami.tag == "点击"):
            for change_node in ami:
                click_key = change_node.get("键位")
                click_key = transform_chinese_to_Qt_object(click_key) #转中文为qt对象
                
                playing_animation = change_node.get("当前动画id")
                    
                happen_condition = change_node.get("条件")
                if(happen_condition is not None):
                    happen_condition = happen_condition.strip().split(",")# 清理空白字符，分割条件
                    happen_condition = situation.transform_condition_str_list_to_judge_function_list(happen_condition) # 将条件list转化为对应的判断函数list
                    
                aim_animation_id = change_node.get("动作id")
                hang_point = change_node.get("悬挂点")

                if(hang_point is not None and hang_point.find(",")!=-1):
                    hang_point = hang_point.strip().split(",")
                    x,y = map(int, hang_point)
                    hang_point = QPoint(x,y)
                    
                # 添加鼠标点击事件记录
                mouse_animation.add_mouse_click_animation_change(click_key, happen_condition, playing_animation, aim_animation_id, hang_point)
                
        if(ami.tag == "释放"):
            for change_node in ami:
                click_key = change_node.get("键位")
                click_key = transform_chinese_to_Qt_object(click_key) #转中文为qt对象
                playing_animation = change_node.get("当前动画id")
                    
                happen_condition = change_node.get("条件")
                happen_condition = happen_condition.strip().split(",")# 清理空白字符，分割条件
                happen_condition = situation.transform_condition_str_list_to_judge_function_list(happen_condition) # 将条件list转化为对应的判断函数list
                    
                aim_animation_id = change_node.get("动作id")
                hang_point = change_node.get("悬挂点")
                if(hang_point is not None and hang_point.find(",")!=-1):
                    hang_point = hang_point.strip().split(",")
                    x,y = map(int, hang_point)
                    hang_point = QPoint(x,y)
                    
                cancel_hang = change_node.get("取消悬挂")
                      
                # 添加鼠标释放记录
                mouse_animation.add_mouse_release_animation_change(click_key, happen_condition, playing_animation, aim_animation_id, hang_point, cancel_hang)
                
        if(ami.tag == "鼠标滚轮"):
            for change_node in ami:
                mouse_wheel_operation = change_node.get("滚轮")
                    
                happen_condition = change_node.get("条件")
                happen_condition = happen_condition.strip().split(",")# 清理空白字符，分割条件
                happen_condition = situation.transform_condition_str_list_to_judge_function_list(happen_condition) # 将条件list转化为对应的判断函数list
                    
                playing_animation_id = change_node.get("当前动画id")
                aim_animation_id = change_node.get("动作id")
                
                # 添加鼠标滚轮事件记录 
                mouse_animation.add_mouse_wheel_animation_change(mouse_wheel_operation, happen_condition, playing_animation_id, aim_animation_id)
    
    print(mouse_animation)
    return mouse_animation

def _load_init_animation(root):
    print("读取初始动画信息")
    init_AnimationID = root.find("初始动画").attrib.get("动作id")
    print(init_AnimationID)
    return init_AnimationID
    
def _load_signal_animation(root, situation):
    '''
    读取信号动画信息
    situation：传入的状态类实例
    
    返回:一个AnimationSignal类实例
    '''
    print("读取信号动画信息")
    signal_animation_ELE = root.find("信号动画")
    if(signal_animation_ELE is None):
        return 
    
    signal_animation = AnimationSignal()
    for signal_node in signal_animation_ELE:  
        
        signal_name = signal_node.get("信号名称")
        happen_condition = signal_node.get("条件")
        happen_condition = happen_condition.strip().split(",")# 清理空白字符，分割条件
        happen_condition = situation.transform_condition_str_list_to_judge_function_list(happen_condition) # 将条件list转化为对应的判断函数list
              
        aim_animation_id = signal_node.get("动作id")
        now_playing_animation = signal_node.get("当前动画id")
        
        # 添加记录
        signal_animation.add_signal_animation(signal_name, happen_condition, now_playing_animation, aim_animation_id)
    
    print(signal_animation)
    return signal_animation
    

def check_error(animation_dict, logic_dict, resource_dict, mouse_animation, signal_animation, init_AnimationID):
    '''
    检查文档是否有问题
    '''
    print("检查是否存在错误")
    
    # 检查<动作注册>里填写的东西对应的东西是否存在
    for register_note in animation_dict.values():
        # 检查逻辑是否存在
        if(logic_dict.get(register_note.logic_id) is None):
            print("error:<动作 id=\"" + register_note.animation_id + "\">[逻辑id]")
            print("<逻辑  id=\"" + register_note.logic_id + "\">不存在")
        # 检查资源是否存在
        if(resource_dict.get(register_note.resource_id) is None):
            print("error:<动作 id=\""+register_note.animation_id+"\">[资源id]")
            print("<资源集合 id=\"" + register_note.resource_id + "\">不存在")
    # 检查<动作逻辑>里填写的东西对应的东西是否存在
    for logic_note in logic_dict.values():
        # 检查<下一个动作>的目标是否存在
        if(logic_note.next_animation_list is not None):
            # 检查<下一个动作>[动画id]
            for next_animation_note in logic_note.next_animation_list:
                if(animation_dict.get(next_animation_note["动画id"]) is None):
                    print("error:<逻辑 id=\""+next_animation_note.logicID+"\"<下一个动作>[动作id]")
                    print("<动作 id=\""+next_animation_note["动画id"]+"\">不存在")
        # 检查<逻辑更替>的目标是否存在
        if(logic_note.logic_replace_list is not None):
            for logic_replace_note in logic_note.logic_replace_list:
                # 检查<逻辑更替>[逻辑id]
                if(logic_dict.get(logic_replace_note["逻辑id"]) is None):
                    print("error:<逻辑 id=\""+next_animation_note.logicID+"\"<下一个动作>[动作id]")
                    print("<逻辑 id=\""+next_animation_note["逻辑id"]+"\">不存在")
    # 检查<鼠标动画>里填写的东西对应的东西是否存在
    if(mouse_animation is not None):
        # <点击>
        if(mouse_animation.mouse_click_animation_list is not None):
            for click_note in mouse_animation.mouse_click_animation_list:
                # <点击>[当前动画id]
                if(animation_dict.get(click_note["当前动画id"]) is None):
                    print("error:<鼠标动画><点击><转换>[当前动画id]")
                    print("<动作 id=\""+click_note["当前动画id"]+"\">不存在")
                # <点击>[动作id]
                if(animation_dict.get(click_note["目标动画"]) is None):
                    print("error:<鼠标动画><点击><转换>[动作id]")
                    print("<动作 id=\""+click_note["目标动画"]+"\">不存在")
        # <释放>
        if(mouse_animation.mouse_release_animation_list is not None):
            for release_note in mouse_animation.mouse_release_animation_list:
                # <释放>[当前动画id]
                if(animation_dict.get(release_note["当前动画id"]) is None):
                    print("error:<鼠标动画><释放><转换>[当前动画id]")
                    print("<动作 id=\""+release_note["当前动画id"]+"\">不存在")
                # <释放>[动作id]
                if(animation_dict.get(release_note["目标动画"]) is None):
                    print("error:<鼠标动画><点击><转换>[动作id]")
                    print("<动作 id=\""+release_note["目标动画"]+"\">不存在")
        # <滚轮>
        if(mouse_animation.mouse_wheel_animation_list is not None):
            for wheel_note in mouse_animation.mouse_wheel_animation_list:
                # <滚轮>[当前动画id]
                if(animation_dict.get(wheel_note["当前动画id"]) is None):
                    print("error:<鼠标动画><滚轮><转换>[当前动画id]")
                    print("<动作 id=\""+wheel_note["当前动画id"]+"\">不存在")
                # <滚轮>[动作id]
                if(animation_dict.get(wheel_note["目标动画"]) is None):
                    print("error:<鼠标动画><滚轮><转换>[动作id]")
                    print("<动作 id=\""+wheel_note["目标动画"]+"\">不存在")
    
        
def load_animation_from_xml(fairyID):
    print("读取动作xml......")
    
    xml_add = get_FairyInfo(fairyID).resourceLocation
    print(xml_add)
#     print(xml_add)
    
    #载入xml文件进行分析
    tree = ET.parse(xml_add) 
    root = tree.getroot()   # 获取根节点
    
    # 状态对象，用于处理动画状态
    situation = Situation()
    
    
    
    animation_dict = _load_animation_register_info(root) # 载入动画注册信息
    logic_dict = _load_animation_logic_info(root, situation) # 载入动画逻辑信息
    resource_dict = _load_animation_resource(root, fairyID) # 载入动画资源信息
    mouse_animation = _load_mouse_animation(root, situation) # 载入鼠标动画信息
    signal_animation = _load_signal_animation(root, situation) # 载入信号动画信息
    init_AnimationID = _load_init_animation(root) # 载入初始动画信息
    
    # 检查错误
    check_error(animation_dict, logic_dict, resource_dict, mouse_animation, signal_animation, init_AnimationID)
    
    
    animation_console = AnimationConsole(animation_dict, logic_dict, resource_dict, mouse_animation, signal_animation, init_AnimationID, situation)
    
    #保存简要动画信息
    save_general_fairy_info_to_file(fairyID, animation_dict, logic_dict, resource_dict, mouse_animation, signal_animation, init_AnimationID)
    
    return animation_console

def getLoadAnimationQThread(fairyID):
    from model.CLASS.MyThread import MyThread
    return MyThread(load_animation_from_xml, fairyID)
    
if __name__ == '__main__':
#     print(animationXMLLocation)
    l = load_animation_from_xml("vat")
#     for i in l.resource_dict["闲置_站立"].picture_list: 
#         print(i)
    