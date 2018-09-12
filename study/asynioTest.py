#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from aiohttp import web
from flask import Flask, request, render_template


async def index(request):
    await asyncio.sleep(0, 5)
    return web.Response(body=b'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
<h1>Home</h1>
</body>
</html>''', content_type='text/html')


async def init(l):
    app = web.Application(loop=l)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
