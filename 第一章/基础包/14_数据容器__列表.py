# 重复的变量定义赋值不高效且不优雅
"""
数据容器:
    一种可以容纳多份数据的数据类型,容纳的每一份数据都称之为一个元素,每一种元素都可以是不同的数据类型,例如字符串,数字,布尔型
分类:
    列表,元组,字符串,集合,字典


题外话:↓
函数和方法的区别:
函数: def add(x,y):
        return x+y
方法: class Student:

        def add(x,y):
            return x+y

函数和方法的功能一致,都有传入参数,有返回值,只是方法的使用格式不同
函数的使用: num=add(1,2)
方法的使用:   student = Student()  #去Student中将方法点出来,后面利用'student.'直接调用
            num = student.add(1,2)
"""
"""
列表操作统计
"""
# 1  _ 列表.index(元素)              查询指定元素在列表中的下标值,找不到会报错ValueError
# 2  _ 列表[下标]=新值               将目标下标的元素替换成指定的值
# 3  _ 列表.insert(下标,元素)        指在列表的指定位置插入指定的元素
# 4  _ 列表.append(元素)            追加元素到列表的尾部
# 5  _ 列表.extend(其他数据容器)      追加其他容器到列表的尾部
# 6  _ del 列表[下标]                删除指定下标的元素
# 7  _ 列表.pop[下标]               删除指定下标的元素后也可以被变量接收
# 8  _ 列表.remove(元素)            从前往后删除遇到的第一个符合条件的元素
# 9  _ 列表.clear()                 清空列表[]
# 10 _ 列表.count("待查询次数的元素")  查询列表中指定元素的数量
# 11 _ len(列表)                     列表中共有多少元素


# list 列表-------------------------------------------------------------------------------------------------------------
"""
列表可以一次存储多个数据
元素:数据容器中的每一个数据都可以叫做元素

列表中的元素类型不受限制
列表中也可以包含列表,嵌套的列表
取值范围不要超出列表范围,不然会报超出报错

定义变量:
    变量名称=[元素1,元素2,元素3,元素4.....]
定义空列表:
    变量名称 = []
    变量名称 = list()

"""
name_list = ['ANKON', 'PYTHON', 'ITCAST']
print(name_list)
print(type(name_list))  # 返回的类型是list

my_list = ['芜湖', 123, True]
print(my_list)
print(type(my_list))  # 列表内可存储任何形式的数据

my_list_1 = [['ANKON', 'PYTHON', 'ITCAST'], ['芜湖', 123, True]]
print(my_list_1)
print(type(my_list_1))  # 列表中也可以嵌套列表

# 通过下标来取出列表中的指定元素---------------------------------------------------------------------------------------------
"""
下标索引
    从前向后是从0开始的
    从后向前是从-1开始的


"""
list_test = ['列表', '元组', '字符串', '集合', '字典']
print(list_test[1])  # 正数第二个:元组
print(list_test[-2])  # 倒数第二个:集合

# 嵌套索引的读取: 列表名称[ 嵌套列表的位置 ][ 嵌套列表中需要读取元素的位置 ]
print(my_list_1[0][1])
"""









"""
# 列表的常用操作----------------------------------------------------------------------------------------------------------
"""
列表同时也包含这些操作
    插入,删除,清空,修改,统计个数
"""
# <-{ 查询 }->:     列表.index(元素) 查询指定元素在列表中的下标值,找不到会报错ValueError
# index可以称之为方法
list_test = ['列表', '元组', '字符串', '集合', '字典']

index = list_test.index('元组')
print(index)  # 返回值:1
"""
index = list_test.index('芜湖')
print(index)  # 返回报错:ValueError: '芜湖' is not in list
"""

# <-{ 修改 }->:     列表[下标]=新值
list_test = ['列表', '元组', '字符串', '集合', '字典']
list_test[1] = '芜湖'
print(list_test)  # 返回 ['列表', '芜湖', '字符串', '集合', '字典'] ,元组已经被替换

# <-{ 插入 }->:     列表.insert(下标,元素) 指在列表的指定位置插入指定的元素
list_test = ['列表', '元组', '字符串', '集合', '字典']
list_test.insert(5, '啊哈')
print(list_test)  # 返回 ['列表', '芜湖', '字符串', '集合', '字典', '啊哈'] ,会在指定位置插入
# 那么在已有位置上进行插入
list_test.insert(0, '已有位置插入')
print(list_test)  # 返回 ['已有位置插入','列表', '芜湖', '字符串', '集合', '字典', '啊哈'] ,也会在指定位置插入,但是会将其他元素后移

# <-{ 追加1.0 }->      列表.append(元素),追加到列表的尾部
list_test.append('追加测试')
print(list_test)  # 会将元素追加到列表尾部

# 列表.extend(其他数据容器),追加到列表的尾部
list_test.extend(name_list)
print(list_test)  # name_list的列表已经被一整个追加到list_test后面

# <-{ 删除 }->

# 方法1:del 列表[下标]
name_list = ['ANKON', 'PYTHON', 'ITCAST', 'PYCHARM']
del name_list[0]
print(name_list)  # 成功删除掉ANKON

# 方法2:列表.pop[下标]
name_list = ['ANKON', 'PYTHON', 'ITCAST', 'PYCHARM']
name_list1 = name_list.pop(0)
print(f"可以通过变量来接收取出来的值[{name_list1}],同时列表{name_list}也完成了删除")

# 方法3:列表.remove(元素)
name_list = ['ANKON', 'PYTHON', 'ITCAST', 'PYCHARM', 'ANKON']
name_list.remove('ANKON')  # 从前到后遇到的第一个进行删除
print(name_list)

# <-{ 清空 }->    列表.clear()
name_list.clear()
print(name_list)  # 列表被清空为[]

# <-{ 计数 }->    列表.count("待查询次数的元素")
name_list = ['ANKON', 'PYTHON', 'ITCAST', 'PYCHARM', 'ANKON']
count = name_list.count('ANKON')
print(f"name_list列表中 ANKON 存在{count}个")
# 统计列表内共有多少元素   len(列表)
count = len(name_list)
print(f"列表中共有{count}个元素")  # 列表中共有5个元素
