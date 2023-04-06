# 位运算
"""
都是针对于二进制的运算 & | ^ ~ << >>
&  类似于  and
|  类似于  or
^  异或运算,相同为0不同为1

"""

n1 = 0b0110
n2 = 0b0010
print(n1 & n2)
'''
比较结果是
从后往前的
0和0做对比 -- 0&0 --假 为0
1和1做对比 -- 1&1 --真 为1
1和0做对比 -- 1&0 --假 为0
0和0做对比 -- 0&0 --假 为0
即为 0b0010 = 2  ---->  输出的为 十进制的2
'''
print(n1 | n2)  # = 0110 = 6
print(n1 ^ n2)  # = 0100 = 4
print(5 ^ 9)  # 0101 1001 = 1100 = 12
"""
bit  b

byte  比特
n=2
其中n也是占位符也会占有内存


已知十进制的负数 , 求二进制的负数表示
原码 0110
反码 1001
补码 反码加一
1001 +1
则 1010 = 10
5的
原码 0101
反码 1010
补码 1011 = 11

2. 已知二进制的负数 (判断是否是付的二进制的依据 , 看二进制的最高位: 1111 1010 最高位为1为负数 ,最高位为0 , 则为正数)

1.负的二进制  2.二进制减一  3.取反 4.将转成的前面转成十进制 , 在前面加上负号

将二进制-1 --> 取反 = 原码
将最后的十进制的前面加上符号就是了
1110 --> 0001 = -1
 ` 
"""
print(~n1)  # n1 = 取反:0b0110 = 1001 =1000
print(~7)  # 就是将7的二进制取反

# 1_练习
"""
1. ~7 
7的二进制 0000 0111
取反     1111 1000
减一     1111 0111  此时是付的二进制
对付的二进制的处理
将      1111 0111
取反     0000 1000  =  8
由于是付的二进制  ,也要给8带上负号  ,则为-8

2. -9 
-9 的二进制 0000 1001
1111 0110 加一 1111 0111
取反 00001000 = 8

3.~-4 
先求-4的二进制   0000 0100 --> 1111 1011
取反加一  1111 1100 
取反 0000 0011 = 3

4. 1111 1101 十进制 
已知是付的二进制
减一
1111 1100
取反 0000 0011 = -3
"""






















