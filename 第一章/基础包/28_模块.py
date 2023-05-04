"""
1.什么是模块
2.导入模块
"""
# 模块就是一个工具包,是一个py文件,可已经内部的定义内容直接拿来用
"""
语法
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
[]是可选的意思

1. 基本语法
import 模块名
模块名.功能名

"""
print("区分线奥+++++++++++++++++++++++++++")
# 导入了内置的time文件,是调用了全部的功能
import time
time.sleep(0.5)  # 延时3秒

print("区分线奥+++++++++++++++++++++++++++")
# 调用time里的一个指定功能
from time import sleep
sleep(0.5)

print("区分线奥+++++++++++++++++++++++++++")
# 调用了全部的功能,还不用 . 来调用
from time import *
sleep(0.5)

print("区分线奥+++++++++++++++++++++++++++")
# 给调用的函数赋予别名
from time import sleep as The_word
The_word(0.5)
