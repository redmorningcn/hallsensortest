'''
作者：redmorningcn   200915
描述：读取速度信号。电机采用BLDC4260无刷直流电机，自带速度信号输出。没转输出12个脉冲;适用减速比为4.5（72/16）
包：Zkzt2Data，(self,port,baund = 9600)，
方法：setSpeed(self,speed,frq = 1000,direction = STA_CW):设置速度，其中speed 为%0-%100,可调速度。
'''
import   ctypes
import   platform
from     ctypes  import  *  
import   time

#Checker= ctypes.cdll.LoadLibrary(".\\CrcCheck.dll")
#不同的操作系统，打印对应的信息
if platform.system() == "Linux":
    Frqer   = CDLL("./GPIO_counter.so")
else:
    Frqer   = CDLL(".\\GPIO_counter.dll")

import  threading

#脉冲常数
g_PLUSE = 12
#减速比
g_RATIO = 4.5
#返回速度值
l_rotate = 0
def  getSpeed():
    global l_rotate
    frq    = Frqer.getFrq()
    rotate = (int)((60 * frq) / (g_PLUSE * g_RATIO))
    #speed  = (int)((rotate + l_rotate)/2)      #前后数据取平均，去抖
    speed = rotate
    l_rotate = rotate
    return speed

def  taskSecond():
    while True:
        time.sleep(1)
        frq    = Frqer.getFrq()
        #rotate = (int)((60 * frq) / (11 * 10))
        rotate = (int)((60 * frq) / (g_PLUSE * g_RATIO))
        #speed  = (int)(3.6 * (frq * 3.14 * 1.05) / (11 * 10))
        speed  = (int)(3.6 * (frq * 3.14 * 1.05) / (g_PLUSE * g_RATIO))
        print("\r\n频率：%d,转速：%d,速度：%d"%(frq,rotate,speed))


if __name__=="__main__":

    pin     = 21
    
    Frqer.initFrq(pin)        #频率检测电路引脚

    tfrq    = threading.Thread(target = Frqer.threadCounter)
    tfrq.start()             #启动多线程

    tsec    = threading.Thread(target = taskSecond)
    tsec.start()
    
    while True:
        time.sleep(0.1)


    #motor.stop()
    #sendData = Zkzt2_ST(0xE0,0x01,0x00,0x00,0x32,0x03,0x20,0xF0)
    #bcc = Checker.GetBccCheck(ctypes.byref(sendData),ctypes.sizeof(sendData)-1)
    #print(bcc)


