import my_utils.str_util  # 调用时必须写全

print(my_utils.str_util.str_reverse("123456789"))

from my_utils.file_util import *

print_file_info("D:/ankon文件下载位置/旧版本拉取到的语句.txt")
append_to_file("D:/ankon文件下载位置/旧版本拉取到的语句.txt", "12345的蛤UI的哈无敌")
