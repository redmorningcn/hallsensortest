'''
查询本机IP地址
redmorningcn 2020.10.19
'''

import socket
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
  

if __name__ == '__main__':
    #第一种方法
    print(get_host_ip())
     
    #第二种方法
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    print(hostname)
    ip = socket.gethostbyname(hostname)
    print(ip)