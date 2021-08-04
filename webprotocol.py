'''
websocket，通讯协议
redmorningcn 2020.10.19
'''
HEADER = '#'
ENDER = '!'
SPEED_CTL = ['up','down','none']
SPEED_DIR = ['right','left','none']
POWER_CTL = ['stop','shutdown','none']

from    websocketserver4   import *
from    SetPWM             import *
from    GetMotorSpeed      import *
from    keyer              import *
from    hallsensortest     import *

def startWebProtocol():
    t = threading.Thread(target = webprotocol)
    t.start()

def webSendMessage(text):
    message = ("%s,%s,%s")%(HEADER,text,ENDER)
    #print(message)
    server_send(message)  #服务器主动发送消息


#远程设置速度
websetspeed  = -1
#远程设置转速
websetrotate = -1
#远程设置方向
websetdir    = -1
#远程设置轮径
websetdim    = 0
    
webspeedaddflg = 0
webspeedsubflg = 0

def getwebspeedaddflg():
    global webspeedaddflg
    key = webspeedaddflg
    webspeedaddflg = 0
    return key

def getwebspeedsubflg():
    global webspeedsubflg
    key = webspeedsubflg
    webspeedsubflg = 0
    return key

def getwebsetspeed():
    global websetspeed
    key = websetspeed
    websetspeed = -1
    return key

def getwebsetrotate():
    global websetrotate
    key = websetrotate
    websetrotate = -1
    return key

def getwebsetdim():
    global websetdim
    key = websetdim
    websetdim = 0
    return key

def getwebsetdir():
    global websetdir
    key = websetdir
    websetdir = -1
    return key


def webprotocol():
    global webspeedaddflg
    global webspeedsubflg    
    global websetspeed
    global websetrotate
    global websetdir
    global websetdim
    
    #times = 0
    while True:
    #if True:
        time.sleep(0.01)
        '''
        times+=1
        if times > 100:     #1s
            times = 0
            #message = ("%s,%s,%s")%(HEADER,str(getval()),ENDER)
            message = ("%s,%s,%s")%(HEADER,str(getdisplaylocospeed()),ENDER)
            #print(message)
            print(getdisplaylocospeed())
            server_send(message)  #服务器主动发送消息
        '''
        txt =  server_recv()
        if txt:
            prorecv_list = txt.split(',')
            print(prorecv_list)
            i = 0
            while i < 9:          #列表补齐
                prorecv_list.append('none')
                i += 1
            
            #接收到数据
            if HEADER == prorecv_list[0]:
                #速度加减
                if prorecv_list[1] == SPEED_CTL[0]:
                    #speedadd()
                    webspeedaddflg = 1
                    webspeedsubflg = 0
                elif prorecv_list[1] == SPEED_CTL[1]:
                    webspeedaddflg = 0
                    webspeedsubflg = 1
                    print('speedsub')
                else:
                    webspeedaddflg = 0
                    webspeedsubflg = 0                    
                    print('speedother')
                    
                #速度加减
                if prorecv_list[2] == SPEED_DIR[0]:
                    #setdir(1)
                    websetdir = 0
                    print('setdir(1)')
                elif prorecv_list[2] == SPEED_DIR[1]:
                    #setdir(0)
                    websetdir = 1
                    print('setdir(0)')
                else:
                    websetdir = -1
                    print('setdir')
                    
                #关机
                if prorecv_list[3] == POWER_CTL[0]:
                    #shutdown()
                    print('stop(0)')
                elif prorecv_list[3] == POWER_CTL[1]:
                    #setdir(0)
                    print('shutdown(1)')                    
                else:
                    print('shutdown(0)')
                    
                print('速度，转速，轮径',prorecv_list[4],prorecv_list[5],prorecv_list[6])
                #速度
                if prorecv_list[4] != 'none' and prorecv_list[4].isdigit():
                    
                    websetspeed = int(prorecv_list[4])
                else:
                    websetspeed = -1
                #转速
                if prorecv_list[5] != 'none'and prorecv_list[5].isdigit():
                    websetrotate = int(prorecv_list[5])
                else:
                    websetrotate = -1
                #轮径
                if prorecv_list[6] != 'none' and prorecv_list[6].isdigit():
                    websetdim = int(prorecv_list[6])
                else:
                    websetdim = 0
        #else:
            #webspeedaddflg = 0
            #webspeedsubflg = 0   
        
import   time      
if __name__=='__main__':
    startServer()           #启动服务
    startWebProtocol()      #启动通讯协议
    


