#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# d['王五']=12
# a=(12,12);
# d[a]=123;
# print(d.get((12,12)))

# 关键字参数
# d={'张三':10,"赵四":11}
# def person(name,age,**kw):
# 	print('name:%s,age:%s,kw:%s' %(name,age,kw))
# person('张三',11,city='北京',sex='男')
# person('张三',11,**d)

# # 默认参数
# def person1(name,age,city='北京',sex='男'):
# 	print('name:%s,age:%s,city:%s，sex:%s' %(name,age,city,sex))
# person1('李四',20,sex='女')

# # 可变参数
# def student(*name):
# 	print(name)
# s=['张三','李四','王五']
# student(*s)

# # 命名参赛  命名参赛必须传参数名
# def peron2(name,age,*,city='北京',sex='男'):
# 	print('name:%s,age:%s,city:%s，sex:%s' %(name,age,city,sex))
# peron2('张三',11,city='北京',sex='男')

# # 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# # 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

# 装饰器
import functools


def log(text):
    def dis(func):
        @functools.wraps(func)
        def wrapper(*age, **kw):
            print('%s:%s' % (text, func.__name__))
            return func(*age, **kw)

        return wrapper

    return dis


@log('方法名')
def sum():
    print('sum')


def main():
    sum()


if __name__ == '__main__':
    main()
