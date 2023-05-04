import random

num = random.randint(1, 10)
flow_id = 1
print(num)

while True:
    su_num = int(input('数字:'))
    if flow_id == 3:
        break
    else:
        if su_num == num:
            print('嫩牛哇 , 猜对了')
            break
        elif su_num > num:
            print('大了')
        elif su_num < num:
            print('小了')
    flow_id += 1

# import random

"""优化后的代码使用了for循环来代替while循环,使代码更加简洁易读,同时,用for循环代替while循环使得不必定义额外的变量flow_id,
而是使用范围为(0, 3)的计数器i,从而更加简便,在优化前后的代码差别上,
主要表现为流程的控制方式,优化前的代码使用while循环和break语句来控制流程,在循环体内通过判断变量flow_id的值来决定是否跳出循环,
而优化后的代码使用for循环和break语句来控制流程,并通过else语句在循环结束后打印一段额外信息
"""

num = random.randint(1, 10)
print(num)

for i in range(3):
    guess_num = int(input('请猜一个数字（1-10）： '))
    if guess_num == num:
        print('恭喜你猜对了！')
        break
    elif guess_num > num:
        print('你猜的数字太大了！')
    else:
        print('你猜的数字太小了！')
else:
    print('很遗憾，你连三次机会都用完了，正确答案是 %d' % num)


