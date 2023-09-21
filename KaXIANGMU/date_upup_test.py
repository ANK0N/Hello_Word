from datetime import datetime, timedelta


def oper_date():
    to_date = datetime.now().date()  # 当天
    to_date_2 = to_date.strftime("%Y%m")  # 上传日期（年份和月份）
    to_date_3 = to_date.strftime("%d")  # 今日日期
    print(f"当天为{to_date}")
    print(f"上传日期{to_date_2}")
    print(to_date_3)
    to_date_3 = '01'
    if to_date_3 == '01':
        two_months_ago = (to_date - timedelta(days=1)).replace(day=1)
        print(two_months_ago.strftime("%Y%m%d"))
    elif to_date_3 == '15':
        last_month = (to_date - timedelta(days=1)).replace(day=1)
        print(last_month.strftime("%Y%m%d"))


oper_date()