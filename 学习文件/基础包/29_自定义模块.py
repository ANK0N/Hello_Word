"""
自定义模块
就创建一个普通的py文件即可,然后要在同一目录下

如果,调用两个包里的同一个名称的函数,第二次的会将第一次的覆盖
"""
import mode_test1

mode_test1.test(5, 10)
# 如果在模块内进行了调用,则在导入时也会执行模块内的函数调用语句

# main变量
"""
if __name__ == '__main__':
    test(1, 2)
需要将测试的流程或者语句总加入到main下

"""

# all变量,可以来控制在利用*调用时可以导入的功能
"""
__all__ = ['test']
def test(a, b):
    print(a + b)
def test1(a, b):
    print(a - b)
在通过*调用时就只能有test了
"""
from mode_test1 import *

test(1, 3)  # 有这个函数,但是没有test1
