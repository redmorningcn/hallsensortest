'''
启动websocket，发送和接收数据
redmorningcn 2020.10.19
'''
from   websocket_server import WebsocketServer
import threading
import json
from   datetime import datetime
import threading


def startServer():
    #t = threading.Timer(60, Server.run)
    t = threading.Thread(target = Server.run)
    t.start()
    
def server_send(text):
    if Server.serverflg == 2:
        Server.send_message(text)
        
def server_recv():
    if Server.messagelen > 0:
        #print(Server.messagelen)
        Server.messagelen = 0
        return Server.messagetxt
    return 0

class Server:
    serverflg  = 1
    messagetxt = ''
    messagelen = 0
    
    @classmethod
    def run(cls):
        PORT = 1234
        server = WebsocketServer(PORT, host='0.0.0.0')
        cls.myserver = server
        
        server.set_fn_new_client(cls.new_client)
        server.set_fn_client_left(cls.client_left)
        server.set_fn_message_received(cls.message_received)
        print("Web socket server has started at %s." % datetime.now())
        #showTimer()
        server.run_forever()
    
    @classmethod
    def getEvent(cls, data):
        try:
            jsonDic = json.loads(data)
            dic = dict(jsonDic)
            event = dic["event"]
        except Exception as error:
            print("Get event error:%s" % error)
            return None, {}
        return event, dic

    @classmethod
    def new_client(cls, client, server):
        print("A new client connected and was given id %d at %s." % (client['id'], datetime.now()))
        server.send_message_to_all("Hey all, a new client has joined us at %s." % datetime.now())
        Server.serverflg = 2    #连接正常
    @classmethod
    def send_message(cls,text):
        #print("A new client connected and was given id %d at %s." % (client['id'], datetime.now()))
        cls.myserver.send_message_to_all(text)
        
    @classmethod
    def client_left(cls, client, server):
        Server.serverflg   = 1  #连接断开
        print("Client(%d) disconnected at %s." % (client['id'], datetime.now()))

    @classmethod
    def message_received(cls, client, server, message):
        event, dic = cls.getEvent(message)
        #print(event, dic)
        #if event == 1:
        #    print(dic["tree"])
            
        Server.messagetxt = message
        Server.messagelen = len(message)
        #print(Server.messagelen,Server.messagetxt)
        #print("Client(%d) said: %s at %s" % (client['id'], message, datetime.now()))
      
import   time      
if __name__=='__main__':
    startServer()      #启动服务
    
    while True:
        time.sleep(1)

        txt =  server_recv()
        if txt:
            print(txt)
           
            
