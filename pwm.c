#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>

#define	PWM_MAX_VAL	(1024-1)
  
int PWM_pin = 0;

//初始化PWM引脚
int initPWM(int pin)
{
    PWM_pin = pin;				//PWM引脚号					
	wiringPiSetupGpio();            	//初始化 BCM GPIO 
    pinMode(pin,PWM_OUTPUT);
    //pwmSetMode (PWM_MODE_BAL);	
    pwmSetMode (PWM_MODE_MS);			//PWM_MODE_MS（固定频率）     0  PWM_MODE_BAL 1 // 标记和空格;PWM_MODE_BAL    1   // 平衡   默认是这个模式	
    //pwmSetClock(3048);			//wiringpi在初始化gpio时默认采用32倍分频 		 
    //pwmSetClock(38400);		        //wiringpi在初始化gpio时默认采用32倍分频 
    pwmSetClock(8);				//wiringpi在初始化gpio时默认采用32倍分频,电机推荐PWM频率为15～25K，设置4,频率为13.2k
    pwmSetRange(1024);
    return 1;
}

//设置PWN的时钟分频系数，值越大，产生波形频率越小（频率越大，越平稳;越小力越大）
int SetPWMClock(int val)
{
    pwmSetClock(val);
}

//设置PWM值
int SetPWM(int val)
{
    if (val > PWM_MAX_VAL )
		val = PWM_MAX_VAL;
	else if(val < 0)
		val = 0;
	
	pwmWrite(PWM_pin,val);
	return val;
}



