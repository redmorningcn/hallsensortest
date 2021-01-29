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

def startWebProtocol():
    t = threading.Timer(0, webprotocol)
    t.start()

def webprotocol():
    times = 0
    while True:
        time.sleep(0.01)
        
        times+=1
        if times > 100:     #1s
            times = 0
            #message = ("%s,%s,%s")%(HEADER,str(getval()),ENDER)
            message = ("%s,%s,%s")%(HEADER,str(getSpeed()),ENDER)
            #print(message)
            server_send(message)  #服务器主动发送消息
        
        txt =  server_recv()
        if txt:
            prorecv_list = txt.split(',')
            print(prorecv_list)
            i = 0
            while i < 4:          #列表补齐
                prorecv_list.append('none')
                i += 1
            
            #接收到数据
            if HEADER == prorecv_list[0]:
                #速度加减
                if prorecv_list[1] == SPEED_CTL[0]:
                    speedadd()
                    print('speedadd')
                elif prorecv_list[1] == SPEED_CTL[1]:
                    speedsub()
                    print('speedsub')
                else:
                    print('speedother')
                    
                #速度加减
                if prorecv_list[2] == SPEED_DIR[0]:
                    #setdir(1)
                    print('setdir(1)')
                elif prorecv_list[2] == SPEED_DIR[1]:
                    #setdir(0)
                    print('setdir(0)')
                else:
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
        
import   time      
if __name__=='__main__':
    startServer()           #启动服务
    startWebProtocol()      #启动通讯协议
    
