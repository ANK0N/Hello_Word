"""
def 函数名称(传入变量名称):
    函数体
    return 返回值  <-- 用来返回函数计算出来的值,可以将结果返回给函数的调用者


没有设置返回值的函数都会返回none,或者 return None 代表着函数没有返回有意义的东西,none的类型为Nonetype,代表着没有意义

None值的价值
1. 可以用在函数没有实际返回值上面
2. 可以用在if判断上,且None等同于false,可以做出相关处理
3. 可以赋予给变量,在他并没有值的时候,先不提供值给变量
"""


# 1. 定义函数
def say_hi():
    print("你好哇~")  # 输出一句话
    return "你好哇~~~"  # 返回值是这句话


# 函数定义完以后,需要进行调用才能开始工作
say_hi()  # 只执行了打印操作
print(say_hi())  # 不过打印,也返回了值


# 2. 传入参数功能: 在调用时可以接收外部传输的值
def my_add(num1, num2):
    number = num1 + num2
    return number


num3 = my_add(7381, 3278931)
print(num3)


# 3.返回值 None
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None


result = check_age(20)
if not result:  # 利用not反转来完成
    print("没成年呢奥!")
else:
    print("成年哩,速速让我访问")

name = None  # 可以赋予给变量,在他并没有值的时候,先不提供值给变量


# 4.函数的注释 补齐函数的说明文档奥!
def my_add(num1, num2):
    """
    :param num1: 数字1
    :param num2: 数字2
    :return: 输出相加的值
    """
    number = num1 + num2
    return number


# 5.函数的调用 在一个函数中调用了其他的的函数 其中若函数A调用了函数B,会将函数B全部执行完后继续执行函数A的内容
def test1():
    print("--1--")


def test2():
    test1()
    print("--2--")


test2()

# 6.函数中的变量作用域 指的是变量的作用范围
# 局部变量: 函数内部声明的变量在函数外面调用不到,出了函数体就无法使用了
# 全局变量: 在函数体外部声明的变量就为全局变量在函数内外都可以调用和使用
# 在函数内修改全局变量 global
num4 = 100


def test3():
    global num4  # 声明调用的变量名为全局变量,里面和外面就是同一个了
    num4 += 1000
    print(num4)


test3()
