# 字符串
s1 = 'hello'
s2 = s1
s3 = 'hello'
s4 = 'hello1'
# print(s1, s2, s3)
# print(id(s1))
# print(id(s2))
# print(id(s3))
# is
# print(s1 is s2)  # 比较的是字符串地址是否相同
# print(s1 is s4)

# 字符串获取(截取)内部的字符
s1 = 'ABCDEFGHIJKLMN'
# 字符串的位置是从0开始的 , A 为 0 ,B 为 1
# index 就是代表索引
# 索引的机制 正向取值是从0开始
#          负向取值是从-1开始
# len(字符串)  可以获取字符串长度
# -len(字符串) 可以付的取值
"""字符串的组成"""
print(s1[4])
