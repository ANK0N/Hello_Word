# 1 编码  -->  各种各样的编码格式,值得是翻译规则
# 常见的 : GBK,UTF-8,Big5.......

# 打开读取关闭 文件
"""
函数 : open(name,mode,encoding)
name: 打开的目标文件名的在字符串(也可以包含文件的具体路径,不写路径则是当前项目的所在文件位置)

mode: 打开文件的格式(访问模式):只读,写入,追加等等
r 只读 以只读模式打开,指针在开头
w 写入 打开一个文件重头编辑,原有内容被删除,如果文件不存在则创建文件并写入
a 追加 追加的内容会在原有内容后面写入,如果文件不存在则创建文件并写入

encoding: 编码格式

"""

# 打开文件
f = open('D:/ankon文件下载位置/txt_test.txt', 'r', encoding='utf-8')  # 获取了打开文件的实例
print(type(f))  # <class '_io.TextIOWrapper'>类型--对文本文件进行IO操作的类

print("_________________read_________________")
# read()方法 文件对象.read(num)  num=文件中读取的数据长度,不写则是读取全部
print(f.read(6))

"""
如果连续读取两次,第二次读取会从上一次读取的后面读取
因为指针已经移动
"""

print("_________________readlines_________________")
# readlines()方法 文件对象.readlines() 可以按照行的方式把整个文件进行一次性读取,返回一个列表,每行就是列表中的一个元素
f = open('D:/ankon文件下载位置/txt_test.txt', 'r', encoding='utf-8')  # 获取了打开文件的实例
print(f.readlines()[0])  # 返回了"ANKON"

print("_________________readline_________________")
# readline() 文件对象.readline() 一次只读取一行的内容
f = open('D:/ankon文件下载位置/txt_test.txt', 'r', encoding='utf-8')  # 获取了打开文件的实例
print(f"第一行数据是,{f.readline()}")
print(f"第二行数据是,{f.readline()}")
print(f"第三行数据是,{f.readline()}")

print("_________________for循环遍历_________________")
# 也可以使用for循环来遍历变量
txt = open('D:/ankon文件下载位置/txt_test.txt', 'r', encoding='utf-8')  # 获取了打开文件的实例
for i in txt:
    print(f"每一行数据是,{i}")

print("_________________关闭文件_________________")
# 因为如果文件还在占用使用时,源文件是被占用的,所以需要释放他
# 文件对象.close() 来关闭文件
txt.close()

print("_________________with open_________________")
# 语法 with open(路径,打开格式) as 文件对象名:
# 在调用文件结束后,会自动释放关闭文件

with open('D:/ankon文件下载位置/txt_test.txt', 'r', encoding='UTF-8') as txt:
    print(f"第一行数据是,{txt.readline()}")

"""
课后练习的方法,读取后直接遍历,然后利用字符串函数count()统计指定文本的次数
要记住通过列表读取后会存在\n这个玩意需要替换掉或者strip自动去两头
            直接读取全部文本然后count()计数
"""