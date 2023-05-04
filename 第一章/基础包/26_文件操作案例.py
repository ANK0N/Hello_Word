"""
函数 : open(name,mode,encoding)
name: 打开的目标文件名的在字符串(也可以包含文件的具体路径,不写路径则是当前项目的所在文件位置)
mode: 打开文件的格式(访问模式):只读,写入,追加等等
r 只读 以只读模式打开,指针在开头
w 写入 打开一个文件重头编辑,原有内容被删除,如果文件不存在则创建文件并写入
a 追加 追加的内容会在原有内容后面写入,如果文件不存在则创建文件并写入
"""
# 由于无文件 ,只记录思路
# 表结构
# 名称 , 时间 , 金额 , 消费形式 , 正式/测试
"""
1. 读取文件
2. 将文件写入到bull.txt.bak
3. 将与文件内的状态为 "测试" 的数据丢弃
"""
my_file = open("/第一章/1_练习/bull_python.txt", "r", encoding='utf-8')  # 读取文件
create_file = open('D:/ankon文件下载位置/bull_python.txt.bak', 'a', encoding='utf-8')  # 新建接收文件,且是追加模式
for my_txt in my_file:
    my_txt = my_txt.replace('"', '').strip().split(" ")
    if my_txt[0] != "name":  # 可以直接使用满足条件跳过步骤的循环,使循环跳过不符合条件的项默认执行写入操作
        if my_txt[5] == "正式":
            print(my_txt)
            create_file.write(str(my_txt).replace("[", "").replace("]", "").replace("'", "").replace(",", " ") + "\n")
    elif my_txt[0] == "name":
        print(my_txt)
        create_file.write(str(my_txt).replace("[", "").replace("]", "").replace("'", "").replace(",", " ") + "\n") # \n可以不用拼接,直接write写入也可以
create_file.close()
my_file.close()
