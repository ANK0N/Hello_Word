# 1-10,通过遍历将偶数搞出来放到一个列表里,使用while和for各来一遍
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = []
status = 0
while status < len(num_list):
    if num_list[status] % 2 == 0:
        num.append(num_list[status])
    status += 1
print(num)

num = []
for i in num_list:
    if i % 2 == 0:
        num.append(i)
print(num)
