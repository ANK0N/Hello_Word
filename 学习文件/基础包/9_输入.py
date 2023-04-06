"""
数据输出 : print
数据输入 : input



"""
print('你是谁 ?')
name = input()
print('你是%s' % name)


print('------或者------')

name = input('你是谁 ? :')
print('你是%s' % name)

num = input('数字测试')   # input默认接收类型都是字符串 , 如需要其他类型需要自行转换
print(type(num))
print(type(int(num)))


name = input("您的用户名 :")
vi_type = 'SSSSSSSSSSVIP'
print("""
欢迎您 %s
您是尊贵的%s会员
""" % (name, vi_type))
