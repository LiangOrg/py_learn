#!/usr/bin/env python
#encoding:utf-8
import time,functools
def performance(unit):       #形参,定义装饰器携带一个参数
    def perf_decorator(f):   #再嵌套一个函数，携带参数f,形参f是一个函数
        @functools.wraps(f)  #装饰器调用functools模块的wraps方法来打印函数f的函数名
        def wrapper(*args,**kw):  #定义功能函数，并且可以携参数
            t1 = time.time()      #打印函数执行前的时间
            r = f(*args,**kw)     #执行函数并赋值给r
            t2 = time.time()      #打印函数执行后的时间
            t=(t2 - t1) * 1000 if unit == 'ms' else (t2-t1)   #计算函数执行花费时间, 装饰器携带的参数如果是'ms',就 x1000,否则就是计算的结果本身。
            print 'call %s() in %f %s' %(f.__name__,t,unit)   #打印函数名，函数执行花费时间，装饰器携带的参数('ms' or 's')
            return r              #返回函数r
        return wrapper            #返回函数wrapper
    return perf_decorator         #返回函数perf_decorator
    
@performance('ms')  #装饰器携带参数 'ms' or 's' (毫秒或者秒)
def factorial(n):   #定义函数factorial,计算1到10相乘的积.
    return reduce(lambda x,y:x*y,range(1,n+1))  #reduce 用lambda匿名函数依次作用序列[1,..10],并返回最后的值
t = factorial(11)  #赋值给t
print t            #打印t函数
