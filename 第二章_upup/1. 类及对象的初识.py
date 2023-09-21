"""
生活中设计中都可以设计生产表格
设计表格 __ 设计类
打印表格 __ 创建对象
填写表格 __ 对象属性赋值

类中也就包含属性和行为

类的属性 _ 定义在类中的变量(成员变量)
累的行为 _ 写在类中的函数(成员,方法)
"""


# 设计一个类 (设计一张表)
class Student:
    name = None  # 记录姓名
    gender = None  # 记录性别
    nationality = None  # 记录国籍
    native_place = None  # 记录籍贯
    age = None  # 记录年龄

    # 创建一个对象(打印一张表)


# ↓ 创建类对象
stu_1 = Student()  # stu_1既是变量 , 也是对象

# 对对象属性进行赋值(填写表单)
stu_1.name = 'ANKON'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '河北'
stu_1.age = '22'

# 获取对象中的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
