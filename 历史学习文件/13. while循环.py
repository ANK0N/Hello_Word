"""
none = True               --要声明控制循环的变量
number = 0                --被操作的变量
while none:               --声明循环开始
    number += 1           --循环的操作
    if number > 10:
        none = False      --当控制循环为False退出循环
    if number % 2 == 1:
        print(number)
"""

# for 循环 , 是一个计次循环再循环数已知的情况下
# for 循环的范例
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
import random
count = 0
number = 0
run = 1
while run <= 3:
    ran = str(random.randint(0, 2))
    # print(ran)
    status = str(input('猜拳 , 石头(0),剪刀(1),布(2)'))
    if (status == '0' and ran == '1') or (status == '1' and ran == '2') or (status == '2' and ran == '0'):
        count += 1
        print('你赢啦')
    elif (status == '0' and ran == '0') or (status == '1' and ran == '1') or (status == '2' and ran == '2'):
        print('平局')
        run -= 1
    else:
        print('机器赢')
        number += 1
    run += 1
if count > number:
    print('三局两胜你赢了')
elif count < number:
    print('三局两胜你输啦')
else:
    print('平局')
