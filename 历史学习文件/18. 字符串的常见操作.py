# len(字符串)可以获取字符串长度
path = 'https://codeup.aliyun.com/msy/zhidou.banmahui/erp-interface/commit/dong_26e82ede760929753490e461.gif'
# find, index , rfind , rindex
"""
find  : 从左往右找到符合条件的第一个条件的位置 , 如果找不到符合要求的 , 则返回 '-1'
rfind : 从右往左找到符合条件的第一个条件的位置 , 如果找不到符合要求的 , 则返回 '-1'
count : 统计指定字符的个数
index : 和find一致, 但是找不到会报错
rindex: 和rfind一致, 但是找不到会报错
"""
i = path.find('_')  # 去字符串里寻找包含'_'的位置
name = path[i + 1:]
print(name)

# 想拿到图片的拓展名
i = path.rfind('.')  # 去字符串里反向寻找包含'.'的位置
name = path[i:]
print(name)
# 计算 j 中 '.' 出现的次数
number = 0
j = '1.1.1.1.1.1'
while True:
    i = j.find('.')
    j = j[i+1:]
    if i == -1:
        print('没有了')
        break
    else:
        number += 1
print(number)
j = '1.1.1.1.1.1'
n = j.count('.')
print(n)


