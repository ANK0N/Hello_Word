"""
函数 : open(name,mode,encoding)
name: 打开的目标文件名的在字符串(也可以包含文件的具体路径,不写路径则是当前项目的所在文件位置)
mode: 打开文件的格式(访问模式):只读,写入,追加等等
r 只读 以只读模式打开,指针在开头
w 写入 打开一个文件重头编辑,原有内容被删除,如果文件不存在则创建文件并写入
a 追加 追加的内容会在原有内容后面写入,如果文件不存在则创建文件并写入
"""
# 文件目标.write()
# f.flush() 将修改后的内容写入到硬盘中去
"""
1. 打开
f = open('D:/ankon文件下载位置/txt_test.txt', 'r', encoding='utf-8')

2. 文件写入
f.write("hello_word")

3. 写入硬盘
f.flush()
"""
f = open('D:/ankon文件下载位置/ankon.txt', 'w', encoding='utf-8')
f.write("hello_word")  # 数据依旧保存在了内存中
f.flush()  # 文件已经出现,且数据被写入硬盘中
f.close()  # close也是内置了flush功能的

print("________追加___________")
# 追加模式会在光标后追加写入
f = open('D:/ankon文件下载位置/ankon.txt', 'a', encoding='utf-8')
f.write("hello_word\n")
f.flush()
f.close()
