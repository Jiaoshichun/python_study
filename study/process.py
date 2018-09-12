#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process
from multiprocessing import Pool

# pid=os.fork()
# if(pid==0):
# 	print('我是子进程 %s' %os.getpid())
# else:
# 	print('我%s 开了一个子进程 %s' %(os.getpid(),pid))

'''
def child_run(name):
	print('子进程在运行 %s ' %name)
if __name__ == '__main__':
	print('parent process %s' %os.getpid())
	p=Process(target=child_run,args=('子进程参数',))
	p.start()
	p.join()#等待子进程运行
	print('子进程运行完毕')
'''


