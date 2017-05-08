#!/usr/bin/env python
def func1(lst):
    def func2():
        def f(x,y):
            return x * y
        return reduce(f,lst)
    return func2
t=func1(range(1,5))
print t()
