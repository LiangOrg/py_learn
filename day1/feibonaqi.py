#!/usr/bin/env python2.7
#coding:utf8

import sys

def feibonaqi(N):                          #形参N表示第n天
	result = []                     #前2天的兔子数列表
    	Sum = 1                            #前2天共有1对兔子

        for i in range(N-2):
        	sum = result[-2]+result[-1]  #第N天的兔子数
        	result.append(sum)      
        	Sum+=sum                     #计算兔子的总数
		
    	print result
    	print "\033[32m第\033[1;32m%d\033[0;32m天,会有\033[1;;32m%d\033[0;32m对兔子.\033[0m"  % (N,sum)
    	print "\033[33m第\033[1;31m%d\033[0;33m天后,共有\033[1;;31m%d\033[0;33m对兔子.\033[0m"  % (N,Sum)

if __name__=='__main__':
	try:
		feibonaqi(int(sys.argv[1]))    #实参sys.argv[1] 传入一个大于2的整数
	except :
		print "请输入一个大于2的整数."
