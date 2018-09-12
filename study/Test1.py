#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from urllib import request, parse
from html.parser import HTMLParser
from html.entities import name2codepoint


# get请求
def get():
    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print('Data:', data.decode('utf-8'))


def post():
    print('登陆微博')
    email = input('Email:')
    passwd = input('Password:')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    req = request.Request("https://passport.weibo.cn/sso/login")
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    with request.urlopen(req, data=login_data.encode("utf-8")) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


class MyHTMLParser(HTMLParser):
    def error(self, message):
        print('error---message:%s' % message)

    # Overridable -- handle start tag
    def handle_starttag(self, tag, attrs):
        print('handle_starttag---tag:%s,attrs:%s' % (tag, attrs))

    # Overridable -- handle end tag
    def handle_endtag(self, tag):
        print('handle_endtag---tag:%s' % tag)

    # Overridable -- handle character reference
    def handle_charref(self, name):
        print('handle_charref---name:%s' % name)

    # Overridable -- handle entity reference
    def handle_entityref(self, name):
        print('handle_entityref---name:%s' % name)

    # Overridable -- handle data
    def handle_data(self, data):
        print('handle_data---data:%s' % data)

    # Overridable -- handle comment
    def handle_comment(self, data):
        print('handle_comment---data:%s' % data)
        # Overridable -- finish processing of start+end tag: <tag.../>

    def handle_startendtag(self, tag, attrs):
        MyHTMLParser.handle_startendtag(self,tag,attrs)
        print('handle_startendtag---tag:%s,attrs:%s' % (tag, attrs))


def getHTML():
    pars=MyHTMLParser()
    with request.urlopen("https://www.python.org/events/python-events/") as f:
        result=f.read().decode('utf-8')
        print(result)
        pars.feed(result)



def main():
    getHTML()


if __name__ == '__main__':
    main()
