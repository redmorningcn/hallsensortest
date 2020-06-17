
'''
作者：redmorningcn   200606
描述：直流电机控制板ZK-ZT2，速度加和速度减函数

'''
from  zkzt2_com2  import *

STA_CW  = 0x00              #正转
STA_CCW = 0x01              #反转
STA_STOP= 0x02              #停止
STA_SD  = 0x03              #刹车

l_speed = 0                            #全局变量
l_frq   = 0

if platform.system() == "Linux":
    port = "/dev/ttyUSB0"
        #port = "/dev/ttyUSB1"
else:
    port  = "COM10"
        
motor   = Zkzt2Data(port)
    

#速度加，每调用一次，速度加1
def speedadd():
    global      l_speed
    global      l_frq
    
    if l_speed > 0:                     #速度有初始值，在原值上加
        speed = l_speed +1
        if speed > 100:
            speed = 100                 #最大值为100
    else:
        speed = 20

    fre = 3000
    
    motor.setSpeed(speed,fre,STA_CCW)   #设置速度值
    l_speed = speed                     #保存设置值
    

#速度减，每调用一次，速度减1
def speedsub():
    global      l_speed
    global      l_frq

    if l_speed > 15:
        speed = l_speed -1
    else:
        speed   = 0

    fre = 3000
            
    motor.setSpeed(speed,fre,STA_CCW)   #设置速度值
    l_speed = speed                     #保存设置值
    
#速度停止，速度减1
def speedstop():
    global      l_speed
    global      l_frq
    motor.setSpeed(0,0,STA_CCW)   #设置速度值
    l_speed = 0
    l_frq = 0

if __name__=="__main__":
    import time

    cnt = 0
    
    while True:
        time.sleep(1)
        
        if cnt < 150:
            speedadd()
        else: 
            speedsub()
            if cnt > 300:
                cnt = 0
            
        cnt+=1
        print("l_speed:",l_speed)
