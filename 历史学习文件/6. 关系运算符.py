"""关系运算符  返回的结果是 : False,True
>  <  =  == != is

"""
a = 10
b = 20

print(a > b)  # =False
print(a < b)  # =True
print(a == b)  # a和b相等么 = False
print(a != b)  # a和b相等么 = True

# 判断字符型可否对比
c = 'abcdefg'
d = 'qwer'
print(c == d)  # c和d相等么 = False
print(c != d)  # c和d相等么 = True
print(c < d)  # 字符型对比的是ASCII码

e = 10
print(a >= e)  # 因为包含等号 , 所以就算True

# 输入考试分数来判断成绩是否在100-80间
fen = float(input('输入成绩'))
print(100 >= fen >= 80)
# 输入两个商品的价格来比较商品价格是否相同
price = float(input('输入商品价格:'))
price1 = float(input('输入商品价格:'))
print(price == price1)
