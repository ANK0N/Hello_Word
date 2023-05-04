"""
通过def定义的函数是带有名称的函数
但是通过lambda定义的函数可以是没有名称的匿名函数
无名称的匿名函数只能临时使用一次

我感觉只能塞进def的调用中
"""


# lambda函数定义语法
# lambda 传入值:操作(语句操作,但是只能写一行)
def test_func(computer):
    my_num = computer(1, 2)
    print(my_num)


test_func(lambda x, y: x + y)  # 可以将lambda当作一整个函数传进去参加计算
