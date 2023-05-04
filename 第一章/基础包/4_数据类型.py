"""
string  字符串类型 __ 引号引起来的数据都是字符串
int     整数型    __ 数字类型 , 存放整数
float   浮点型    __ 数字类型 , 存放小数

通过 type (被查看数据) 来产看数据的类型

"""
# 可以直接用type查询 , 也可以将查询值赋值给变量来进行打印

tpa = type('芜湖')
print(tpa)
tpa = type(1234)
print(tpa)
tpa = type(123213125.1221)
print(tpa)

"""
    数据类型转换
    
1. int(x)   转为整数
2. float(x) 转为浮点
3. str(x)   转为字符
"""
# 万物皆可转为字符串

# 整数型转字符型
num_str = str(11)
print(num_str, type(num_str))
# 字符型转浮点型
num_int = float('11.123')
print(num_int, type(num_int))
# 字符型转整型
num_float = int('11')
print(num_float, type(num_float))


# 整数型转浮点型
num_int_float = float(11)
print(num_int_float, type(num_int_float))
# 浮点型转整数时会去掉小数 , 导致丢失精度
num_int_float = int(11.111111)
print(num_int_float, type(num_int_float))
