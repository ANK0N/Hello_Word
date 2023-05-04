# 1.布尔类型和比较运算符
"""
布尔(bool) 类型 :true 1 | false 0

== 相等
!= 不等
>
<
>=
<=
"""
# 定义变量赋值布尔类型
result = 10 > 5
print(result)  # True
typ_1 = bool(0)
print(typ_1)  # False

bool_1 = True
bool_2 = False
print(f"""{bool_1}__{bool_2}
{type(bool_1)}{type(bool_2)}""")

# 比较运算符
bool_1 = 1
bool_2 = 10
print(bool_1 == bool_2)  # False
print(bool_1 != bool_2)  # True
print(bool_1 > bool_2)  # False
print(bool_1 < bool_2)  # True

print('_______________逻辑判断 if________________')

age = 20

if age > 18:
    print('让我访问!!!!!')
elif age == 18:
    print('刚18岁就来????')
else:
    print('形不成型,意不在意,再回去练一下吧')


print('_______________if 嵌套________________')
age = 20
money = 648

if age > 18:
    print('让我访问!!!!!')
    if money >= 648:
        print('我焯嫩牛娃')
    else:
        print('gui!!!!!!!!!')
elif age == 18:
    print('刚18岁就来????')
else:
    print('形不成型,意不在意,再回去练一下吧')
























