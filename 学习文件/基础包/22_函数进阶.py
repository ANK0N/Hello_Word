# 函数的多返回值
"""
由于函数在return以后就已经会

"""


def return_num():
    return 1
    return 2


my_num = return_num()
print(my_num)


# 这样的话只会有一个返回值,那么要怎么解决呢 ?
def return_num():
    return 1, 2


my_num1, my_num2 = return_num()
print(my_num1)
print(my_num2)


# 可以通过 return 返回值1,返回值2 来返回多个返回值 , 而结果也可以用两个变量接收 变量1,变量2 = 返回值1,返回值2


# 函数的多传参
# 1. 位置参数
def user_info(name, age, gender):
    print(f"您是{name},您{age}岁了,您是{gender}")


user_info("ANKON", "22", "男人")
# 通过将内部参数使用key:value对应来传入参数
user_info(name="ANKON", age="22", gender="男人")
"""
键值传参可以打乱顺序
可以和位置传参一起使用,但是位置参数位置必须正确
"""


# 2. 缺省参数   设置默认值的一定要在最后,从最后往前排着写
def user_info1(name, age=20, gender="男人"):
    print(f"您是{name},您{age}岁了,您是{gender}")


# 在不传入后使用默认值
user_info1("ANKON")
# 传入后默认不用
user_info1("aili", "20", "女孩")


# 3. 可变参数  在调用时不确定会传入多少参数
# 位置传递的不定长
def user_info(*agrs):  # 默认为元组
    print(agrs)


user_info("TOM")  # ("TOM")的元组
user_info("TOM", "18")


# 关键字传递的不定长
def user_info(**kwargs):  # 默认为元组
    print(kwargs)


user_info(name="TOM",age="22")

# 参数不定的
