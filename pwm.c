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

//PWM工作频率 Fw= 206*256*1024 = 54001664
//pwm频率计算 f = Fw /（rang * clock）
#define PWM_WORK_FRQ  (54001664)
int SetFrq(unsigned int val)
{
    unsigned int range,divclock;
    unsigned int tmp,i;
    
    //频率范围0-1000000；
    if(val < 1 )
      return 0;
    if(val >1000000)
      val = 1000000;
    
    //printf("val:%d\r\n",val);
    tmp = (unsigned int)(PWM_WORK_FRQ / (val * 1000));
    //printf("tmp1:%d,%f\r\n",tmp,tmp);
    
    divclock = (0x0FFF & tmp) + 1;           	 //计算分频系数
    //printf("divclock:%d\r\n",divclock);
    
    tmp = 0x0100;
    for(i = 0;i < 8;i++){
	if( divclock & tmp){			//2的整数倍
	    divclock &= tmp;
	    break;
	}
	tmp = tmp>>1;
	//printf("tmp:%x,divclock %x,divclock & tmp %d,%x\r\n",tmp,divclock,(divclock & tmp),(divclock & tmp));
    }
    //printf("divclock:%d\r\n",divclock);
    if (divclock < 2)
        divclock = 2;
    
    range    = (unsigned int)(PWM_WORK_FRQ / (val * divclock )); //计算范围
    
    if(range < 2)	//容错处理
	range = 2;
    
    pwmSetClock(divclock);			//设置分频系数
    pwmSetRange(range);				//设置范围
    //printf("pwmset:divclock %d,range %d\r\n",divclock,range);
    pwmWrite(PWM_pin,range/2);
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



