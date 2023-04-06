money = 0  # 游戏金币数
num = 0    # 游戏次数
while True:
    if money >= 5:
        money += 1
        import random
        check1 = random.randint(1, 6)
        check2 = random.randint(6, 6)
        check = check1 + check2
        status = str(input('猜大[1]还是猜小[2]:'))
        if (status == '1' and check > 6) or (status == '2' and check < 6):
            money -= 5
            print('猜对啦')
            money += 2
        elif check == 6:
            money -= 5
            print('通吃了')
        else:
            money -= 5
            print('猜错啦')
        num += 1
    else:
        print('游戏币不足请充值')
        prices = input('是否充值?[Y/N]')
        if prices == 'Y':
            while True:
                price = int(input('请输入你充值的金额,需要为10的倍数'))
                run = price % 10
                if run == 0:
                    money += price * 2
                    print('充值成功,谢谢惠顾')
                    break
                else:
                    print('请查看充值要求')
        elif prices == 'N':
            print('没钱出门左转')
        else:
            print('请输入正确的选项')
        print('当前剩余金币%d个' % money)
    doom = input('[N]则退出游戏')
    if doom == 'N':
        break
print('共进行游戏%d次,剩余金币%d个' % (num, money))

