# 序列 :指的是内容连续,有序,可使用下标当做索引的一类数据容器
# 序列的常见操作 切片  [1, 2, 3, 4, 5]  ->  [2, 3, 4] 取出来一个就叫切片

"""
语法: 序列[起始下标:结束下标:步长]
1. 起始可以留空,试做从头开始
2 .结束也可以留空,试做到末尾,但是不包含末尾是小于的关系不是小于等于
3. 步长
    步长1表示一个一个取
    步长2表示每次跳过1个元素取
    步长N表示每次跳过N-1个元素取数
    步长为负数表示反向取,同时起始和结束也要负数

"""
my_list = [1, 2, 3, 4, 5, 6]
my_list1 = my_list[1:4]  # 将my_list从
print(my_list1)

my_tuple = (1, 2, 3, 4, 5, 6)
my_tuple1 = my_tuple[:]  # 全部默认值的话就只写一个" : "即可
print(my_tuple1)
my_tuple2 = my_tuple[::2]  # 在都取默认值还需要有步长控制时需要在 : 后再写个 :步长
print(my_tuple2)

# 反向 , 步长为负数就是反过来倒叙
my_str = '123456789'
my_str1 = my_str[::-1]  # 等同于将序列反转了
print(my_str1)

my_list = [1, 2, 3, 4, 5, 6]  # 从3开始到1结束,需要利用步进将其变为倒叙
my_list3 = my_list[3:0:-1]
print(my_list3)
