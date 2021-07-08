import os,sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

def shutdown():
    #os.system("shutdown -r -t 5 now")
    os.system("shutdown -t 5 now")
    sys.exit()
    
if __name__=="__main__":
    shutdown()