#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>
  
int g_frq   = 0;
int g_count = 0;
int g_times = 0;
#define     ONE_SECOND   (1000000)

int g_pin_counter;
//边沿中断函数，计数器加1
void frqcounter(void)
{
    //if(digitalRead (g_pin_counter) == LOW)
        g_count++;
}

//
int initFrq(int pin)
{
    wiringPiSetupGpio();            //初始化 BCM GPIO 
    g_pin_counter = pin;
    pinMode(pin,INPUT);
    pullUpDnControl(pin,PUD_DOWN);
    wiringPiISR (pin, INT_EDGE_FALLING,  frqcounter);
    return 1;
}

//取频率值
int getFrq(void)
{
    return g_frq;
}

//取频率值
int getTimes(void)
{
    return g_times;
}



//线程函数，每秒执行1次
int threadCounter(void)
{
    long tim;
    /* do something */
    tim = micros();
    while(1)
    {
        //if(micros() - tim >= ONE_SECOND)        //1秒
        {   
            delayMicroseconds(ONE_SECOND);

            g_frq   = g_count;                    //取频率值
            g_count = 0;
            //tim     = micros();        
            //g_times++;
        }
    }
    return 0;
}


