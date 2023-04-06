"""
都是针对于二进制的运算 & | ^ ~ << >>
&  类似于  and
|  类似于  or
^  异或运算,相同为0不同为1
<< 左移

"""
'''左移'''
n = 12  # 1100
# 是将00001100这个二进制向左移动 , 左边少两个00同时在右边补上两个00 则为 00110000 = 48
print(n << 1)  # 24  = 12*2的1次
print(n << 2)  # 48  = 12*2的2次
print(n << 3)  # 96  = 12*2的3次
print(n << 4)  # 192 = 12*2的4次
print(n << 5)  # 384 = 12*2的5次
print(n << 6)  # 768 = 12*2的6次
'''右移'''
m = 12  # 1100
print(n >> 1)  # 6  12 整除 2 ==6
print(n >> 2)  # 3  12 整除 2的2次 ==3
print(n >> 3)  # 1  12 整除 2的3次 ==1
print(n >> 4)  # 0
print(n >> 5)  # 0
print(n >> 6)  # 0

"""
n = 89  右移5位
89/32 = 2
93 左移3位
"""

#######################################################################################################################
# 优先级   --- 括号可以改变运行顺序
x = 20
result = 20*5**2  # 先计算5的2次方然后乘以20 =500
print(result)

a = 1
b = 2
print(b > a + x < a + b)  # 计算顺序 优先计算加减 (2>21<3) 不成立 所以为 False
print(b > a + (x < a + b))  # 计算顺序 括号内的计算是 20<1+2 为假 假为0 然后 b > a + 0 = 2 > 1 为真 True
































