"""
用户名 'ANKON'--或者--账号   '123456789'

密码 : 009230

用户名 全部小写,首字母不能为数字 , 长度大于6
手机号 纯数字 长度11
密码必须是六位数字

其中 , 若是账号,用户名输入错误 , 应该提示输入错误并且重新输入



以上符合则进入下层验证
用户名和密码是否正确
正确则成功 , 否则登陆失败

"""
name = input('用户名/手机号码:')
if (name.isdigit() and len(name) == 11) or name[0].isalpha and name.islower():
    while True:

        password = str(input('密码:'))
        if password.isdigit() and len(password) == 8:
            if (name == 'ANKON' or name == '12345678910') and password == '09231216':
                print('登陆成功')
                break
            else:
                print('登陆失败 , 请重新输入')
        else:
            print('输入的密码不符合条件')
            continue
else:
    print('输入用户名/手机号码错误')
