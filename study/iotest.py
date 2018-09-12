#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


# 查找文件
def selectFile(path, s):
    for root, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            if s == file_name:
                print(os.path.abspath(os.path.join(root, file_name)))
                return


# 使用元类实现 namedtuple  
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
def tupleC(name, attr):
    class Meta(type):
        # 定义一个元类，采用`__call__`方法来拦截类的实例化，在实例化之前我们先把位置参数全部转入一个叫args的元组中，
        # 然后在调用type的`__call__`方法，从而把刚才的元组传进去，这样就只有一个参数了，从而无论你传入多少个位置参数，
        # 在这个步骤之后，只会出现一个参数了，成功！
        def __call__(self, *args):
            return type.__call__(self, args)

    def init(self, args):
        if len(args) != len(attr):
            raise ValueError('参数数量不对')
        self._value = tuple(args)

    # self._attr=attr

    def _getattr(self, attr):
        for i, value in enumerate(attr):
            if value == attr:
                return self._value[i]
        return tuple.__getattr__(self, attr)

    def _setattr(self, attr, value):
        if attr != '_value' and attr != '_attr':
            raise ValueError('参数值不可变')
        tuple.__setattr__(self, attr, value)

    t = Meta(name, (tuple,), dict())
    t.__init__ = init
    t.__setattr__ = _setattr
    t.__getattr__ = _getattr
    t.__str__ = lambda s: '%s%s' % (name, s._value)
    t.__repr__ = t.__str__
    return t


def main():
    # selectFile('.','ShoppeVideoActivity.java')
    # a=os.walk('.')
    # next(a)
    # next(a)
    # print(next(a))
    Point = tupleC('Point', ['x', 'y', 'z'])
    p = Point(5, 6, 1923)
    # p.x=10
    print(p.z)
    print(p)


if __name__ == '__main__':
    main()
