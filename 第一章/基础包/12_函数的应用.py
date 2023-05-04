# 函数:是组织好的可使用的,用来实现功能的代码块  例如:len(获取长度)
# 我们使用函数是为了得到一个针对特定需求,可重复利用的代码段,提高程序的复用性,减少重复代码的存在
"""
前面使用的 str() int() type() input() print() 都是函数

↓不使用内置函数来完成 len 的功能
"""
str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count += 1
print(f"{str1}共有{count}个字符")

count = 0
for i in str2:
    count += 1
print(f"{str2}共有{count}个字符")

count = 0
for i in str3:
    count += 1
print(f"{str3}共有{count}个字符")

# 过于重复 ,只有小部分一致 ,其他部分几乎一模一样 所以才需要使用函数来优化
"""
def [函数名称]([传入变量名称])
return [需要输出的东西] -- 用来返回函数计算出来的值
"""


def my_len(data):
    my_count = 0
    for j in data:
        my_count += 1
    return f"{data}共有{my_count}个字符"


print(my_len(str1))
print(my_len(str2))
print(my_len(str3))
