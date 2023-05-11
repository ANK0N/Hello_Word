"""
增加一个品牌,来拼接出文件地址

"""
# 导入参考表
from pandas import *
from pandas.core.methods.to_dict import to_dict

df = read_excel('D:\\ankon文件下载位置\\工作簿1.xlsx', sheet_name='Sheet1')
my_dict = to_dict(df.head(600))

import os

# 生成文件和文件位置的对照字典 i 是别名 , my_dict[i] 是地址
my_dict1 = {}
for root, dirs, files in os.walk('D:\\ankon文件下载位置\\statement'):
    for d in dirs:
        address = os.path.join(root, d)
        my_count = address.count("\\")
        if my_count == 4:
            my_list = address.split("\\")
            my_dict1[my_list[4]] = address

import shutil
for i in my_dict1:  # 遍历位置表,比较别名来确定文件去往的位置
    w = 0
    while w < 592:
        addresss = my_dict['别名'][w]
        erp_interface_id = my_dict['接口编号'][w]
        if i == addresss:
            src = f"D:\\ankon文件下载位置\\erp_interface\\{erp_interface_id}.yaml"
            dst = f"{my_dict1[i]}\\{erp_interface_id}.yaml"
            print(src)
            print(dst)
            shutil.copy(src, dst)
        w += 1

