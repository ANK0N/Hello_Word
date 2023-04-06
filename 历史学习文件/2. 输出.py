money = 28  # 声明了一个money的变量,赋值为28
type(money)  # 变量的数据类型
print(money)  # 打印,只负责输出结果
print(type(money))  # 返回了 '<class 'int'>'

money = 28.1233444213
print(type(money))  # 返回了 <class 'float'>  届时会是浮点型了

money = '一万'  # 赋值为字符串
print(type(money))  # 返回了 <class 'str'>  届时是字符串类型

# 其实只要是在引号中的就是字符串 , 其中当'''''' 三引号用在赋值后也可以当做常规引号组使用
# 三引号保留格式输出

ankon = "item_info= '8001010'"
print(ankon)



# 布尔类型 : True False  只有这两个关键字才是布尔类型
# 主要用于开发中的判断,比如:是否登录成功

isLogin = True  # 真
print(isLogin)
isLogin = False  # 假
print(isLogin)

yihao = '就打我'
erhao = '带我打非人防发热个人股'

print (yihao+erhao)
