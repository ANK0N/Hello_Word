"""
字符串相关模块
"""

__all__ = ['str_reverse']


def str_reverse(my_str):
    """
    :param my_str: 传入的字符串
    :return: 反转后的字符串
    """
    my_str = my_str[::-1]
    return my_str


def substr(s, x, y):
    """
    :param s: 窜入字符串
    :param x: 起始下标位置
    :param y: 结束下标位置
    :return: 截取内容
    """
    s_str = s[x:y]
    return s_str


if __name__ == '__main__':  # 对函数的测试
    print(str_reverse('123456789'))
    print(substr('123456789', 1, 3))
