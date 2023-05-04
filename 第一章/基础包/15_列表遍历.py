"""
遍历归根结底是利用循环去逐渐增加列表下标值来完成
while遍历列表
for 遍历列表
"""
# 通过下标索引的方式取出
# 循环条件为 下标值<元素数量

my_list = [21, 25, 21, 23, 22, 20]
num = 0

# while遍历列表
while num < len(my_list):
    print(my_list[num])
    num += 1

# for 遍历列表
for i in range(0, len(my_list)):
    print(my_list[i])

# 可以直接循环列表来遍历
for i in my_list:
    print(i)


"""
while适用于申鹤可以循环的场景
for循环适用于遍历容器或者小的循环中
"""