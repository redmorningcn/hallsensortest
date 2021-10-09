import  ctypes
#from    SetPWM             import *

l_pwmrate       = 1600            # 步进电机分频系数 
l_rotaterate    = 4.5               # 设置齿轮传动比(4)


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
    try:
        locospeed = (int)((rotate * 3.14 * diameter) *60 / (1000*1000))
    except:
        print("速度计算错误calclocospeed")
    return locospeed

# 转速计算
def calclocorotate(locospeed,diameter = 1050):
    try:
        rotate = (int)((locospeed * 1000 * 1000 ) /( 3.14 * diameter *60 ))
        #print("计算转速值：",rotate)
    except:
        print("转速计算错误calclocorotate")
    return rotate


    
    
    
