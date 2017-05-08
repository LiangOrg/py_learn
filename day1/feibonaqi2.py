#!/usr/bin/env python2.7
#coding:utf8

import sys

def febs():
    Num_list=[]
    a,b=1,2
    #L=1
    for i in range(65535):
        Num_list.append(a)
        a,b=b,a+b
        #L+=a
        if b<=4000000:
            Even_num=(filter(lambda x:x%2==0,Num_list))
            Sum_num=sum(Even_num)
	else:
		break
    print Num_list
    print Even_num
    return Sum_num
if __name__ == "__main__":
    print febs()
