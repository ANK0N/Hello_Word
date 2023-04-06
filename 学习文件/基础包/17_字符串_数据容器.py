""""
字符串也是每个字符的容器

字符串也是不可以修改的容器,和元组一致
只能存储字符串
长度任意(受到内存限制)
允许重复字符存在
支持循环遍历

"""
my_str = "苟利国家生死以"
print(my_str[0])
lens = - + len(my_str)
print(my_str[lens])

# index
my_str.index("苟")
print(my_str.index("苟"))

# replace  并不是修改了my_str的本身,而是产生了一个新的字符串,一般需要一个变量来接收
my_str.replace("苟", "狗")
print(my_str.replace("苟", "狗"))

# 字符串.split(分隔符)  将字符串分割成列表  并不是修改了my_str的本身,而是产生了一个新的列表,一般需要一个变量来接收
my_str1 = "岂 因 祸 福 避 趋 之"
print(my_str1.split(" "))

# 字符串的规整操作,用来消除字符串中的前后空格和换行符
# 语法:字符串.strip(不参数会删除前后空格和换行符 / 传入参数去除指定字符 (满足括号内的任何一个都将会被去掉))
my_str = "  岂 因 祸 福 避 趋 之  "
print(my_str.strip())  # 不传入参数去除首尾空格
my_str = "12岂 因 祸 福 避 趋 之21"
print(my_str.strip("12"))  # 传入参数去除指定字符 (满足括号内的任何一个都将会被去掉)

# len(字符串) 查询字符串长度
# count(字符) 查询出现次数

my_str = "苟利国家生死以,岂因祸福避趋之"
len(my_str)
my_str.count("苟")

# 字符串的遍历
# while遍历字符串
num = 0
while num < len(my_str):
    print(my_str[num])
    num += 1

# for 遍历字符串
for i in range(0, len(my_str)):
    print(my_str[i])

# 可以直接循环列表来字符串
for i in my_str:
    print(i)
