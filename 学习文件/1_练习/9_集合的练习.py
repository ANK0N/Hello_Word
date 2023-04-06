"""
定义一个列表,利用for循环遍历列表,并将值添加至集合,并去重
"""
my_list = [1, 2, "ANKON", 1, 3, "芜湖", 4, 1, "ANKON"]
my_set = set()
for i in my_list:
    my_set.add(i)
print(f"去重后的列表为{my_set}")