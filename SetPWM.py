import ctypes


PWM = ctypes.cdll.LoadLibrary('./pwm.so')

#初始化PWM端口，
PWM.initPWM(18)

if __name__=="__main__":
    while True:
        print("占空比X/1024：")
        ratio = int(input())
        PWM.SetPWM(ratio)
