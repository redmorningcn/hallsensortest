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
    PWM_pin = pin;					//PWM���ź�					
	wiringPiSetupGpio();            //��ʼ�� BCM GPIO 
    pinMode(pin,PWM_OUTPUT);
    return 1;
}

//ȡƵ��ֵ
int SetPWM(int val)
{
    if (val > PWM_MAX_VAL )
		val = PWM_MAX_VAL;
	else if(val < 0)
		val = 0;
	
	pwmWrite(PWM_pin,val);
	return val;
}



