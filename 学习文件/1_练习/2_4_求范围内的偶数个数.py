# 1_练习 : 反馈输入值范围中的偶数个数
s_num = int(input("输入开始值:"))
e_num = int(input("输入结束值:"))
e_num += 1
num = 0
for i in range(s_num, e_num):
    if i % 2 == 0:
        num += 1
print(num)


