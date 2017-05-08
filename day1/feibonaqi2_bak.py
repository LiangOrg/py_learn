#!/usr/bin/env python2.7
#coding:utf8

import sys

def febs(num):
    num_list=[0,1]
    a,b=1,2
    Sum=1
    for i in range(num-2):
        num_list.append(a)
        Sum+=a
        a,b=b,a+b
    print num_list
    print "\033[32m第\033[1;5;32m%d\033[0;32m天,会有\033[1;5;32m%d\033[0;32m对兔子.\033[0m"  % (num,a)
    print "\033[33m第\033[1;5;31m%d\033[0;33m天后,共有\033[1;5;31m%d\033[0;33m对兔子.\033[0m"  % (num,Sum)

if __name__ == "__main__":
    try:
        febs(int(sys.argv[1]))
    except:
        print "\033[32m Please input a big more than 1 num!\033[0m"
