"""
break     -- 跳出循环
continue  -- 跳过当前批次循环
pass      --循环中的占位符 , 什么都不做


"""
'''
# 不打印能被3整除的
for i in range(10):
    if i % 3 == 0:
        continue
    else:
        print(i)

print('*-' * 10)
for i in range(10):
    if i % 3 == 0:
        continue  # 跳过本次循环,令下面的语句都不执行
    print(i)
'''
# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + 'X' + str(i) + '=' + str(j * i), end=" ")
    print('')

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print('')

print('-----------------------------')

for i in range(1, 6):
    for j in range(1, 7-i):
        print('*', end='')
    print('')


