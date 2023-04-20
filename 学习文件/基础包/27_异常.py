"""
异常: 当程序运行时检测到错误,届时会出现一堆提示,就是异常



"""
# 异常展示
# f = open("ANKON", "r")
"""
Traceback (most recent call last):
  File "D:\python ankon\学习文件\基础包\27_异常.py", line 8, in <module>
    f = open("ANKON","r")
FileNotFoundError: [Errno 2] No such file or directory: 'ANKON'
"""
# 异常的捕获  对可能出现在异常进行提前准备,提前处理
"""
基本语法
# 捕获全部异常

try:
    可能出现的代码
except:
    如果出现异常则执行的代码
else: #可写可不写
    没有异常时执行的代码
finally:
    无论如何都要执行的语句
    f.close() 一般可以用来关闭调用的资源


# 捕获指定异常
try:
    可能出现的代码
except 异常类型 as 别名:
    如果出现异常则执行的代码
    print(别名)  # 可以将异常作为对象获取
存在多个时,可以将异常用元组展示
except (异常类型1,异常类型2) as 别名:

# 捕获所有异常
try:
    可能出现的代码
except Exception as 别名: # 可以捕获所有的异常
    print(别名)
"""
# try:
#     f = open("ANKON.txt", "r")
# except Exception as d:
#     f = open("ANKON.txt", "w")


print("_____异常的传递性_____")


# 函数2包含函数1时,1的异常会逐步传递到函数2和调用流程中
# 虽然异常会传递,但是也会截断异常语句后面的语句
# 异常的处理可以在高层级处理
def func1():
    print("func1开始")
    num = 1 / 0
    print("func1结束")


def func2():
    print("func2开始")
    func1()
    print("func2结束")


def main():
    try:
        func2()
    except Exception as a:
        print(a)


main()
