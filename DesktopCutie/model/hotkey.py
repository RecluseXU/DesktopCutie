# -*- coding: utf-8 -*-
'''
Created on 2019年3月8日

@author: RecluseXu
'''

import ctypes, win32con, ctypes.wintypes, win32gui
import threading
from infoTool.load_Project_Location import get_resourceLocation
from infoTool.load_ini_configure import load_ini_value, set_ini_value


hotkey_threading = None
hotkey1 = None
hotkey2 = None


class Hotkey(threading.Thread):
    def run(self, press_function):
        '''
        运行，开始监听系统按键，当按下热键，执行传入的press_function,返回结果。
        '''
        global hotkey1,hotkey2
        if(hotkey1 is None or hotkey2 is None):
            return "尚未设置热键"
        
        user32 = ctypes.windll.user32
        if(not user32.RegisterHotKey(None, 99, hotkey1, hotkey2)):
#             raise RuntimeError # 看看注册的热键有没有被占用了，有就报错好了
            return "键位已被占用"
        try:
            msg = ctypes.wintypes.MSG()
            while(user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0):
                if(msg.message == win32con.WM_HOTKEY): 
                    # 当你按下热键
                    if(msg.wParam == 99):
                        # 执行传入的按下函数
                        user32.UnregisterHotKey(None, 1)
                        return press_function()
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 99) # 注销热键

def _translate_key_str_to_win_key(key_str):
    '''将按键str转换为win32con中的变量'''
    key_mapper = {
        "ALT":win32con.MOD_ALT,
        "CTRL":win32con.MOD_CONTROL,
        "SHIFT":win32con.MOD_SHIFT,
        "WIN":win32con.MOD_WIN,
        "F1":win32con.VK_F1,
        "F2":win32con.VK_F2,
        "F3":win32con.VK_F3,
        "F4":win32con.VK_F4,
        "F5":win32con.VK_F5,
        "F6":win32con.VK_F6,
        "F7":win32con.VK_F7,
        "F8":win32con.VK_F8,
        "F9":win32con.VK_F9,
        "F10":win32con.VK_F10,
        "F11":win32con.VK_F11,
        "F12":win32con.VK_F12  
        }
    return key_mapper.get(key_str)

def set_hot_key(input_hotkey1, input_hotkey2):
    '''
    设置热键，顺便检查是否可行
    '''
    # 将输入的按键字符转换为win32con中的变量
    hotkey1_win,hotkey2_win = _translate_key_str_to_win_key(input_hotkey1),_translate_key_str_to_win_key(input_hotkey2)
    
    # 检查键位是否被占用
    user32 = ctypes.windll.user32
    if(not user32.RegisterHotKey(None, 99, hotkey1_win,hotkey2_win)):
        return False
    else:
        user32.UnregisterHotKey(None, 99) # 注销热键
    
    # 保存键位到变量
    global hotkey1, hotkey2
    hotkey1,hotkey2 = hotkey1_win,hotkey2_win
    
    # 保存键位到设置文档
    location = "D:/github_repository/DesktopFairy/DesktopCutie/resource/Manager/ManagerConfigure.ini"
    aim_list = [["TalkFrame","unhide_hotkey1",input_hotkey1], ["TalkFrame","unhide_hotkey2",input_hotkey2]]
    set_ini_value(location,aim_list)
    
    return True
    
def _init_things():
    global hotkey1, hotkey2, hotkey_threading
    if(hotkey1 is None or hotkey2 is None):
        location = "D:/github_repository/DesktopFairy/DesktopCutie/resource/Manager/ManagerConfigure.ini"
        aim_list = [["TalkFrame","unhide_hotkey1"], ["TalkFrame","unhide_hotkey2"]]
        key_list = load_ini_value(location, aim_list)
        hotkey1,hotkey2 = list(map(_translate_key_str_to_win_key, key_list))
    if(hotkey_threading is None):
        hotkey_threading = Hotkey()
    
def start_listen_hot_key(press_function):
    '''
    启动一个监听热键的线程,监听到热键输入后执行按下函数(press_function)
    '''
    global hotkey_threading
    
    if(hotkey_threading is None):
        _init_things()
    return hotkey_threading.run(press_function)

def stop_listen_hot_key():
    global hotkey_threading
    if(hotkey_threading.isAlive()):
#         print("alive")
        return 
#     print("not alive")
    hotkey_threading = None
    


if __name__=="__main__":
    print(set_hot_key("ALT", "F4"))
    a=start_listen_hot_key(lambda: print("!"))
    print(a)
    stop_listen_hot_key()
