
import configparser
import os

class ReadConfig:
    """定义一个读取配置文件的类"""

    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            #root_dir = os.path.dirname(os.path.abspath('.'))
            root_dir = os.getcwd()
            configpath = os.path.join(root_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)
        self.path = configpath
        #print(self.cf.sections())

    def File(self, param):
        root_dir = os.getcwd()
        value = self.cf.get("File", param)
        value = os.path.join(root_dir, value)
        return value
    def Speed(self, param):
        value = self.cf.get("Speed", param)
        return value

    def Debug(self, param):
        value = self.cf.get("Debug", param)
        return value

    def WriteSpeed(self,param,value):
        self.cf.set("Speed",param,value)
        with open(self.path,'w') as f:
            self.cf.write(f)
        
confile = ReadConfig()          #读取配置文件

def getDebugInfo():
    global confile
        
    return 1

if __name__ == '__main__':
    test = ReadConfig()
    #print(test.sections)
    t = test.File("path")
    print(t)
    t = test.Speed("diameter")
    print(t)

    t = test.Debug("Debug")
    print(t)

    test.WriteSpeed("diameter","1000")


