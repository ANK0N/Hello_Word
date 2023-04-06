"""
切片 :字符串,列表
格式 :字符串变量[start:end]
字符串变量[start:end:step]  还可以加步长
# 如果步长是负数 , 就注定走动方向是向左走

"""

s = 'ABCDEFG'
print(s[1:4])  # 为什么是4  :结果和range一样,左闭右开,包前不包后
print(s[0:5])
"开始为0 可以默认写成"
print(s[:5])  # 从0开始到5
print(s[-3:-1])
"要是截取到最后 , 后面可以不写"
print(s[-3:])  # 从-3开始到结尾
# 两套规则是可以共同的
print(s[-3:7])
print(s[:])  # 代表从头到尾
x = s[:]
y = s[-3:7]
print(id(x))
print(id(s))
# 不要两头 只要中间
print(s[1:-1])

# 要取BDF
print(s[1::2])
print(s[::-1])
print(s[::-2])
