"""

主要是利用百分号的符号进行占位 , 然后在后面补充参数

格式符号 :
%%      输出%号
%s      字符串
%d      有符号十进制整数
%f      浮点数
%c      字符
%u      无符号十进制整数
%o      八进制整数
%x      十六进制整数(小写字母0x)
%X      十六进制整数(大写字母0X)
%e      科学计数法(小写的e)
%E      科学计数法(大写的E)
%g      %f和%e的简写
%G      %f和%E的简写
"""

# 苟利国家生死以, 岂因祸福避趋之

use = '苟利'
use1 = '生死以'
use2 = '祸福'
print('%s国家%s,岂因%s避趋之' % (use, use1, use2))

name = '王新越'
years = 23
print('我叫%s我今年%d岁了' % (name, years))

money = 12999.93
print('我叫%s我今年%d岁,月薪%f' % (name, years, money))
print('我叫%s我今年%s岁,月薪%s' % (name, years, money))
print('我叫%s我今年%d岁,月薪%.2f' % (name, years, money))  # .2f代表了浮点型的小数点后几位
