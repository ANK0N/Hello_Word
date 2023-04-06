"""
for(.....){
循环体
}

格式
for i in range(n):
    循环体中的内容


特殊函数 range(start,end,step)
start : 开始值
end : 结束值(但不包含结束值)
step : 循环相加的步长



"""
# 1-10 的数字打印   range(n) n的表示从0开始到(n-1)结束
# range(10) 是默认从0开始到n-1的
# range(start,end)  从start开始到end-1结束  (包前不包后)
for i in range(11):
    print(i)

print('*' * 50)
# 从初始值开始
for i in range(1, 10):
    print(i)
print('*' * 50)
# range的第三个参数
# 第三个参数是i循环的步长
for i in range(1, 10, 2):
    print(i)

'''1-50的累加和'''
number = 0
for i in range(1, 51):
    number += i
print(number)

'''输入应户名和密码,最多输入三次 , 账号3次都登陆不成功 , 提示账号被锁定'''
zh = '18830771910'
mm = '506036507'
for i in range(3):
    izh = str(input('输入账号:'))
    imm = str(input('输入密码:'))
    if i == 2:
        print('账号被锁定')
    else:
        if zh == izh and mm == imm:
            print('登陆成功')
            break
        else:
            print('登陆失败')
'''for i in 也是存在else的 , 是在整个循环体结束后触发else,
但是当循环被break跳出了 , 则不会执行
'''

number = 1
while number < 10:
    print(number)
    number += 1
    if number <= 3:
        print('小于等于3')
    elif number == 5:
        print('==5将被退出')
        # break
else:
    print('while循环被跳出了')

'''while 也是存在else的 , 是在整个循环体结束后触发else,
但是当循环被break跳出了 , 则不会执行
'''
