#!/usr/bin/env python
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print r
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
factorial(10)
