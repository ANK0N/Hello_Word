"""
定义一个字符串
统计再付款中的"it"的个数
将字符串中的空格替换成"|"
按照"|"将字符串分割成列表
"""
my_str = "itwuhu ithebei itbeijing itzbc"
print(f"字符串{my_str}中'it'的个数为{my_str.count('it')}个")
my_str1 = my_str.replace(" ", "|")
print(f"空格被替换后的字符串为{my_str1}")
my_list = my_str1.split("|")
print(f"根据|分割成的列表为{my_list}")