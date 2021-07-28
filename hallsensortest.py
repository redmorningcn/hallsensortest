
# -*- coding: utf-8 -*-

"""
Module implementing ui_main.
"""

from PyQt5.QtCore      import pyqtSlot
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
import  os,sys,time

KEY_SUB    = 7              #速度-   （引脚号）
KEY_ADD    = 3              #速度+   （引脚号）
KEY_SET    = 2              #设置按键 （引脚号）


#displaylocospeed = 0

def getdisplaylocospeed():
    print("ui_main.displaylocospeed22  =",ui_main.getSpeed())
    #ui_main.getSpeed()
    return ui_main.d_speed

#class ui_main(QMainWindow, Ui_MainWindow):
class ui_main(QMainWindow, Ui_Form):
    """
    Class documentation goes here.
    """
    d_speed = 10
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ui_main, self).__init__(parent)
        self.setupUi(self)
        self.showFullScreen()                   #全屏显示
        #self.show()                              #全屏显示
        
        time.sleep(1.5)                          #
        
        speedstop()                              #速度设置为0
        
        #self.thread1 = threading.Thread(target = self.showSpeed)        #显示速度值
        #self.thread1.start()
        time.sleep(2.5)                          #
        self.thread2 = threading.Thread(target = self.daemon)           #守护线程
        self.thread2.start()
        #关机daoji时
        self.shutdownflg = 0
        self.shutdowntimeleft  = 50
        
        self.setrotatespeed    = 0                     # 设置的转速（如果装置没有反馈速度值，则以该值做速度有无的判断）
        
        self.setobj            = 0                     # 设置对象(0,转速;1,机车轮径;2,速度;3方向)
        self.objnum            = 4
        
        self.diameter          = 1050                  # 机车轮径
        self.locospeed         = 0                     # 机车速度
        self.dir               = 0                     # 方向
    
    def diameterAdd(self):                             # 机车轮径增加
        print("#机车轮径增加")
        self.diameter += 1
        
        if  self.diameter > 1300:
            self.diameter = 1300

    def diameterSub(self):                             # 机车轮径减小
        print("# 机车轮径减小")
        self.diameter -= 1
        
        if  self.diameter < 800:
            self.diameter = 800

    def locospeedadd(self):                            # 机车速度增加
        
        self.locospeed += 0.5
        print("# 机车速度增加",self.locospeed)
        
        if  self.locospeed > 100:
            self.locospeed = 100
        
        self.setrotatespeed = calclocorotate(self.locospeed, self.diameter)  #计算转速
        
    def locospeedsub(self):                            # 机车速度减少
        print("# 机车速度减少")
        if self.locospeed  >= 1:
            self.locospeed -= 0.5
            
        if  self.locospeed < 1.5:
            self.locospeed = 0
        
        self.setrotatespeed = calclocorotate(self.locospeed, self.diameter)  #计算转速        

    def rotatesspeedadd(self):                         # 转速增加
        print("# 转速增加")
        self.setrotatespeed += 1
        
        if  self.setrotatespeed > 500:
            self.setrotatespeed = 500
        
        self.locospeed = calclocospeed(self.setrotatespeed,self.diameter )
        print("# 转速增加self.locospeed ",self.locospeed )

    def rotatesspeedsub(self):                         # 转速减少
        print("# 转速减少")
        if self.setrotatespeed > 1:
            self.setrotatespeed -= 1
        
        if  self.setrotatespeed < 10:
            self.setrotatespeed = 0
            
        self.locospeed = calclocospeed(self.setrotatespeed,self.diameter )
    
    @classmethod
    def getSpeed(cls):
        return cls.d_speed
    
    showtimes = 0
    def showSpeed(self):                               # 显示速度值
        #shutdowntimes = 0
        
        #while True:
            
        #    time.sleep(0.5)
        showtimes+=1
		
        dim2 = 1250                                # 机车轮径1250mm
        dim1 = 1050                                # 机车轮径1050mm
        try:
            self.ln_locol.display( self.diameter ) # 显示机车轮径
            
            self.ln_motorspeed.display(self.setrotatespeed ) #显示转速
            
            self.ln_locolspeed.display(self.locospeed )    #显示速度
            
            if self.dir == 0:
                dir = "right"
            else:
                dir = "left"
            text = ("%s,%s,%s,%s,%s,%s")%("none",dir,"none",str(self.locospeed),str(self.setrotatespeed),str(self.diameter))
			
			if(showtimes %2 == 0):
				webSendMessage(text)
            #ui_main.d_speed = self.locospeed
            #print("ui_main.displaylocospeed",ui_main.d_speed)
            
            if self.dir == 0:              # 机车方向
                self.com_rotatedir.setCurrentIndex(0)
            else:
                self.com_rotatedir.setCurrentIndex(1)
            
            if self.shutdownflg == 0:     #关机，用该位置显示倒计时
                self.label.setText("霍尔传感器便携式测试设备")
            
        except Exception as e:
            print("速度读取错误", e)
        
    #daemon，多线程
    def  daemon(self):
        #setkey按下时间
        setkeytimes       = 0
        setkeydowntime    = 0
        setkeystilltime   = 0
        
        #时间变量
        daemontime        = 0     
        lstrotate         = 0                         #设定转速
        #电机参数
        rotaterate        = getrotaterate()           #同步轮齿数比
        pwmrate           = getpwmrate()              #步进电机分频系数
        
        while True:
            time.sleep(0.2)
            daemontime +=1                                                      #时间变量
            
            self.showSpeed()           #参数显示
            
            pwmfre = (self.setrotatespeed * rotaterate * pwmrate) / 60;
            speedset(pwmfre)  #根据设置的转速值，设置频率
            
            self.dir = getChangeDircetion()                                     #读取方向信号
            
            ### 根据要设置的参数，闪烁提醒
            if self.setrotatespeed == 0:
                if self.setobj == 0:       #转速
                    if daemontime % 5 == 0:
                        self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
                    else:
                        self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                
                if self.setobj == 1:       #轮径
                    if daemontime % 5 == 0:
                        self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
                    else:
                        self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                        
                if self.setobj == 2:       #速度
                    if daemontime % 5 == 0:
                        self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
                    else:
                        self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                        
                if self.setobj == 3:       #方向
                    if daemontime % 5 == 0:
                        self.com_rotatedir.setCurrentIndex(2)
                    else:
                        self.com_rotatedir.setCurrentIndex(self.dir)
            else:
                self.ln_motorspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                self.ln_locol.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                self.ln_locolspeed.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                
            ### 获取并显示IP值        
            ip = get_host_ip()
            self.label_IP.setText(ip)
            
            ### 关机倒计时
            if self.shutdownflg == 1:
                if self.shutdowntimeleft > 0:
                    print("self.shutdowntimeleft ",self.shutdowntimeleft)
                    self.shutdowntimeleft-=1
                    times = self.shutdowntimeleft/5
                    tmp = "" + str(int(times))+"秒后关机！"
                    #self.bt_shutdown_2.setText(tmp)
                    
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
                self.diameter = webdim

            #速度为零，设置方向
            webdir    = getwebsetdir()
            if self.locospeed < 2:
                if webdir == 0:
                    self.dir == webdir
            else:
                webdir = 0
                
            #速度和转速设置，互斥只能设置一个，且需要控制调整速率
            if webspeed != 0:
                lstrotate = calclocorotate(webspeed,self.diameter)
                print("lstrotate",lstrotate)
                webrotate   = 0
            
            if webrotate != 0:
                lstrotate = webrotate
                webspeed =0

            #缓慢加减速度
            if lstrotate > 0 and lstrotate <=500:
                if  lstrotate > self.setrotatespeed:
                    #速度+
                    self.rotatesspeedadd()
                    print("lstrotate add",lstrotate)
                    print("lstrotate add",self.setrotatespeed)
                    time.sleep(0.1)
                elif lstrotate < self.setrotatespeed:
                    #速度-
                    self.rotatesspeedsub()
                    print("lstrotate sub",lstrotate)
                    time.sleep(0.1)
                else:
                    lstrotate = 0
            else:
                lstrotate = 0
            

            
            ### 速度0时，可以选择 参数调整 功能
            if self.setrotatespeed == 0:

                if getKeySta(KEY_SET):
                    #功能设置按键按下，进行相应的功能选择。
                    if daemontime != setkeydowntime +1:       # 不是长按状态（连续进入则认为是长按）
                        #setkeytimes     += 1
                        setkeystilltime  = 0                  # 按键长按计时开始
                        
                        self.setobj += 1                      # 设置对象往下偏移
                        self.setobj %= self.objnum            # 范围限制                        
                    else:
                        setkeystilltime += 1                  # 按键保持按下状态
                        print("setkeystilltime",setkeystilltime)
                        if setkeystilltime > 25:              # 5s #在速度为0情况下，长按设置按键5s，设备关机。
                            self.shutdownflg = 1
                            
                    setkeydowntime = daemontime               # 记录设置按键按下时间（判断是长时间、短时间按键）。
                    
                keysub = getKeySta(KEY_SUB) or getwebspeedsubflg()
                keyadd = getKeySta(KEY_ADD) or getwebspeedaddflg()
                
                if  keysub or keyadd:                #有按键按下
                    
                    #有其他按键，设置按键清零
                    setkeytimes = 0
                    
                    if self.shutdownflg == 1:            #如果是在关机倒计时，则只取消关机过程
                        self.shutdownflg = 0             #关机过程中，有其他按键按下，取消关机           
                        self.shutdowntimeleft = 50       #重新赋值
                    else:
                        if keyadd:                       #按键+
                            if   self.setobj == 0:       #转速
                                self.rotatesspeedadd()               
                            elif self.setobj == 1:       #轮径
                                self.diameterAdd()
                            elif self.setobj == 2:       #速度    
                                self.locospeedadd()
                            else:                        #改变方向
                                changedirection()                        
                        else:                            #按键-
                            if   self.setobj == 0:       #转速
                                self.rotatesspeedsub()               
                            elif self.setobj == 1:       #轮径
                                self.diameterSub()
                            elif self.setobj == 2:       #速度    
                                self.locospeedsub()
                            else:                        #改变方向
                                changedirection()
                        
            ###  速度不为零        
            if self.setrotatespeed != 0:
                
                # 在速度不为零时，双击设置按键，紧急停机
                if getKeySta(KEY_SET):
                    #功能设置按键按下，进行相应的功能选择。
                    if daemontime != setkeydowntime +1:       # 不是长按状态（连续进入则认为是长按）
                        setkeytimes += 1
                        
                    setkeydowntime = daemontime               # 记录时间
                    
                    if setkeytimes > 1:                       # 连续按两次以上，表示急停
                        speedstop()                           # 速度停止
                        self.setrotatespeed = 0
                        self.locospeed = 0
                        
                if getKeySta(KEY_SET) == 0:                   # 按键松开
                    if daemontime > setkeydowntime + 10:      # 松开间隔时间大于2秒
                        setkeytimes = 0
                        
                # 在速度不为零时，只能调整转速和速度值。默认设置为转速
                if  self.setobj == 1 or self.setobj == 3:     # 轮径设置 或 方向设置
                    self.setobj =  0

                # 按加、减按键，进行速度的增减
                if  getKeySta(KEY_ADD ) or getwebspeedaddflg():
                    if self.setobj == 0:
                        self.rotatesspeedadd()    
                    elif self.setobj == 2:        #速度
                        self.locospeedadd()
                    #else:
                elif   getKeySta(KEY_SUB) or getwebspeedsubflg():
                    if self.setobj == 0:
                        self.rotatesspeedsub()               
                    elif self.setobj == 2:       #速度
                        self.locospeedsub()
                    #else:                    
                                              
            
            """
            if getKeySta(KEY_SUB) |  getKeySta(KEY_ADD):     #有按键按下
                if getKeySta(KEY_ADD) & getKeySta(KEY_SUB) : #同时有按键按下，在低速时，切换方向
                    doublekeydowntims+=1
                    if getpwnvalue() < 520:
                        if doublekeydowntims > 5:
                            if dirchangetimes == 0:
                                changedirection()
                                dirchangetimes = 1
                elif getKeySta(KEY_ADD):
                    dirchangetimes    = 0
                    doublekeydowntims = 0
                    speedadd()
                else:
                    speedsub()
                    dirchangetimes    = 0
                    doublekeydowntims = 0                    
            """
    #@pyqtSlot()
    #def on_bt_speedadd_clicked(self):
        """
        Slot documentation goes here.
        """
        #speedadd()                                          #速度加
       # TODO: not implemented yet
        #  raise NotImplementedError
    
    #@pyqtSlot()
    #def on_bt_speedsub_clicked(self):
        """
        Slot documentation goes here.
        """
        #speedsub()                                          #速度减
        # TODO: not implemented yet
        # raise NotImplementedError
        
    #@pyqtSlot()
    #def on_bt_shutdown_clicked(self):           #关机查询
        """
        Slot documentation goes here.
        """
        
        #speedstop()
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #if reply == QMessageBox.Yes:
        #    os.system('shutdown -s -t 10' )      #关机
        #else:
        #    print("取消关机")
        # TODO: not implemented yet
        #raise NotImplementedError
    #@pyqtSlot()
    #def on_bt_shutdown_2_clicked(self):           #关机查询
        """
        Slot documentation goes here.
        """
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #reply = MyMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        '''
        if self.shutdownflg == 1:
            self.bt_shutdown_2.setText("关机")
            self.shutdowntimeleft  = 50
            self.shutdownflg = 0
        else :
            self.shutdownflg = 1
        '''
        #if reply == QMessageBox.Yes:
        #    shutdown()
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #if reply == QMessageBox.Yes:
        #    os.system('shutdown -s -t 10' )      #关机
        #else:
        #    print("取消关机")
        # TODO: not implemented yet
        #raise NotImplementedError

    #@pyqtSlot()
    #def on_bt_dir_clicked(self):           #关机查询
        """
        Slot documentation goes here.
        """
        #改变方向
        #changedirection()
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #if reply == QMessageBox.Yes:
        #    os.system('shutdown -s -t 10' )      #关机
        #else:
        #    print("取消关机")
        # TODO: not implemented yet
        #raise NotImplementedError
#按键及脉冲检测电路
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
    time.sleep(0.5)
    initGPIO()              #脉冲检测及按键端口初始化

    app = QtWidgets.QApplication(sys.argv)
    ui = ui_main()
    sys.exit(app.exec_())
	
	

