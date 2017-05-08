#!/usr/bin/env python2.7
#encoding:utf-8
class Person(object):
    count = 0
    @classmethod
    def how_many(self):
        return self.count
    def __init__(self,name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
