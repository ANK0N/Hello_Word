"""
列表元组字符串 都支持元素重复也是有序的
而集合不支持元素重复,且内部是无序的

变量名 = {}
变量名 = set()

不支持下标索引但是可以修改
"""
# 定义集合   变量名 = {}
# my_set = {"元素1", "元素2", "元素3", "元素4", "元素5"}
# 定义空集合 变量名 = set()
# my_set = set()

my_set = {"元素1", "元素2", "元素3", "元素1", "元素2", "元素3"}
my_set_empty = set()
print(f"my_set的类型是{type(my_set)},他的内容是{my_set}")  # 会自动去重,且乱序了
print(f"my_set_empty的类型是{type(my_set_empty)},他的内容是{my_set_empty}")

# 对集合添加新元素
my_set.add("PYTHON")
my_set.add("元素1")
print(my_set)  # 结果增加了新元素且去重了

# 移除指定元素
my_set.remove("元素2")
print(my_set)  # 指定的值被移除

# 随即取出   由于列表有下标可以取出指定下标的元素,但是集合无下标就是随机取出
print(my_set.pop())  # 随机取出一个

# 清空
my_set.clear()
print(my_set)  # set()  被清空为空集合了


#
#
# 两个集合的差集,返回出一个空集合 (集合1有 集合2没有 的)
# difference
my_set1 = {1, 2, 3, 4, 5, 6}
my_set2 = {1, 4, 6}
my_set3 = my_set1.difference(my_set2)
print(f"集合1为{my_set1}\n集合2为{my_set2}\n差集为{my_set3}")

# 消除差集  对比集合1和集合2,并删除集合1中和集合2相等的元素
# difference_update
my_set1.difference_update(my_set2)
print(f"去除集合2后集合1的剩余元素为:{my_set1}")

# 集合的元素个数
my_set1 = {1, 2, 3, 4, 5, 6}
print(len(my_set1))

# 集合之间的合并   集合1.union(集合2)
my_set1 = {1, 2, 3, 5, 6, 7}
my_set2 = {1, 4, 6}
print(f"两集合合并的结果为{my_set1.union(my_set2)}")

# 遍历集合  # 由于没有下标则无法使用while来遍历
# for 遍历集合
# 可以直接循环列表来遍历
for i in my_set1:
    print(i)

