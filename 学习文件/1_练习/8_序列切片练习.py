"""
将字符串"之趋避福祸因岂,以死生家国利苟"中的 祸福避趋 取出来
"""
my_str = "之趋避福祸因岂,以死生家国利苟"
# 1
my_str1 = my_str[::-1]
my_list = my_str1.split(",")
my_str1 = my_list[1]
my_str2 = my_list[1]
print(my_str1)  # 岂因祸福避趋之

# 分组后替换掉不用的
my_str1 = my_str1.replace("岂因", "").replace("之", "")
print(my_str1)

# 切片取出
my_str2 = my_str2[2:6]
print(my_str2)

# --------------------------------------------------------------
my_str = "之趋避福祸因岂,以死生家国利苟"
print(my_str[::-1][10:14])
print(my_str[1:5][::-1])

