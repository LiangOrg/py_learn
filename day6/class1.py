#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      '''构造函数'''
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
lw=Employee('lw',13000)
lx=Employee('lx',16000)
lx.displayEmployee()
lw.displayEmployee()
lw.displayCount()
print "实例lw的Doc为: %s" % str(lx.__doc__)
print "实例lw的init初始化Doc为: %s" % str(lx.__init__.__doc__)
print lx.__module__
