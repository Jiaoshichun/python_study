#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    # return '<h1>Home</h1>'
    return render_template('Home.html')


@app.route('/signin', methods=['GET'])
def logon():
    # return '''<form action='/logon' method='post'>
    # <p><input name='username'></p>
    # <p><input name='password' type='password'></p>
    # <p><button type='submit'>Log On</button></p>
    # </from>'''
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def toLogon():
    # if request.form['username'] == 'chun' and request.form['password'] == '111111':
    #     return '<h3>Hello,Chun</h3>'
    # return '<h3>Bad username or password</h3>'
    username = request.form['username']
    password = request.form['password']
    if username == 'chun' and password == '111111':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password')


if __name__ == '__main__':
    app.run()
