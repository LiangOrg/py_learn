#!/usr/bin/env python
class Person(object):
    count = 0
    def __init__(self, name):
        Person.count = Person.count + 1
        self.name = name
p1 = Person('Bob')
print Person.count
# => 1
p2 = Person('Alice')
print Person.count
# => 2
p3 = Person('Tim')
print Person.count
# => 3
