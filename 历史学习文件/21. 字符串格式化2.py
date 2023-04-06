'''
格式化:
format方式 : 优点是变量可以复用
1.可以省略字段名
2.可以将输入的值重复调用 , 通过给花括号取名字
3.使用数字填充 , 用0开始计数
4.要将值放置在括号里才能直接应用变量名 , 要利用变量名参数






'''

name = 'ANKON'
years = '22'
values = '尬殿{}荡了{}次'.format(name, years)
print(values)

name = 'ANKON'
years = '22'
values = '尬殿{0}荡了{1}次,我救了他{1}次'.format(name, years)
print(values)

values = '尬殿{name}荡了{years}次,我救了他{years}次'.format(name='ANKON', years='22')   # 要将值放置在括号里才能直接应用变量名
print(values)


