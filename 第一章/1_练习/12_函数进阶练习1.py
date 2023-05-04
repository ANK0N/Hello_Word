# 定义一个函数1,接受另外一个函数2
def my_func1(my_func2):
    num_test1 = my_func2(3, 12)
    print(num_test1)


def my_func2(x, y):
    return x + y

my_func1(my_func2)