"""
运算符是
算术运算符 : + - * /
"""

a = 1
b = 2
c = a + b
print(a, b, c)
# 为什么在打印后有个空行
print(a, b, c, end='\n')  # 表示为末尾换行
print(c - a)
print(c * a)
print(c / a)
print(c / 2)  # 除法
print(c // 2)  # 整除,没有小数
print(2 ** 3)  # 2的3次幂
print(3 % 2)  # 取余数
# 键盘输入一个3位数 , 打印他的个位数 , 十位数 ,百位数
user = int(input('三位数'))
print(user % 10)             # 个位数
print((user % 100)//10)      # 十位数
print((user % 1000)//100)    # 百位数

print(user % 10)   # 个位数
print(user // 10 % 10)   # 十位数
print(user // 100)   # 百位数






