
# -*- coding: utf-8 -*-

"""
Module implementing ui_main.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import   QMessageBox
from PyQt5      import QtCore, QtGui, QtWidgets

from Ui_hallsensortest import Ui_MainWindow
from speedCtrol import *
import threading
from    zkzt2_com2  import *
from    keyer       import *
import  os,sys,time


KEY_SUB    = 13                                                      #速度-   （引脚号）
KEY_ADD    = 5                                                       #速度+   （引脚号）


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
        #self.show()                   #全屏显示
        
        self.thread1 = threading.Thread(target = self.showSpeed)        #显示速度值
        self.thread1.start()
        self.thread2 = threading.Thread(target = self.daemon)             #守护线程
        self.thread2.start()

    def showSpeed(self):                                #显示速度值
        while True:
            time.sleep(1.5)
            dim2 = 1250                                #机车轮径1250mm
            dim1 = 1050                                #机车轮径1050mm
            try:
                rotate       = getSpeed()                      #取速度信号，在文件zkzt2_com2中
                speed1050    = (int)((rotate*3.1415926 * dim1 * 60)/(1000*1000) )
                speed1250    = (int)((rotate*3.1415926 * dim2 * 60)/(1000*1000) )
                self.ln_speed.display(rotate)
                self.ln_speed1050.display(speed1050)
                self.ln_speed1250.display(speed1250)
                
            except Exception as e:
                print("速度读取错误", e)

    def  daemon(self):
        while True:
            time.sleep(0.1)
            if getKeySta(KEY_SUB) |  getKeySta(KEY_ADD):   #有按键按下
                if getKeySta(KEY_ADD):
                    speedadd()
                else:
                    speedsub()

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


#按键及脉冲检测电路
def initGPIO():
    
    initKey(KEY_SUB)                                                    #初始化速度-按键
    initKey(KEY_ADD)                                                    #初始化速度+按键
    KeyThread = threading.Thread(target = daemonKey)   #创建多线程，启动接收任务
    KeyThread.start()
    
    FRQ_IN     = 21                                                      #频率采集    
    Frqer.initFrq(FRQ_IN)                                               #频率检测电路引脚

    tfrq    = threading.Thread(target = Frqer.threadCounter)
    tfrq.start()                                                            #启动多线程

    #tsec    = threading.Thread(target = taskSecond)
    #tsec.start()
    

if __name__ == "__main__":
    initGPIO()              #脉冲检测及按键端口初始化

    app = QtWidgets.QApplication(sys.argv)
    ui = ui_main()
    sys.exit(app.exec_())

