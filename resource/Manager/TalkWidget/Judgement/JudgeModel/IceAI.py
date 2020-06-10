# -*- coding: utf-8 -*-

'''
Created on 2019年3月11日

@author: RecluseXu
使用wxpy调用微信内容以达到和小冰聊天的目的
    xpy文档:https://wxpy.readthedocs.io/zh/latest/index.html
'''

# 导入模块
from wxpy import Bot
from model.CLASS.JudgeResoult import JudgeResoult
from time import sleep
from infoTool.load_Project_Location import get_resourceLocation

bot = None
ice = None
ice_reply = None

def _init():
    global bot
    global ice
    print("小冰AI初始化......")
    # 设置一个保存登陆账户文件的文件
    loacation = get_resourceLocation()+"Manager/TalkWidget/reply/wxpy.pkl"
    
    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=loacation)
    ice = bot.mps(update=False).search("小冰") # 在公众号里找到小冰
    if(len(ice) == 1):
        ice = ice[0]
    else:
        global ice_reply
        ice_reply ="尚未关注小冰"
    
    # 注册事件，当接收到来自小冰的信息时，执行，将信息保存
    @bot.register(chats=ice)
    def print_group_msg(msg):
        global ice_reply
        if(ice_reply is None):
            ice_reply = msg
        if(isinstance(ice_reply, str)):
            ice_reply = ice_reply + msg
    
    
def send_message_to_ice(message_str):
    global ice
    # 消息先发过去
    if(ice is None):
        _init()
    ice.send_msg(message_str)
    

def get_message():
    # 每隔0.5秒尝试获取一次信息，一共尝试10次
    try_times = 11
    global ice_reply
    while(try_times > 0):
        try_times = try_times-1
        sleep(0.5)
        # 当获取到了回复
        if(ice_reply is not None):
            # 清理全局变量再返回
            rep = ice_reply
            ice_reply = None
            return rep
        
    return "小冰并未给你回复，或许现在网络不好，你可以等下再试试"
    
def destory():
    global bot
    # 登出
    bot.logout()
    bot = None
    ice = None






#-----------------------------------------------------

def judge(input_str):
    # 先将消息发给小冰，由于网络是有延迟的，所以先发，过一会儿再看看有没有回复可以收
    send_message_to_ice(input_str)
    
    judge_resoult = JudgeResoult(input_str,True)
    judge_resoult.operation_str = "ChatIce"
    judge_resoult.parameter = input_str
    judge_resoult.judge_type = "ChatIce"
    # 尝试接收消息
    judge_resoult.reply = get_message()
    
    return judge_resoult

if __name__ == '__main__':
    send_message_to_ice("你好，小冰")
    print(get_message())