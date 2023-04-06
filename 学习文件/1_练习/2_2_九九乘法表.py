"""
9*9乘法表
"""

for num_1 in range(1, 10):
    for num_2 in range(1, num_1 + 1):
        print(f"{num_2}*{num_1}={num_1 * num_2}  ", end='')
    print("")

# 在优化后的代码中，使用字符串拼接将每一行的结果先计算完成后再输出，避免了重复计算。这样可以大幅度提高程序的执行效率。
#
# 优化前后的差别是：
#
# 优化前：每次嵌套的循环都要进行一次乘法运算，执行效率较低。
# 优化后：使用字符串拼接将结果先计算完成后再输出，避免了重复计算，提高了执行效率。

for num_3 in range(1, 100):
    row = ''
    for num_4 in range(1, num_3 + 1):
        row += f"{num_4}*{num_3}={num_3 * num_4}  "
    print(row)

nine_1 = 1
nine_2 = 1
bia_1 = ''
while nine_1 <= 9:
    while nine_2 <= nine_1:
        bia_1 += f'{nine_1}*{nine_2}={nine_1*nine_2}\t'
        nine_2 += 1
    nine_1 += 1
