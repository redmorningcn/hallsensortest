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

l_lstfrq    = 0     #上次频率值
l_setfrq    = 0     #设置频率值
l_times     = 0

# 速度监视程序
def   daemonSpeedSet():
    daemonfrqSet()
# 速度监视程序
def   daemonfrqSet():
    global      l_lstfrq
    global      l_setfrq   
    global      l_times
    while True:
        time.sleep(0.5)
        while   l_lstfrq != l_setfrq:
            if l_lstfrq < l_setfrq:       #设置值大，速度加
                l_lstfrq += 1
            
            if l_lstfrq > l_setfrq:       #设置值小，速度减
                 l_lstfrq -= 1
            
            PWM.SetFrq(l_lstfrq)          #设置速度值
            time.sleep(0.05)
            print("l_lstfrq %d,l_setfrq %d"%(l_lstfrq,l_setfrq))


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
    global      l_lstfrq
    return      l_lstfrq


l_speed = 0                            #全局变量 50-1024 //分频值
#速度加，每调用一次，速度加1
def speedadd():
    global      l_lstfrq
    global      l_setfrq
    
    l_setfrq = l_lstfrq + 5
    
    maxfrq   = 60000
    if l_setfrq > maxfrq:
        l_setfrq = maxfrq

def speedset(value = 0):
    global      l_setfrq
    
    maxfrq   = 60000
    if value > maxfrq:
        l_setfrq = maxfrq
    elif value < 0:
        l_setfrq = 0
    else:
        l_setfrq = value
    
#速度减，每调用一次，速度减1
def speedsub():
    global      l_lstfrq
    global      l_setfrq
    
    l_setfrq = l_lstfrq - 5
    
    minfrq   = 100
    if l_setfrq < minfrq:
        l_setfrq = 0


#速度停止，速度减0
def speedstop():
    global      l_lstfrq
    global      l_setfrq
    l_setfrq = 0
    l_lstfrq = l_setfrq
    PWM.SetPWM(l_setfrq)                       #设置速度值

from    keyer              import       *

KEY_SUB    = 7                                                      #速度-   （引脚号）
KEY_ADD    = 3                                                       #速度+   （引脚号）

if __name__=="__main__":
    initKey(KEY_SUB)                                                    #初始化速度-按键
    initKey(KEY_ADD)                                                    #初始化速度+按键
    KeyThread = threading.Thread(target = daemonKey)   #创建多线程，启动接收任务
    KeyThread.start() 

    #初始化PWM端口，
    PWM.initPWM(12)    
    PWM.SetPWMClock(2048)
    
    #LowThread = threading.Thread(target = daemonfrqSet)     #创建多线程，启动接收任务
    #LowThread.start()        
    while True:
        #print("占空比X/1024：")
        print("设置频率")
        ratio = int(input())
        #speedset(ratio)
        PWM.SetFrq(ratio)
        '''
        for ratio in range(100,60000,1):
            PWM.SetFrq(ratio)
            if (ratio % 100) == 0:
                print("设置脉冲数：%d，计算速度：%d"%(ratio,(int)(((ratio*60/1600))*3.1415*1.05*60*20/1000/72)))
            time.sleep(0.02)
        
        while True:
            time.sleep(0.5)          
        PWM.SetFrq(20000)
        time.sleep(0.5)
        '''
        #ratio = 491
        #PWM.SetPWM(ratio)
        #l_pwnvalue = ratio
        #ratio = int(input())

    
        #设置PWN的时钟分频系数，值越大，产生波形频率越小（频率越大，越平稳;越小力越大）
        #print("分频系数：")
        #clock = int(input())
        #PWM.SetPWMClock(clock)
        
        #GPIO.output(13, GPIO.HIGH)
