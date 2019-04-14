# -*- coding: utf-8 -*-
'''
Created on 2019年1月9日

@author: RecluseXu
'''
from model.CLASS.AnimationPlayer import AnimationPlayer
from model.CLASS.Situation import check_all_condiction_in_list

class AnimationConsole(object):
    #动画控制
    
    def __init__(self,animation_dict, logic_dict, resource_dict, mouse_animation, signal_animation, init_AnimationID, situation):
        self.animation_dict = animation_dict # 动画注册集
        self.logic_dict = logic_dict # 动画逻辑集
        self.resource_dict = resource_dict # 动画资源集
        self.mouse_animation = mouse_animation # 鼠标动画
        self.signal_Animation = signal_animation # 信号改变动画
        self.situation = situation # 状态信息
        self.init_animation_id = init_AnimationID # 初始动画的动画id
        
        
        now_Animation = self.animation_dict[init_AnimationID]
        now_logice = self.logic_dict[now_Animation.logic_id]
        now_resource = self.resource_dict[now_Animation.resource_id]
        
        self.animation_player = AnimationPlayer(now_Animation, now_logice, now_resource, self.get_register_by_id, self.get_logic_by_id, self.get_resource_by_id)
        
    def get_register_by_id(self, animation_id):
        '''
        通过传入动画id，获取动画注册信息
        '''
        return self.animation_dict[animation_id]
    
    def get_logic_by_id(self, logic_id):
        '''
        通过传入逻辑id,获取动画逻辑信息
        '''
        return self.logic_dict[logic_id]
    
    def get_resource_by_id(self, resource_id):
        '''
        通过传入资源id,获取动画资源信息
        '''
        return self.resource_dict[resource_id]
    
    def get_next_resource(self):
        '''
        获取下一帧资源记录
        '''
        # 获取图像
        note = self.animation_player.get_next_frame()
        img = note["图像"]
        
#         print(note)
#         # 检查翻转
        if(self.situation.isMirrorImage()==True):
            img = img.mirrored(True, False)
        return img,note

    def changeAnimationByID(self, animation_id):
        '''
        根据传入的动作ID更变动作，强制变更
        '''
        self.animation_player.change_animation_by_animation_id(animation_id)
        
    def change_Aniamtion_by_signal(self, signal_name):
        '''
        根据传入的信号更变动作，强制变更。
        '''
        aim = self.signal_Animation.signal_animation_dict.get(signal_name)
        if(aim is None):
            return
        if(aim["当前动画id"] is not None and aim["当前动画id"] != self.animation_player.now_register.animation_id):
            return
        if(aim["发生条件"] is not None and check_all_condiction_in_list(aim["发生条件"]) == False):
            return
        
        self.changeAnimationByID(aim.get("目标动画"))
    

if __name__ == '__main__':
    # 读取fairy信息
    from infoTool.load_Fairy_From_XML_File import get_FairyInfo
    fairy = get_FairyInfo("vat")
        
    # 加载动画
    from infoTool.load_Animation_from_xml import load_animation_from_xml
    animationConsole = load_animation_from_xml(fairy.id)
    for a in range(1,20):
        k = animationConsole.get_next_resource()
#         print(k)