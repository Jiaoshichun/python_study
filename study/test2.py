#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def out(self):
        print('name:%s,age:%s' % (self.name, self.age))


s = Student('zs', 30)
s.out()
print(dir(Student))


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __str__(self):
        return self._path

    def __getattr__(self, path):
        if 'user' != path:
            return Chain('%s/%s' % (self._path, path))
        return lambda path: Chain('%s/%s' % (self._path, path))


print(Chain().list.user('张三').age.repo)
print(type(s))
