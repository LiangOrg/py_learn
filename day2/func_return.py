#!/usr/bin/env python
def func1(list1):
    def func2():
        return reduce((lambda x,y:x*y),list1)
    return func2
t=func1([1,2,3,4])
print t()
