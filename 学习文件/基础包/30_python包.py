"""
包其实就指的是一个文件夹,本质上也是一个模块
在文件夹内有一个__init__.py的文件  有这个文件才能属于是包

这个文件中也可以同模块一样配置__all__ = [模块名]
来控制调用的时候允许被导入的模块列表
"""
# 其中的调用语法是  import 包名.模块名
import test_package.mode_test

test_package.mode_test.test(1, 3)
