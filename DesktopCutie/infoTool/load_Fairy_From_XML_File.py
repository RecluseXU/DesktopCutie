# -*- coding: utf-8 -*-
'''
Created on 2019年1月10日

@author: RecluseXu
'''
import xml.etree.cElementTree as ET
import os
from model.Fairy import Fairy

def load_CutieInfo_from_XML(xmlLocation=""):
    #从保存Cutie信息的xml中获取信息，保存为Cutie类实例返回
    tree = ET.parse(xmlLocation) 
    root = tree.getroot()   # 获取根节点

    fairy = Fairy(root.attrib.get("id"))
    fairy.name = root.attrib.get("name")
    
    from infoTool.load_Project_Location import get_ProjectLocation
    a = root.find("动作设定文件")
    fairy.resourceLocation = get_ProjectLocation() + a.attrib.get("路径")
    
    a = a.attrib.get("缩放比例")
    if(a is not None):
        fairy.animationSizeScale = float(a)
    else:
        fairy.animationSizeScale = 1
    
    a = root.find("标识")
    if(a is not None):
        a = a.attrib
        fairy.author = a.get("作者")
        fairy.version = a.get("版本")
        fairy.license = a.get("许可")
        fairy.fairyINFO = a.get("信息")
    
    a = root.find("窗口")
    fairy.initWindowLocation = a.attrib.get("初始位置").split(",")
    fairy.windowLocationLimited_X = [int(x) for x in a.attrib.get("水平位置限制").split(",")]
    fairy.windowLocationLimited_Y = [int(x) for x in a.attrib.get("垂直位置限制").split(",")]
    
    fairy.fairySetXMLLocation = xmlLocation
    
    return fairy

CutieXmlDict = None # 用于保存已经扫描出来的Cutie-XML
def scan_FairyXML(reScan=False):
    #扫描resource文件夹下的xml，将找到的xml文件路径,保存到CutieXmlDict
    # 当再次调用函数，如果不传入True，那么将直接用上次的结果返回
    
    global CutieXmlDict
    if(CutieXmlDict is None or reScan==True):
    # 获取资源路径下所有xml文件，认为都是Fairy注册文件。
        from infoTool.load_Project_Location import get_resourceLocation
        xmlDict = {}
        path = get_resourceLocation()
        print("扫描resource目录下所有xml文件......")
        f_list = os.listdir(path)
        for i in f_list:
            # os.path.splitext():分离文件名与扩展名
            if(os.path.splitext(i)[1] == '.xml'):
                xmlDict[i.replace(".xml","")] = path + i
        return xmlDict
    else:
        return CutieXmlDict

def get_FairyInfo(fairyID, reScan=False):
    #通过传入ID,获取对应Fairy类实例
    global CutieXmlDict
    if(CutieXmlDict is None or reScan==True):
        CutieXmlDict = scan_FairyXML(reScan)
    if(type(CutieXmlDict.get(fairyID))== type("字符")):
        aimFairy_xmlAddress = CutieXmlDict.get(fairyID)
        CutieXmlDict[fairyID]=load_CutieInfo_from_XML(aimFairy_xmlAddress)
    return CutieXmlDict[fairyID]
    
    
if __name__ == '__main__':
    print(get_FairyInfo("demo"))
    print(get_FairyInfo("vat"))