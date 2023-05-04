"""
由于列表是可以被修改的,但是从需求上看,咱们不想他能被修改,所以才有的元组
# 定义元组
元组 = (元素1,元素2,元素3.....)

# 空元组
元组 = ()
元组 = tuple()

如果对元组执行修改的话,会报错
TypeError: 'tuple' object does not support item assignment

但是如果元组中嵌套了一个list便可以修改
t7 = (1, 2, 3, [1, 2, 3])
t7[3][0] = 5
print(t7)
"""

t1 = (1, 'ANKON', True)
t2 = ()  # 空元组
t3 = tuple()  # 空元组

# ↓以下类型皆为 tuple
print(type(t1))
print(type(t2))
print(type(t3))

# 如果元组中只有一个元素,那也需要额外写上一个逗号
t4 = ('ANKON',)
print(type(t4))

# 元组的嵌套
t5 = (t1, (4, 5, 6))
print(t5)  # 嵌套结果((1, 'ANKON', True), (4, 5, 6))

# 和list一样都支持下标索引
print(t5[1][2])  # 嵌套后的取数逻辑和列表一致

"""
元组的主要操作
index ()查找
count() 计数
len() 长度
"""
t6 = (1, 2, 3, 4, 4, 3, 2, 1, 1, 1)
print(t6.index(2))  # 第一个2的下标为1
print(t6.count(1))  # 1的总个数为4
print(len(t6))  # 总长度为10


print("-----------------------------------------------------")
"""
元组的遍历
"""
# while遍历元组
num = 0
while num < len(t6):
    print(t6[num])
    num += 1

# for 遍历元组
for i in range(0, len(t6)):
    print(t6[i])

# 可以直接循环列表来元组
for i in t6:
    print(i)

t7 = (1, 2, 3, [1, 2, 3])
t7[3][0] = 5
print(t7)
