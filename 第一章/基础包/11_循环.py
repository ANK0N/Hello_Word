"""
条件 = True               --要声明控制循环的变量
number = 0                --被操作的变量
while 条件:               --声明循环开始
    number += 1           --循环的操作
    if number > 10:
        条件 = False      --当控制循环为False退出循环
    if number % 2 == 1:
        print(number)

1. 无限循环的控制可以依靠bool类型本身来完成
2. 也可以直接通过break来退出循环
"""
# while计算1...100的和

sum_num = 0
i = 1
while i <= 100:
    sum_num = sum_num + i
    i += 1
print(sum_num)

'''
money = 0
count = 0
while True:
    price = float(input('购买金额:'))
    number = int(input('购买数量:'))
    money += price * number
    count += number
    status = input('停止购买请按(d)')
    if status == 'd':
        print('此次一共购买%s件商品,共消费%.2f元' % (count, money))
        break
'''
"""
猜数字,无限次,会提示猜大了还是猜小了
"""

import random

num = random.randint(1, 10)
print(num)
ji_lu = 0
while True:
    in_num = int(input('猜数字:'))
    ji_lu += 1
    if in_num == num:
        print("猜对了,猜了%s次" % ji_lu)
        break
    elif in_num > num:
        print("猜大了")
    elif in_num < num:
        print("猜小了")

"""
在print后加[,end='']可以使打印结果不换行
在内容中使用/t可以使字符串对其

9*9乘法表
"""

i = 1
while i <= 9:
    txt = ''
    u = 1
    while u <= i:
        txt += f'{u}*{i}={u * i}\t'
        u += 1
    print(txt)
    i += 1

"""
for 临时变量 in 待处理数据集:
可以将待处理数据集中的数据挨个取出 (是序列类型)

range 语句 ---可以生成一个数字序列
for i in range()

while 循环和for循环是可以相互嵌套的

语法:
1: range(number)  = range(5)__(1234)
2: range(number1,number2)  = range(5,10)__(56789)
3: range(number1,number2,set)  = range(5,10.2)__(579) set 为步长
"""
for i in range(10):  # 结果 : 从0到9的序列
    print(i)
for i in range(5, 10):  # 结果 : 从5到9的序列
    print(i)
for i in range(1, 10, 2):  # 结果 : 从1到9的步长为2的序列
    print(i)

for i in range(10):
    print('送玫瑰花')

# 1_练习 : 反馈输入值范围中的偶数个数
s_num = int(input("输入开始值:"))
e_num = int(input("输入结束值:"))
e_num += 1
num = 0
for i in range(s_num, e_num):
    if i % 2 == 0:
        num += 1
print(num)

"""
for i in range(5):
    print(i)

print(i)
循环外的是可以访问到i的值的 ,但是规范上不允许
"""
# for循环的嵌套也是依靠缩进来完成缩进
# 99乘法表      外层循环控制行数,内层循环控制内容

for num_1 in range(1, 10):
    for num_2 in range(1, num_1 + 1):
        print(f"{num_2}*{num_1}={num_1 * num_2}\t", end='')
    print("")

for num_1 in range(1, 10):
    row = ''
    for num_2 in range(1, num_1 + 1):
        row += f"{num_2}*{num_1}={num_1 * num_2}  "
    print(row)

# ---------  对循环的操作  -----------
"""
continue :
1. 循环中存在某些原因需要跳过当前循环执行, 可用continue来跳过
2. 只会对他所在的循环生效
break :
1. 可以直接跳出, 结束循环
2. 只会对他所在的循环生效

"""
