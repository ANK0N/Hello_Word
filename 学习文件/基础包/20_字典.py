# 利用Key找到value
"""
有一份表格数据 , 姓名和成绩相互对应
需要使用key来找到关联的value

1. 容纳多个数据,不同类型
2. 都是key和键值对
3. 不支持下标
4. 可以修改
5. 可以for循环遍历
"""
# 字典的定义也是用{} , 但是其内部存储的是一个个的键值对
my_dict = {1: "ANKON", 2: "506036"}
# 空字典定义
my_dict = {}
my_dict = dict()
"""
测试数据
"""
# 定义字典    key:value
my_student = {"王力宏": 99, "周杰伦": 100, "林俊杰": 60}
# 字典中不允许key的重复,新的会将旧的覆盖
# 获取字典中的数据
print(my_student["王力宏"])  # 和使用下标索引的方法一样,利用中括号调用key来获得value

# 字典的嵌套  将表格写入成字典
my_student = {"王力宏": {"语文": 77, "数学": 66, "英语": 33, },
              "周杰伦": {"语文": 88, "数学": 86, "英语": 55, },
              "林俊杰": {"语文": 99, "数学": 96, "英语": 66, }
              }
print(my_student["林俊杰"]["语文"])

print("_________________________________字典的常用操作________________________________________")

my_dict1 = {}
# 新增或者更新元素  字典[key]=value
my_dict1["芜湖"] = "宇宙中心"
print(my_dict1)
my_dict1["芜湖"] = "曹县才是宇宙中心"
my_dict1["曹县"] = "宇宙中心"
print(my_dict1)
# 删除元素  字典.pop(key)
my_dict1.pop("芜湖")
print(my_dict1)
# 清空字典  字典.clear()
my_dict1.clear()
print(my_dict1)
# 获取全部的key  字典.keys()
my_dict1["芜湖"] = "曹县才是宇宙中心"
my_dict1["曹县"] = "宇宙中心"
print(my_dict1.keys())  # 会返回字典中的key值
print(type(my_dict1.keys()))  # 返回格式是dict_keys
# 遍历字典
# 1. 遍历全部的key
dict1_key = my_dict1.keys()
for i in dict1_key:
    print(f"遍历字典值,key为: {i}, 值为: {my_dict1[i]}")
# 2. 直接遍历字典
for i in my_dict1:
    print(f"遍历字典值,key为: {i}, 值为: {my_dict1[i]}")

# 字典长度  len(字典)
print(len(my_dict1))  # 元素数量为2
