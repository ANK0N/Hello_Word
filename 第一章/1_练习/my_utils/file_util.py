"""
文件相关
"""


def print_file_info(file_name):
    """
    :param file_name: 传入的文件位置
    :return: 无任何输出
    """
    try:
        my_file = open(str(file_name), 'r', encoding='utf-8')
        print(my_file.read())
        my_file.close()
    except Exception as lo_exc:
        print("文件不存在")


def append_to_file(file_name, data):
    """
    :param file_name: 文件位置
    :param data: 追加内容
    :return:
    """
    my_file = open(str(file_name), 'a', encoding='utf-8')
    my_file.write(data)
    my_file.flush()
    my_file.close()


if __name__ == '__main__':
    print_file_info("D:/ankon文件下载位置/旧版本拉取到的语句.txt")
    append_to_file("D:/ankon文件下载位置/旧版本拉取到的语句.txt", "12345的蛤UI的哈无敌")
