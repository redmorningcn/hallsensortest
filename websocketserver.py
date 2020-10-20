# coding:utf8
# __author:  redmorningcn
# date:      2020/10/19 
# /usr/bin/env python
import socket,base64,hashlib


def get_headers(data):
    '''将请求头转换为字典'''
    header_dict = {}
    data = str(data,encoding="utf-8")

    header,body = data.split("\r\n\r\n",1)
    header_list = header.split("\r\n")
    for i in range(0,len(header_list)):
        if i == 0:
            if len(header_list[0].split(" ")) == 3:
                header_dict['method'],header_dict['url'],header_dict['protocol'] = header_list[0].split(" ")
        else:
            k,v=header_list[i].split(":",1)
            header_dict[k]=v.strip()
    return header_dict

def get_data(info):
    payload_len = info[1] & 127
    if payload_len == 126:
        extend_payload_len = info[2:4]
        mask = info[4:8]
        decoded = info[8:]
    elif payload_len == 127:
        extend_payload_len = info[2:10]
        mask = info[10:14]
        decoded = info[14:]
    else:
        extend_payload_len = None
        mask = info[2:6]
        decoded = info[6:]

    bytes_list = bytearray()    #这里我们使用字节将数据全部收集，再去字符串编码，这样不会导致中文乱码
    for i in range(len(decoded)):
        chunk = decoded[i] ^ mask[i % 4]    #解码方式
        bytes_list.append(chunk)
    body = str(bytes_list, encoding='utf-8')
    return body


class websocketserver:
    def __init__(self,ip="127.0.0.1",port = 8080):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind(("127.0.0.1",8080))
        sock.listen(5)    
        #等待用户连接
        self.conn,self.addr = sock.accept()
        #获取握手消息，magic string ,sha1加密
        #发送给客户端
        #握手消息
        data = self.conn.recv(8096)
        headers = get_headers(data)
        # 对请求头中的sec-websocket-key进行加密
        response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
              "Upgrade:websocket\r\n" \
              "Connection: Upgrade\r\n" \
              "Sec-WebSocket-Accept: %s\r\n" \
              "WebSocket-Location: ws://%s%s\r\n\r\n"

        magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

        value = headers['Sec-WebSocket-Key'] + magic_string
        ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
        response_str = response_tpl % (ac.decode('utf-8'), headers['Host'], headers['url'])
        # 响应【握手】信息
        self.conn.send(bytes(response_str, encoding='utf-8'))
        
        

    def send_msg(self,msg_bytes):
        """
        WebSocket服务端向客户端发送消息
        :param conn: 客户端连接到服务器端的socket对象,即： conn,address = socket.accept()
        :param msg_bytes: 向客户端发送的字节
        :return:
        """
        import struct

        token = b"\x81" #接收的第一字节，一般都是x81不变
        length = len(msg_bytes)
        if length < 126:
            token += struct.pack("B", length)
        elif length <= 0xFFFF:
            token += struct.pack("!BH", 126, length)
        else:
            token += struct.pack("!BQ", 127, length)

        msg = token + msg_bytes
        self.conn.send(msg)
        return True
    
    
    def demoRev(self):
        #可以进行通信
        self.recv_buf       = "test" 
        self.recv_len       = 0                                 #接收数据长度

        while True:
            data = self.conn.recv(8096)
            data = get_data(data)
            
            self.recv_buf = get_data(data)                      #解析数据
            self.recv_len = strlen(self.recv_buf)
            print(data)
            #send_msg(conn,bytes(data+"geah",encoding="utf-8"))

import threading
import      time

if __name__=='__main__':
    wbserver = websocketserver()
    
    t1=threading.Thread(target=wbserver.demoRev)
    t1.start()
    while True:
        time.sleep(1)