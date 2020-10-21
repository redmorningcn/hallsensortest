import  ctypes
import  RPi.GPIO as GPIO

import  time
import  threading
#import  platform

PWM = ctypes.cdll.LoadLibrary('./pwm.so')
#if platform.system() == "Linux":
    #Checker = ctypes.cdll.LoadLibrary("./CrcCheck.so")
#Frqer   = ctypes.cdll.LoadLibrary("./GPIO_counter.so")
#PWM = ctypes.cdll.LoadLibrary('./pwm.so')
#else:
    #Checker = ctypes.cdll.LoadLibrary(".\\CrcCheck.dll")
    #Frqer   = ctypes.cdll.LoadLibrary(".\\GPIO_counter.dll")
    #PWM = ctypes.cdll.LoadLibrary('./pwm.so')
#低速模式：采用短暂启动方式实现

l_pwnvalue = 0
l_times    = 0


#按键监视程序
def   daemonLowSpeed():
    global      l_pwnvalue
    global      l_times
    while True:        
        l_times += 1
        if  l_times > 50:
            l_times = 0
            #print("l_pwnvalue",l_pwnvalue)
            
        time.sleep(0.0005)
        if l_pwnvalue < 550:     #低速启动
            if l_pwnvalue < 50:
                PWM.SetPWM(0)
                #print("l_pwnvalue 0",l_pwnvalue)
            else:
                
                if   l_times < (int)(550 - l_pwnvalue)/12 :
                    PWM.SetPWM(250)
                    #print("l_pwnvalue 2500",l_pwnvalue)
                else:
                    PWM.SetPWM(550)
                    #print("l_pwnvalue 500",l_pwnvalue)


#方向信号
l_directionflg = 0
PIN_DIR = 13
def  setdir(dir):
    global l_directionflg
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_DIR, GPIO.OUT)
    
    if dir == 1:
        GPIO.output(PIN_DIR,GPIO.HIGH)
        GPIO.output(PIN_DIR,GPIO.HIGH)
        if GPIO.input(PIN_DIR)==1:
            l_directionflg = 1
            
    if dir == 0:
        GPIO.output(PIN_DIR,GPIO.LOW)
        GPIO.output(PIN_DIR,GPIO.LOW)
        if GPIO.input(PIN_DIR) == 0:
            l_directionflg = 0
            
def  changedirection():
    global l_directionflg
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_DIR, GPIO.OUT)
    GPIO.setwarnings(False)

    if l_directionflg == 0:
        GPIO.output(PIN_DIR,GPIO.HIGH)
        GPIO.output(PIN_DIR,GPIO.HIGH)
        if GPIO.input(PIN_DIR)==1:
            l_directionflg = 1
    else:
        GPIO.output(PIN_DIR,GPIO.LOW)
        GPIO.output(PIN_DIR,GPIO.LOW)
        if GPIO.input(PIN_DIR) == 0:
            l_directionflg = 0
            
    print("l_directionflg",l_directionflg)

def getChangeDircetion():
    global l_directionflg
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_DIR, GPIO.OUT)
    
    if GPIO.input(PIN_DIR)==1:
        l_directionflg = 1
    else:
        l_directionflg = 0
    return l_directionflg


def getpwnvalue():
    global      l_pwnvalue
    return      l_pwnvalue


l_speed = 0                            #全局变量 50-1024 //分频值
#速度加，每调用一次，速度加1
def speedadd():
    global      l_speed
    global      l_pwnvalue
    
    if l_speed > 0:                     #速度有初始值，在原值上加
        if l_speed < 300:
            speed = l_speed + 3
        elif l_speed < 400:
            speed = l_speed + 4
        else:
            speed = l_speed + 5
            
        if speed > 850:
            speed = 850             #最大值为100
    else:
        speed = 140
    print("\r\n speed add %d"%speed )

    l_speed = speed                     #保存设置值
    l_pwnvalue = l_speed
    PWM.SetPWM(speed)                   #设置速度值



#速度减，每调用一次，速度减1
def speedsub():
    global      l_speed
    global      l_pwnvalue
    if l_speed > 150:
        speed = l_speed -5
    else:
        speed   = 0
    print("\r\n speed sub %d %d"%(speed,l_pwnvalue ))        
    l_speed = speed                     #保存设置值
    l_pwnvalue = l_speed
    PWM.SetPWM(speed)                   #设置速度值

#速度停止，速度减0
def speedstop():
    global      l_speed
    global      l_pwnvalue    
    l_speed = 0
    l_pwnvalue = l_speed
    PWM.SetPWM(0)                       #设置速度值

from    keyer              import *

KEY_SUB    = 7                                                      #速度-   （引脚号）
KEY_ADD    = 3                                                       #速度+   （引脚号）

if __name__=="__main__":
    initKey(KEY_SUB)                                                    #初始化速度-按键
    initKey(KEY_ADD)                                                    #初始化速度+按键
    KeyThread = threading.Thread(target = daemonKey)   #创建多线程，启动接收任务
    KeyThread.start() 

    #初始化PWM端口，
    PWM.initPWM(12)    
    PWM.SetPWMClock(4)
    
    LowThread = threading.Thread(target = daemonLowSpeed)     #创建多线程，启动接收任务
    LowThread.start()        
    while True:
        print("占空比X/1024：")
        ratio = int(input())
        #ratio = 491
        PWM.SetPWM(ratio)
        l_pwnvalue = ratio
        #ratio = int(input())

    
        #设置PWN的时钟分频系数，值越大，产生波形频率越小（频率越大，越平稳;越小力越大）
        #print("分频系数：")
        #clock = int(input())
        #PWM.SetPWMClock(clock)
        
        #GPIO.output(13, GPIO.HIGH)
