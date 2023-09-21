"""
写在类中的行为
在类中的函数就叫做方法
"""


class Student:
    name = None  # 记录姓名
    gender = None  # 记录性别

    def say_hi(self):
        print(f"HI , 我是{self.name}")

    def say_wuhu(self):
        print("可以不用传参")


stu_1 = Student()

stu_1.name = 'ANKON'
stu_1.gender = '男'

print(stu_1.name)
print(stu_1.say_hi())
print(stu_1.say_wuhu())
"""
self 是必须存在的,只要使用其中的方法

--是在成员方法中想要使用成员变量就需要用self来调用
--虽然存在但是可以不传参

1. 他用来表示类对象滋生
2. 使用类对象调用方法时,self会被自动传入
3. 在方法内部想要访问类的成员变量需要使用self
"""


class Niuma:
    name = None

    def asy_hai(self):
        print(f"俺是{self.name}")


# 构建对象时需要加()
clas_hai = Niuma()

clas_hai.name = "ANKON"
print(clas_hai.asy_hai())
