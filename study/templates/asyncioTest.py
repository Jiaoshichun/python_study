#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


# @asyncio.coroutine
# def wget(host):
#     print("请求的host:%s" % host)
#     reader, writer = yield from asyncio.open_connection(host, 80)
#     writer.write(('GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host).encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('host:%s headers > %s' % (host, line))
#     writer.close()
async def wget(host):
    print("请求的host:%s" % host)
    reader, writer =await asyncio.open_connection(host, 80)
    writer.write(('GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host).encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('host:%s headers > %s' % (host, line))
    writer.close()


loop = asyncio.get_event_loop()
task = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(task))
loop.close()
