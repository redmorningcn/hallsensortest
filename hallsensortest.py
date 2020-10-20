
# -*- coding: utf-8 -*-

"""
Module implementing ui_main.
"""

from PyQt5.QtCore      import pyqtSlot
from PyQt5.QtWidgets   import QMainWindow
from PyQt5.QtWidgets   import   QMessageBox
from PyQt5             import QtCore, QtGui, QtWidgets
from Ui_hallsensortest import Ui_MainWindow
#from speedCtrol import *
import  threading
from    SetPWM             import *
from    GetMotorSpeed      import *
from    keyer              import *
from    shutdown           import *

import  os,sys,time

KEY_SUB    = 7                                                      #速度-   （引脚号）
KEY_ADD    = 3                                                      #速度+   （引脚号）



class ui_main(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ui_main, self).__init__(parent)
        self.setupUi(self)
        self.showFullScreen()                   #全屏显示
        #self.show()                            #全屏显示
        
        self.thread1 = threading.Thread(target = self.showSpeed)        #显示速度值
        self.thread1.start()
        self.thread2 = threading.Thread(target = self.daemon)                                       #守护线程
        self.thread2.start()
        #关机daoji时
        self.shutdownflg = 0
        self.shutdowntimeleft  = 50
    def showSpeed(self):                                #显示速度值
        shutdowntimes = 0
        
        while True:
            time.sleep(1.5)
            dim2 = 1250                                #机车轮径1250mm
            dim1 = 1050                                #机车轮径1050mm
            try:
                rotate       = getSpeed()                      #取速度信号，在文件zkzt2_com2中
                speed1050    = (int)((rotate*3.1415926 * dim1 * 60)/(1000*1000) )
                speed1250    = (int)((rotate*3.1415926 * dim2 * 60)/(1000*1000) )
                self.ln_speed.display(rotate)
                self.ln_speed_1050.display(speed1050)
                self.ln_speed_1250.display(speed1250)
                
                #速度为0，且减速减按下10s，则设备准备关机
                if rotate == 0:
                    if getKeySta(KEY_SUB):
                        shutdowntimes +=1
                        if shutdowntimes > 5:
                            self.shutdownflg = 1
                    elif getKeySta(KEY_ADD):   #按其他，取消关机
                        if self.shutdownflg == 1:
                            self.bt_shutdown_2.setText("关机")
                            self.shutdowntimeleft  = 50
                            self.shutdownflg = 0
                            shutdowntimes = 0
                    else:
                        shutdowntimes = 0
                
            except Exception as e:
                print("速度读取错误", e)
    
    #两键同时按下次数
    doublekeydowntims = 0;
    #按下键后方向切换次数
    dirchangetimes    = 0

          
    def  daemon(self):
        while True:
            time.sleep(0.2)
            
            #关机倒计时
            if self.shutdownflg == 1:
                if self.shutdowntimeleft > 0:
                    self.shutdowntimeleft-=1
                    times = self.shutdowntimeleft/5
                    tmp = "" + str(int(times))+"s关机"
                    self.bt_shutdown_2.setText(tmp)
					
					self.bt_shutdown_2.setText(tmp)
                else:
                    shutdown()  #启动关机程序
            
            #分频值小于500,速度方向控件可用
            if getpwnvalue() < 450:
                self.bt_dir.setEnabled(True)
            else:
                self.bt_dir.setEnabled(False)
            
            #速度方向显示    
            if getChangeDircetion() == 0:
                self.bt_dir.setText("顺时针方向")
            else:
                self.bt_dir.setText("逆时针方向")
            
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

    @pyqtSlot()
    def on_bt_speedadd_clicked(self):
        """
        Slot documentation goes here.
        """
        speedadd()                                          #速度加
       # TODO: not implemented yet
        #  raise NotImplementedError
    
    @pyqtSlot()
    def on_bt_speedsub_clicked(self):
        """
        Slot documentation goes here.
        """
        speedsub()                                          #速度减
        # TODO: not implemented yet
        # raise NotImplementedError
        
    @pyqtSlot()
    def on_bt_shutdown_clicked(self):           #关机查询
        """
        Slot documentation goes here.
        """
        
        speedstop()
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #if reply == QMessageBox.Yes:
        #    os.system('shutdown -s -t 10' )      #关机
        #else:
        #    print("取消关机")
        # TODO: not implemented yet
        #raise NotImplementedError
    @pyqtSlot()
    def on_bt_shutdown_2_clicked(self):           #关机查询
        """
        Slot documentation goes here.
        """
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #reply = MyMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        
        if self.shutdownflg == 1:
            self.bt_shutdown_2.setText("关机")
            self.shutdowntimeleft  = 50
            self.shutdownflg = 0
        else :
            self.shutdownflg = 1
        #if reply == QMessageBox.Yes:
        #    shutdown()
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #if reply == QMessageBox.Yes:
        #    os.system('shutdown -s -t 10' )      #关机
        #else:
        #    print("取消关机")
        # TODO: not implemented yet
        #raise NotImplementedError

    @pyqtSlot()
    def on_bt_dir_clicked(self):           #关机查询
        """
        Slot documentation goes here.
        """
        #改变方向
        changedirection()
        #reply = QMessageBox.question(self,'询问','是否关机！', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #if reply == QMessageBox.Yes:
        #    os.system('shutdown -s -t 10' )      #关机
        #else:
        #    print("取消关机")
        # TODO: not implemented yet
        #raise NotImplementedError
#按键及脉冲检测电路
def initGPIO():
    
    initKey(KEY_SUB)                                                    #初始化速度-按键
    initKey(KEY_ADD)                                                    #初始化速度+按键
    KeyThread = threading.Thread(target = daemonKey)   #创建多线程，启动接收任务
    KeyThread.start()
    
    FRQ_IN     = 21                                                      #频率采集    
    Frqer.initFrq(FRQ_IN)                                               #频率检测电路引脚

    tfrq    = threading.Thread(target = Frqer.threadCounter)
    tfrq.start()
    
    PWM.initPWM(12)    
    PWM.SetPWMClock(4)    
    #启动多线程
    LowThread = threading.Thread(target = daemonLowSpeed)     #创建多线程，启动接收任务
    LowThread.start()   
    #tsec    = threading.Thread(target = taskSecond)
    #tsec.start()
    

if __name__ == "__main__":
    initGPIO()              #脉冲检测及按键端口初始化

    app = QtWidgets.QApplication(sys.argv)
    ui = ui_main()
    sys.exit(app.exec_())

