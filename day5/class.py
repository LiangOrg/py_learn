#!/usr/bin/env python

class Person(object):
    pass
xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'

xiaohong = Person()
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2

xiaohong.grade = xiaohong.grade + 1

L1=[xiaoming,xiaohong]
print L1[1].name
