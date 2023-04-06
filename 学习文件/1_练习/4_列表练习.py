"""
有一个列表,内容是:[21,25,21,23,22,20],记录的是一批学生的年龄
请通过列表的功能(方法),对其进行
1.定义这个列表,并用变量接收它
2.追加一个数字31,到列表的尾部
3.追加一个新列表[29,33,30]到列表的尾部,取出第一个元素(应是:21)
5.取出最后一个元素(应是:30)
6.查找元素31,在列表中的下标位置
"""
s_list = [21, 25, 21, 23, 22, 20]  # 定义这个列表,并用变量接收它
print(s_list)

s_list.append(31)  # 追加一个数字31,到列表的尾部
print(s_list)

new_list = [29, 33, 30]  # 赋值新列表
s_list.extend(new_list)  # 追加一个新列表
# 也可以用这种方法追加 s_list.extend([29, 33, 30])
print(s_list[0])  # 取出第一个元素
print(s_list[-1])  # 取出最后一个元素
print(s_list[len(s_list)-1])  # 丈量整体长度-1获得下标值

address = s_list.index(31)  # 查找元素31,在列表中的下标位置
print(address)
