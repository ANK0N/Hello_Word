# str -->整型
type(int('12345') + 1000)
# print('12345'+1000)  字符串无法和整型加减
print(int('12345') + 1000)
# ------想要转成的类型(待转的数据)
# 整型 -->str(字符串)
user = input(':')
print(str(user) + '56789')

'''1_练习'''
# 键盘输入两个数
# 输出和
# 输出差

# one = input('请输入数字:')
# two = input('请输入数字:')

# sc1 = int(one)+int(two)
# sc2 = int(one)-int(two)

# print(sc1)
# print(sc2)


one = input('请输入数字:')
two = input('请输入数字:')
sc1 = float(one) + float(two)
sc2 = float(one) - float(two)
print(sc1)
print(sc2)

#   True转整型是1    转字符串是'True'
#   False转整型是0   转字符串是'False'

flag = True
print(int(flag))

#   只有值为0,或为''时 , 转为bool型是False
a = 5
print(bool(a))
