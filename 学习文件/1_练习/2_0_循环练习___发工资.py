"""
公司账户1W元
给编号1-20的员工发工资
按照绩效分发(1-10)随机生成 ,低于5的不发
如果分发结束则结束发工资

"""
import random

money = 10000
for i in range(1, 21):
    num = int(random.randint(1, 10))
    # print(f"当前员工编号为{i},他的绩效为{num}")
    if money > 0:
        if num >= 5:
            money -= 1000
            print("员工%s,绩效为%s,发放工资1000元,剩余资金%d元" % (i, num, money))
        else:
            print(f"员工{i},绩效为{num},低于5,不发工资,下一位")
    else:
        print(f"是工资发完了,下月再来吧,发到了员工{i}")
        break
if money > 0:
    print(f"剩余资金{money}元")
