# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:49:43 2018

@author: St
"""

#第一步获取参数

import sys,shelve,pyperclip

if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    print('参数输入“save”，保存剪贴板到｛｝中。'.format(sys.argv[2]))
elif sys.argv[1].lower()=='list':
    print('参数输入“list”，列出已保存的剪贴板变量。')
else:
    print('参数错误，退出程序')
    