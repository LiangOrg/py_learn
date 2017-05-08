#!/usr/bin/env python

import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args,**kw):
        print 'cal...'
        return f(*args,**kw)
    return wrapper

@log
def f2():
    pass
print f2.__name__
