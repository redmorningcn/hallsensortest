#作者：redmorningcn  20.03.02
#打开配置文件，将配置信息读入到列表
#
#包：SwitchTable
#包初始化：配置文件路径，例如：r"F:\cvi\app\NC208\NC208measureconfig.csv"
#方法：getConfig(self,num)，根据传感器编号num，获取配置信息列表。

import  fileinput
from    calcspeed             import *

#配置文件路径
path = r"locospeedfile.csv"

conf_list= []
#读取配置信息
def readspeedInfoFromFile(path):
    print(path)
    linenum = 0
    for line in fileinput.input(path):
        linenum += 1
        if linenum == 1:                    #第1行不处理
            continue
        else:
            #print("line is:",line)
            str = line.split(',')           #分割line
            #print(str)
            dict = {}   
            dict['no']  = int(str[0])       #序号
            dict['period']   = int(str[1])  #周期
            dict['speed']   = int(str[2])   #速度值
            dict['group1flg']= str[3]       #组1速度有效标识
            dict['group2flg']= str[4]       #组2速度有效标识
            dict['sensor1dirflg']= str[5]   #传感器1方向标识
            dict['sensor1phasenum']= str[6] #传感器1相位差
            dict['sensor2dirflg']= str[5]   #传感器1方向标识
            dict['sensor2phasenum']= str[6] #传感器1相位差
    
            #print(dict)
            conf_list.append(dict)

    return linenum

class SpeedTable(object):
    def __init__(self,path = r"/home/pi/pycode/hallsensortest/locospeedfile.csv"):
        try:
            self.line = readspeedInfoFromFile(path)

            #print(conf_list)
        except Exception as e:
            print("---配置文件打开异常---:",e)

    def getmodspeed(self,num):              #模拟速度
        for conf in conf_list:
            #print(conf)
            if conf.get('no') == num:
                return conf.get('speed') 
    
        print("未找到对应的配置",num)
        return {}

    def getspeedline(self):                 #返回字典个数
        return self.line

if __name__ == "__main__":
    speedtalbe = SpeedTable(path)           #定义实列

    #print(speedtalbe)
    num = speedtalbe.getspeedline()
    
    i = 0
    while i  < num-1 and num >0:
        speed   = speedtalbe.getmodspeed(i)
        rorate  = calclocorotate(speed, 1050)
        rotaterate        = getrotaterate()           #同步轮齿数比
        pwmrate           = getpwmrate()              #步进电机分频系数
        rorate = rorate/100
        pwmfre = (rorate * rotaterate * pwmrate) / 60;
        print("speed ",speed,(int)(rorate),pwmfre)
        i+=1


