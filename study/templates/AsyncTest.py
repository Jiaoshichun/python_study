#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def consumer():
    r = ''
    while True:
        n = yield r
        print("consumer:%s" % n)
        r = 'ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("生产者:%s" % n)
        r = c.send(n)
        print('消费剩下:%s' % r)
    c.close()


if __name__ == '__main__':
    consumer()
    produce(consumer())
