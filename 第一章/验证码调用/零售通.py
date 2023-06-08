import hashlib

my_src = '647563644F60716363677493D5936F1'  # 待解密字符串,后面9位是验证
data = 'lingshoutong'  # 解密秘钥
my_md5 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
my_md5 = my_md5[2:2 + 9].upper()
print(my_md5)
print(my_src[-9:])  # 截取待解密码的后九位

if my_src[-9:] != my_md5:   # 截取待解密码的后九位
    print("传入值异常")

scr_pas = my_src[:-9]  # 后9位之前
src_len = len(scr_pas)  # 长度
my_str = ''
for i in range(0, src_len, 2):
    my_char = int(scr_pas[i:i+2],16) ^ 0x10
    my_str += chr(my_char)
print(my_str)














