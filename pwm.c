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

//PWM����Ƶ�� Fw= 206*256*1024 = 54001664
//pwmƵ�ʼ��� f = Fw /��rang * clock��
#define PWM_WORK_FRQ  (54001664)
int SetFrq(unsigned int val)
{
    unsigned int range,divclock;
    unsigned int tmp,i;
    
    //Ƶ�ʷ�Χ0-1000000��
    if(val < 1 )
      return 0;
    if(val >1000000)
      val = 1000000;
    
    //printf("val:%d\r\n",val);
    tmp = (unsigned int)(PWM_WORK_FRQ / (val * 1000));
    //printf("tmp1:%d,%f\r\n",tmp,tmp);
    
    divclock = (0x0FFF & tmp) + 1;           	 //�����Ƶϵ��
    //printf("divclock:%d\r\n",divclock);
    
    tmp = 0x0100;
    for(i = 0;i < 8;i++){
	if( divclock & tmp){			//2��������
	    divclock &= tmp;
	    break;
	}
	tmp = tmp>>1;
	//printf("tmp:%x,divclock %x,divclock & tmp %d,%x\r\n",tmp,divclock,(divclock & tmp),(divclock & tmp));
    }
    //printf("divclock:%d\r\n",divclock);
    if (divclock < 2)
        divclock = 2;
    
    range    = (unsigned int)(PWM_WORK_FRQ / (val * divclock )); //���㷶Χ
    
    if(range < 2)	//�ݴ���
	range = 2;
    
    pwmSetClock(divclock);			//���÷�Ƶϵ��
    pwmSetRange(range);				//���÷�Χ
    //printf("pwmset:divclock %d,range %d\r\n",divclock,range);
    pwmWrite(PWM_pin,range/2);
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



