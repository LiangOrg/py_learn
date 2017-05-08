#!/usr/bin/env python
#encoding:utf-8
def triangle1():
    p = [1]
    a = 0
    while True:
        q = []
        i = 0
        while i <= a:
            if i == 0 or i == len(p):
                q.append(1)
            else:
                q.append(p[i-1] + p[i])
            i += 1
        p = q
        yield q
        a += 1

def triangle2():
    q = [1]
    while True:
        yield q
        i = 0
        while 0 <= i <= len(q) - 1:
            if i == 0:
                pass
            else:
                q[i] = p[i-1] + p[i]
            i += 1
        q.append(1)
        p = tuple(q) # or can be p = q[:]

def triangle3():
    q = [1]
    while True:
        yield q
        i = 1
        while 1 <= i <= len(q) - 1:
            q[i] = p[i-1] + p[i]
            i += 1
        q.append(1)
        p = q[:]

def triangle4():
    q = [1]
    while True:
        yield q
        for i in range(1, len(q)):
            q[i] = p[i-1] + p[i]
        q.append(1)
        p = q[:]

def triangle5():
    p = [1]
    while True:
        yield p
        p = [p[0] if i == 0 or i == len(p) else p[i-1] + p[i] for i in range(len(p) + 1)]

def triangle6():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p) - 1)] + [1]
                                                                                                                 
def triangle7():
    p = [1]
    while True:
        yield p
        p.insert(0,0)
        p.append(0)
        p = [p[i] + p[i+1] for i in range(len(p) - 1)]

def triangle8():
    p = [1]
    while True:
        yield p
        a = p[:]
        b = p[:]
        a.insert(0,0)
        b.append(0)
        p = [a[i] + b[i] for i in range(len(a))]

def triangle9():
    p = [1]
    while True:
        yield p
        p.append(0)
        p =  [p[i-1] + p[i] for i in range(len(p))]

def triangle10():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

def triangle11(n):
    if n == 1:
        return [1]
    if n > 1:
        a = triangle11(n-1)
        b = triangle11(n-1)
        a.insert(0,0)
        b.append(0)
        return [a[i] + b[i] for i in range(n)]

n = 0
for i in triangle9():
    print i
    n += 1
    if n == 11:
        break

for i in range(1, 12):
    print triangle10(i)
