"""
if
if...else
if...elif...else

if的格式

if 条件:
    条件成立要执行的格式
elif
"""
'''
n = input('请输入(y/n):')
if n == 'no':
    print('输入错误')
elif n == 'yes':
    print('输入正确')
else:
    print('请输入正确参数')
'''
# 利用 import 函数来调用库完成操作


'''
import random

run = random.randint(1, 5)
shu = input('输入数字:')
if str(run) == str(shu):
    print('我焯太牛了,你猜对了')
    print('药材的数字是!' + str(run))
else:
    print('我焯太涝了')
'''

# 常规的  if else
# 条件较多的  if  elif  elif  else
"""
if 条件1:
    条件打成执行的语句:
elif 条件2:
    条件打成执行的语句
else:
    都不达成执行的语句
"""

# 输入一个销售金额,进去判断我的销售金符合哪种奖励的范围
"""
10000-50000    奖励1000大洋
50000-100000   奖励笔记本
100000-1000000 奖励iphone 13 pro max
1000000以上     奖励特斯拉
"""
money = str(input('这个月为资本家打工挣了多少钱啊?'))
print('您本月的业绩是' + money + '元')
if 10000 < int(money) < 50000:
    print('奖励1000大洋')
elif 50000 < int(money) < 100000:
    print('奖励笔记本一台')
elif 100000 < int(money) < 1000000:
    print('奖励iphone 13 pro max')
elif int(money) < 10000:
    print('多捞啊')
else:
    print('我焯,你是真牛逼啊')
    print('奖励特斯拉一辆')
