"""
输入名字

您好__欢迎来到
1.查询余额
2.存款
3.取款
4.退出

__________查询余额__________
名字,您好,余额为____

__________存款__________
名字,您好,存款___元成功,剩余余额为

__________取款_________
名字,您好,取款___元成功,剩余余额为

money 全局 : 余额
name  全局 : 名字(开始时输入)

定义如下4个函数
1.查询余额
2.存款
3.取款
4.退出

只有输入名字错误和选择退出才会退出
"""

name = input("请输入姓名:")
money = 50000
def c_money(statu):
    global money
    if statu == '1':
        print("__________  查询余额  __________")
        print(f"{name}您好")
        print(f"您当前的存款为{money}元")
    elif statu == '2':
        print("__________  存款  __________")
        print(f"{name}您好")
        in_money = int(input("请输入您要存款的金额"))
        money += in_money
        print(f"共存款{in_money}元,当前存款为为{money}元")
    elif statu == '3':
        print("__________  取款  __________")
        print(f"{name}您好")
        in_money = int(input("请输入您要取款的金额"))
        if in_money > money:
            print(f"您的存款不足,当前存款余额为 {money} 元")
        else:
            money -= in_money
            print(f"共取款{in_money}元,当前存款为{money}元,请点明金额后再离开")
while 1 == 1:
    if name == 'ANKON':
        print(f"{name}先生,请选择您要办理的业务")
        print("[1] 查询余额\n[2] 存款\n[3] 取款\n[4] 退出")
        status = input(":")
        print(status)
        if status in ("1", "2", "3"):
            c_money(status)
            print("\n")
        else:
            break
    else:
        print("您貌似并不是我行的会员捏~~真是杂鱼呐~")
        break
