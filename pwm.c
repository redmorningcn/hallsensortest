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

//��ʼ��PWM����
int initPWM(int pin)
{
    PWM_pin = pin;				//PWM���ź�					
	wiringPiSetupGpio();            	//��ʼ�� BCM GPIO 
    pinMode(pin,PWM_OUTPUT);
    //pwmSetMode (PWM_MODE_BAL);	
    pwmSetMode (PWM_MODE_MS);			//PWM_MODE_MS���̶�Ƶ�ʣ�     0  PWM_MODE_BAL 1 // ��ǺͿո�;PWM_MODE_BAL    1   // ƽ��   Ĭ�������ģʽ	
    //pwmSetClock(3048);			//wiringpi�ڳ�ʼ��gpioʱĬ�ϲ���32����Ƶ 		 
    //pwmSetClock(38400);		        //wiringpi�ڳ�ʼ��gpioʱĬ�ϲ���32����Ƶ 
    pwmSetClock(8);				//wiringpi�ڳ�ʼ��gpioʱĬ�ϲ���32����Ƶ,����Ƽ�PWMƵ��Ϊ15��25K������4,Ƶ��Ϊ13.2k
    pwmSetRange(1024);
    return 1;
}

//����PWN��ʱ�ӷ�Ƶϵ����ֵԽ�󣬲�������Ƶ��ԽС��Ƶ��Խ��Խƽ��;ԽС��Խ��
int SetPWMClock(int val)
{
    pwmSetClock(val);
}

//����PWMֵ
int SetPWM(int val)
{
    if (val > PWM_MAX_VAL )
		val = PWM_MAX_VAL;
	else if(val < 0)
		val = 0;
	
	pwmWrite(PWM_pin,val);
	return val;
}



