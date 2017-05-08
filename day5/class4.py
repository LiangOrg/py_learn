#!/usr/bin/env python
#encoding:utf-8
class Person(object):
    __count = 0  #私有属性，外部没法获取.
    def __init__(self, name):
        Person.__count = Person.__count + 1
        self.name = name
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print Person.__count #没法获取Person 的私有属性 
except AttributeError:
    print 'attributeerror'
