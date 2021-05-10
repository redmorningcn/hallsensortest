import  ctypes
from    SetPWM             import *

l_pwmrate       = 1600            # 步进电机分频系数 
l_rotaterate    = 4               # 设置齿轮传动比


# 取步进点击的分频系数
def getpwmrate():
    global      l_pwmrate
    return      l_pwmrate

# 齿轮传动比
def getrotaterate():
    global      l_rotaterate
    return      l_rotaterate


    
# 速度计算
def calclocospeed(rotate,diameter = 1050):
    locospeed = (int)((rotate * 3.14 * diameter) *60 / (1000*1000))
    return locospeed

# 转速计算
def calclocorotate(locospeed,diameter = 1050):
    rotate = (int)((locospeed * 1000 * 1000) /(3.14 * diameter *60))
    return rotate


    
    
    
