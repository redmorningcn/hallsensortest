
# -*- coding: utf-8 -*-

"""
Module implementing ui_main.
"""

from PyQt5.QtCore      import QThread, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets   import QMainWindow
from PyQt5.QtWidgets   import QMessageBox
from PyQt5             import QtCore, QtGui, QtWidgets


#from Ui_hallsensortest import Ui_MainWindow
from Ui_hallsensortest2 import Ui_Form
#from speedCtrol import *
import  threading

from    SetPWM             import *
from    GetMotorSpeed      import *
from    keyer              import *
from    shutdown           import *
from    gitIP              import *
from    websocketserver4   import *
from    webprotocol        import *
from    calcspeed          import *
from    loger              import *
from    ReadModSpeed       import *
from    SysConfig          import *

import  os,sys,time

KEY_SUB    = 7              #速度-   （引脚号）
KEY_ADD    = 3              #速度+   （引脚号）
KEY_SET    = 2              #设置按键 （引脚号）



'''
#采用多PYQT多线程10ms处理 程序
class MyThread10ms(QThread):  #重写线程类
    time10ms = pyqtSignal()          # 每隔一秒发送一个信号
    
    def __init__(self, parent=None):
        super(MyThread10ms, self).__init__(parent)
        self.num = 0
    
    def run(self):
        while True:
            self.time10ms.emit()     # 发送timeout信号
            time.sleep(0.08)         # 80ms发送一次
'''

#采用多PYQT多线程
class MyThread(QThread):  #重写线程类
    timeout     = pyqtSignal()      # 每隔一秒发送一个信号
    time10msout     = pyqtSignal()      # 每隔一秒发送一个信号

    deamontime  = pyqtSignal(int)   # 每隔一秒发送一个信号
    
    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        self.num = 0
    
    def run(self):
        self.num = 0
        while True:
    

            #if(self.num %2) ==0:
            self.num+=1
            if self.num %25 == 0:
                self.timeout.emit()     # 发送timeout信号

            if self.num % 25 == 12:
                self.deamontime.emit(int(self.num/25))

            if self.num % 8 == 7:
                self.time10msout.emit()     # 发送timeout信号

            time.sleep(0.01)
            #time.sleep(0.25)
            #self.sleep(1)

#取显示速度值
def getdisplaylocospeed():
    print("ui_main.displaylocospeed22  =",ui_main.getSpeed())
    #ui_main.getSpeed()
    return ui_main.d_speed



#class ui_main(QMainWindow, Ui_MainWindow):
class ui_main(QMainWindow, Ui_Form):
    """
    Class documentation goes here.
    """
    global confile
    d_speed = 10
    
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ui_main, self).__init__(parent)
        
        #setkey按下时间
        self.shutdownflg = 0
        self.shutdowntimeleft  = 50
        self.setkeystilltime   = 0
        self.setkeydowntime    = 0
        self.subkeydowntime    = 0
        self.subkeystilltime   = 0
        self.subkeytimes       = 0
        
        self.setrotatespeed    = 0                     # 设置的转速（如果装置没有反馈速度值，则以该值做速度有无的判断）
        
        self.setobj            = 0                     # 设置对象(0,转速;1,机车轮径;2,速度;3方向)
        self.objnum            = 4
                  # 读配置文件中的机车轮径
        self.locospeed         = 0                     # 机车速度
        self.dir               = 0                     # 方向

        self.showtimes         = 0

        self.lstrotate         = -1                     #设定转速
            
        self.setupUi(self)
        #self.show()                                    #全屏显示
        self.showFullScreen()                           #全屏显示
        
        
        speedstop()                                     #速度设置为0
       # try:
       #     self.confile = ReadConfig()                     #读取配置文件
       # except:
       #     print("# 打开运行曲线实列失败add")
            
        self.diameter          = 840                  # 机车轮径
        self.diameter          = int(self.confile.Speed("diameter")) #不能读配置文件，读取配置问价，界面不能运行

        #self.mythread10ms = MyThread10ms()
        self.modrunflg      = 0             #模拟曲线运行标识
        self.modruntimes    = 0             #模拟运行次数标识
        self.modcurrent     = 0             #模拟运行当前值

        self.mythread       = MyThread()    #实例化线程
        self.mythread.timeout.connect(self.showSpeed)   #连接线程类中自定义信号槽到本类的自定义槽函数
        self.mythread.deamontime.connect(self.daemon)   #连接线程类中自定义信号槽到本类的自定义槽函数
        try:
                        #模式选择
            debug = int(self.confile.Debug("Debug"))
            if debug == 1:                      #如果是调试模式，则启动模拟运行进行
                #self.mythread10ms.start()       #开启线程不是调用run函数而是调用start函数
                self.speedtalbe     = SpeedTable()  #模拟运行曲线实列
                self.mythread.time10msout.connect(self.modSpeed)
                        
        except:
            print("# 打开运行曲线实列失败add")
        self.mythread.start()                           #开启线程不是调用run函数而是调用start函数
        

    def diameterAdd(self):                             # 机车轮径增加
        print("#机车轮径增加")
        self.diameter += 1
        
        if  self.diameter > 1300:
            self.diameter = 1300
        self.confile.WriteSpeed("diameter",str(self.diameter))

    def diameterSub(self):                             # 机车轮径减小
        print("# 机车轮径减小")
        self.diameter -= 1
        
        if  self.diameter < 800:
            self.diameter = 800

        self.confile.WriteSpeed("diameter",str(self.diameter))

    def locospeedadd(self):                            # 机车速度增加
        try:
            self.locospeed += 0.5
            print("# 机车速度增加",self.locospeed)
            
            if  self.locospeed > 100:
                self.locospeed = 100
            
            self.setrotatespeed = calclocorotate(self.locospeed, self.diameter)  #计算转速
            
        except:
            print("# 机车速度减少add")

    def locospeedsub(self):                            # 机车速度减少
        try:
            print("# 机车速度减少")
            if self.locospeed  >= 1:
                self.locospeed -= 0.5
                
            if  self.locospeed < 1.5:
                self.locospeed = 0
            
            self.setrotatespeed = calclocorotate(self.locospeed, self.diameter)  #计算转速
            
            
        except:
            print("# 机车速度减少sub")

    def rotatesspeedadd(self):                         # 转速增加
        try:
            print("# 转速增加",self.setrotatespeed)
            self.setrotatespeed += 1
            
            if  self.setrotatespeed > 500:
                self.setrotatespeed = 500
            
            self.locospeed = calclocospeed(self.setrotatespeed,self.diameter )
            print("# 转速增加self.locospeed ",self.locospeed )
        except:
            print("转速计算错误add！")

    def rotatesspeedsub(self):                         # 转速减少
        try:
            print("# 转速减少",self.setrotatespeed)
            if self.setrotatespeed > 1:
                self.setrotatespeed -= 1
            
            if  self.setrotatespeed < 10:
                self.setrotatespeed = 0
                
            self.locospeed = calclocospeed(self.setrotatespeed,self.diameter )
            print("# 转速减少self.locospeed ",self.locospeed )

        except:
            print("转速计算错误sub！")
    
    @classmethod
    def getSpeed(cls):
        return cls.d_speed
    
    def showSpeed(self):                                # 显示速度值

        #while True:
        if True:
            #time.sleep(0.25)
            self.showtimes+=1

            try:
                self.ln_locol.display( self.diameter )              # 显示机车轮径
                
                self.ln_motorspeed.display(self.setrotatespeed )    # 显示转速
                 
                self.ln_locolspeed.display(self.locospeed )         # 显示速度

                if self.dir == 0:              # 机车方向
                    self.com_rotatedir.setCurrentIndex(0)
                    dir = "right"
                else:
                    self.com_rotatedir.setCurrentIndex(1)
                    dir = "left"
                
                if self.shutdownflg == 0:     #关机，用该位置显示倒计时
                    self.label.setText("霍尔传感器便携式测试设备")

                ### 根据要设置的参数，闪烁提醒
                if self.setrotatespeed == 0:
                    if self.setobj == 0:       #转速
                        #self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)    

                        if self.showtimes % 5 == 0:
                            self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
                        else:
                            self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                    
                    if self.setobj == 1:       #轮径
                        if self.showtimes % 5 == 0:
                            self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
                        else:
                            self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                            
                    if self.setobj == 2:       #速度
                        #self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)

                        if self.showtimes % 5 == 0:
                            self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
                        else:
                            self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                            
                    if self.setobj == 3:       #方向
                        if self.showtimes % 5 == 0:
                            self.com_rotatedir.setCurrentIndex(2)
                        else:
                            self.com_rotatedir.setCurrentIndex(self.dir)
                else:
                    self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                    self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                    self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)   
                    

                ### 获取并显示IP值
                try:
                    if self.showtimes % 5 == 0:
                        ip = get_host_ip()
                        self.label_IP.setText(ip)
                except:
                    ip = '8.8.8.8'
                    self.label_IP.setText(ip)
                    print(" wifi未连接")

                if (self.showtimes %2) == 0:
                    try:    
                        text = ("%s,%s,%s,%s,%s,%s")%("none",dir,"none",str(self.locospeed),str(self.setrotatespeed),str(self.diameter))
                        webSendMessage(text)
                        #print("self.showtimes",self.showtimes)
                        #QApplication.processEvents()  
                    except:
                        print("webSendMessage(text):err!")

            except Exception as e:
                print("速度读取错误", e)
        
    #daemon，多线程
    def  daemon(self,daemontime):

        
        #电机参数
        rotaterate        = getrotaterate()           #同步轮齿数比
        pwmrate           = getpwmrate()              #步进电机分频系数
        
        #while True:
        if True:            
            #time.sleep(0.25)

            pwmfre = (self.setrotatespeed * rotaterate * pwmrate) / 60;
            speedset(pwmfre)  #根据设置的转速值，设置频率
            
            self.dir = getChangeDircetion()                                     #读取方向信号
            
            ### 关机倒计时
            if self.shutdownflg == 1:
                if self.shutdowntimeleft > 0:
                    print("self.shutdowntimeleft ",self.shutdowntimeleft)
                    self.shutdowntimeleft-=1
                    times = self.shutdowntimeleft/5
                    tmp = "" + str(int(times))+"秒后关机！"
                    
                    self.label.setText(tmp)
                    #self.textEdit.setText(tmp)
                else:
                    print("shutdown()")
                    shutdown()  #启动关机程序

            ###web设置值（）速度、轮径、转速、方向等
            webspeed  = getwebsetspeed()
            webrotate = getwebsetrotate()
            webdim    = getwebsetdim()

            #轮径800到1500
            if webdim <= 1500 and  webdim >= 800:
                self.diameter  = webdim
                self.locospeed = calclocospeed(self.setrotatespeed,self.diameter )
                
            #速度为零，设置方向
            webdir    = getwebsetdir()
            if self.locospeed <= 2 and webdir !=-1:
                if self.dir != webdir:      #方向不同，设置方向
                    changedirection()
            else:
                webdir = -1

            #print("webspeed",webspeed)
            #速度和转速设置，互斥只能设置一个，且需要控制调整速率
            if webspeed != -1:
                self.lstrotate = calclocorotate(webspeed,self.diameter)+1  #转速值偏小，加1后速度值相同
                if self.lstrotate == 1:     #消除要求设置为0的情况
                    self.lstrotate = 0
                webrotate   = -1
            
            if webrotate != -1:
                self.lstrotate = webrotate
                webspeed = -1

            #缓慢加减速度
            if self.lstrotate >= 0 and self.lstrotate <=500:
                if  self.lstrotate > self.setrotatespeed:
                    #速度+
                    self.rotatesspeedadd()
                elif self.lstrotate < self.setrotatespeed:
                    #速度-
                    self.rotatesspeedsub()
                else:
                    self.lstrotate = -1
            else:
                self.lstrotate = -1
            
            
            ### 速度0时，可以选择 参数调整 功能
            if self.setrotatespeed == 0:

                if getKeySta(KEY_SET):
                    #功能设置按键按下，进行相应的功能选择。
                    if daemontime != self.setkeydowntime +1:        # 不是长按状态（连续进入则认为是长按）
                        self.setkeystilltime  = 0                   # 按键长按计时开始
                        
                        self.setobj += 1                            # 设置对象往下偏移
                        self.setobj %= self.objnum                  # 范围限制                        
                    else:
                        self.setkeystilltime += 1                   # 按键保持按下状态
                        if self.setkeystilltime > 25:               # 5s #在速度为0情况下，长按设置按键5s，设备关机。
                            self.shutdownflg = 1
                            
                    self.setkeydowntime = daemontime                # 记录设置按键按下时间（判断是长时间、短时间按键）。
                    
                keysub = getKeySta(KEY_SUB) or getwebspeedsubflg()
                keyadd = getKeySta(KEY_ADD) or getwebspeedaddflg()
                
                if  keysub or keyadd:                       #有按键按下
                    
                    #有其他按键，设置按键清零
                    
                    if self.shutdownflg == 1:               #如果是在关机倒计时，则只取消关机过程
                        self.shutdownflg = 0                #关机过程中，有其他按键按下，取消关机           
                        self.shutdowntimeleft = 50          #重新赋值
                    else:
                        if keyadd:                          #按键+
                            if   self.setobj == 0:          #转速
                                self.rotatesspeedadd()               
                            elif self.setobj == 1:          #轮径
                                self.diameterAdd()
                            elif self.setobj == 2:          #速度    
                                self.locospeedadd()
                            else:                           #改变方向

                                print("keysub,keyadd1",keyadd,keysub)
                                changedirection()                        
                        else:                               #按键-
                            if   self.setobj == 0:          #转速
                                self.rotatesspeedsub()               
                            elif self.setobj == 1:          #轮径
                                self.diameterSub()
                            elif self.setobj == 2:          #速度    
                                self.locospeedsub()
                            else:                           #改变方向
                                print("keysub,keyadd2",keyadd,keysub)
                                changedirection()
                        
            ###  速度不为零        
            if self.setrotatespeed != 0:

                
                # 在速度不为零时，只能调整转速和速度值。默认设置为转速
                if  self.setobj == 1 or self.setobj == 3:     # 轮径设置 或 方向设置
                    self.setobj =  0

                key_add = getKeySta(KEY_ADD)
                key_sub = getKeySta(KEY_SUB)

                #判断速度减多击键
                if key_sub:             #按键按下
                    if daemontime != self.subkeydowntime +1:        # 不是长按状态（连续进入则认为是长按）
                        self.subkeytimes +=1
                        self.subkeystilltime = 0
                    else:                                           # 长按状态
                        self.subkeystilltime +=1
   
                        if self.subkeystilltime > 5:                # 持续按键
                            self.subkeytimes = 0                    # 取消按键次数判断
                        #elif self.subkeystilltime==1:              # 快速按键
                            #self.subkeytimes += 1
                        
                    self.subkeydowntime = daemontime                # 记录按键按下时间（判断是长时间、短时间按键）。
                    print("self.subkeytimes",self.subkeytimes,self.subkeystilltime,self.subkeydowntime)
                else:
                    self.subkeystilltime = 0

                    if daemontime > self.subkeydowntime + 3 :       #间隔时间过长，取消按键次数判断
                        if self.subkeytimes:
                            print("IF Self.subkeytimes",self.subkeytimes)
                            if self.subkeytimes == 3:               #连续按3次，则速度降为0
                                self.lstrotate = 0
                                print("self.subkeytimes == 3")
                        
                        self.subkeytimes = 0                              
                            

                # 按加、减按键，进行速度的增减
                if key_add  or getwebspeedaddflg():
                    self.lstrotate = -1             #有按键操作，取消预设值
                    
                    if self.setobj == 0:
                        self.rotatesspeedadd()    
                    elif self.setobj == 2:          #速度
                        self.locospeedadd()
                    else:
                        print("在非0时，按速度加")

                        
                elif  key_sub  or getwebspeedsubflg():
                    self.lstrotate = -1             #有按键操作，取消预设值
                    
                    if self.setobj == 0:
                        self.rotatesspeedsub()               
                    elif self.setobj == 2:          #速度
                        self.locospeedsub()
                    else:                    
                        print("在非0时，按速度减")                     
            
    def modSpeed(self):                                 #模拟速度运行
        try:
            if self.modrunflg == 0:
                if self.setrotatespeed == 0 :               #当前速度为零
                    if getKeySta(KEY_SET):                  #按设置按键，开始启动
                        self.modrunflg      = 1
                        self.modruntimes    = self.speedtalbe.getspeedline()
                        self.modcurrent     = 0
            else:
                if self.modcurrent < (self.modruntimes-1) and (self.modruntimes > 0):      #开始模拟运行
                    speed = self.speedtalbe.getmodspeed(self.modcurrent)
                    self.modcurrent+=1
                    
                    rotate =  calclocorotate(speed, self.diameter)  #计算转速

                    self.setrotatespeed = rotate /100
                    locospeed = calclocospeed(rotate,self.diameter )
                    self.locospeed = locospeed /100               
            
                else:                                       #模拟运行结束
                    self.modrunflg      = 0
                    self.modruntimes    = 0
                    self.modcurrent     = 0                
        except Exception as e:
                print("模拟运行错误", e)


def initGPIO():
    
    initKey(KEY_SUB)                                                    #初始化 速度-按键
    initKey(KEY_ADD)                                                    #初始化 速度+按键
    initKey(KEY_SET)                                                    #初始化 设置按键
    
    KeyThread = threading.Thread(target = daemonKey)                    #创建多线程，启动接收任务
    KeyThread.start()
    
    FRQ_IN     = 21                                                     #频率采集    
    Frqer.initFrq(FRQ_IN)                                               #频率检测电路引脚

    tfrq    = threading.Thread(target = Frqer.threadCounter)
    tfrq.start()
    
    PWM.initPWM(12)
    #PWM.SetPWMClock(2048)
    
    #PWM.SetPWMClock(4)    
    #启动多线程
    LowThread = threading.Thread(target = daemonSpeedSet)               #创建多线程，变化速度值
    LowThread.start()
    
    #tsec    = threading.Thread(target = taskSecond)
    #tsec.start()
    #启动websocketserver
    startServer()           #启动服务
    startWebProtocol()      #启动通讯协议
    

if __name__ == "__main__":
    #time.sleep(0.5)
    sys.stdout = Logger(sys.stdout) #将输出记录到log
    sys.stderr = Logger(sys.stderr) #将错误信息记录到log


    initGPIO()                      #脉冲检测及按键端口初始化

    app = QtWidgets.QApplication(sys.argv)
    ui = ui_main()
    sys.exit(app.exec_())
	
	

