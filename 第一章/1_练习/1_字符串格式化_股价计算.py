# 定义需要的变量

name = '传智播客'
stock_price = 19.99  # 当前股价
stock_code = '003032'  # 股票代码
stock_factor = 1.2  # 增长系数
growth_days = 7  # 增长天数

# 计算变化后的股价
stock_money = stock_price*(stock_factor**growth_days)  # 7日后股价


# 按要求打印
print(f"公司:{name} ,股票代码{stock_code} ,当前股价: {stock_price}")  # 用f"{表达式}"
print("每日增长系数是%.1f,经过%d天后 ,股价达到了%.2f" % (stock_factor, growth_days, stock_money))  # 用%表达式

