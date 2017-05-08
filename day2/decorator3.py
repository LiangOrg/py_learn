#!/usr/bin/env python

def log(f):
    def fn(*args,**kd):
        print 'call ' + f.__name__ + '()...'
        return f(*args,**kd)
    return fn
@log
def func1(a,b):
    return reduce(lambda x,y: x*y, range(1,a+1,b))
print func1(10,2)
