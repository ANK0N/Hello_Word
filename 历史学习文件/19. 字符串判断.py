"""
理论上 : 所有is开头的都是有关字符串判断的

判断:  startswith  --(判断是否以什么开头的)  {集合名称}.startswith('匹配文本')
      endswith    --(判断是否以什么结尾的)  {集合名称}.endswith('匹配文本')
      isalpha     --(判断是否是纯字母组成的)  {集合名称}.isalpha()
      isdigit     --(判断是否是纯数字组成的)  {集合名称}.isdigit()
      isalnum     --(判断是否是数字和字母组成的)  {集合名称}.isalnum()
      isspace     --(判断是否由纯空格组成)  {集合名称}.isspace()
      isupper     --(判断是否由大写字母组成)  {集合名称}.isupper()
      islower     --(判断是否由小写字母组成)  {集合名称}.islower()
返回值都是布尔类型的 , 为True或者False
"""

s = 'https://codeup.aliyun.com/msy/zhidou.banmahui/erp-interface/commit/dong_26e82ede760929753490e461.gif'
w = 'A123456'
print(s.startswith('https'))
print(s.startswith('ahttps'))
print(w.isalpha())  # 判断是否是纯字母组成的
print(w.isdigit())  # 判断是否是纯数字组成的
w = '                     '
print(w.isspace())  # 判断是否是纯数字组成的

"""
模拟上传,键盘输入模拟文件的名称 , 判断文件名是否大于6位 , 扩展名是否是 jpg , gif ,png
如果不是 , 则提示上传失败
先看后缀  ,再看名字
名字不满足 , 扩展名满足 则随机生成一个六位数字组成的文件名 , 提示上传成功且打印文件名称
"""
'''
name = ''
anko = ''
import random

file = input('请输入需要上传的文件名称')
if (file.endswith('jpg')) or (file.endswith('gif')) or (file.endswith('png')):
    address = file.find('.')
    files = file[:address]
    number = len(files)
    if number <= 6:
        for i in range(6):
            names = random.randint(1, 9)
            name = name + str(names)
        anko = file[address:]
        file = name + anko
        print(file)
        print('上传成功,文件名称不符合规范,已做修改,文件名称是:%s' % file)
    else:
        print('上传成功,文件名称是:%s' % file)
else:
    print('上传失败,格式有误')
'''
# 随机的字母数字组合

import random

nam = ''
s = 'ANGD786GGGADA3454FWADA3178543GGASDSDAWQ79dfbAHUIFLnj999sdhajDWGFRTWDAkbdshdua2321233IO'
for i in range(6):
    strs = random.randint(1, len(s) - 1)
    nam += s[strs]
print(nam)



