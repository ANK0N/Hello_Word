"""
逻辑运算符
and  or  not

and : 与  并且 的意思
true and true     --> true
true and false    --> false
false and true    --> false
false and false   --> false

or 或  或者   :适用于两个条件有一个满足就可以了
true and true     --> true
true and false    --> true
false and true    --> true
false and false   --> false

not
not true   ---> false
not false  ---> true

"""
a = 1
b = 3
c = 0
print(a and b)  # and两边都是非0的数字则返回最后的一个数字
print(a and c)  # and两边只要有一边为0(false),结果记为0(false)
print(a < b and b > c)  # 常规的是应用在有两侧判断的情况下
# 应用于 用户名 and 密码  来进行登录

print(' \QAQ/ ' * 200)  # python的*表示多少个

print(a or b)  # or两边是前面满足条件了就直接输出了 , 不看后面
print(c or c)  #
print(a < b or b > c)  # 常规的是应用在有两侧判断的情况下
# 应用于 (账号 or 手机)  密码 来进行登录



