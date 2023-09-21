from datetime import datetime, timedelta


def get_date_range(date_list,date_spar):
    to_date = datetime.now().date()
    for date_num in date_list:

    # 将传入的日期字符串转换为日期对象
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    # 初始化一个空列表来存储日期范围
    date_list = []
    date_dict = {}
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    print(date_list)
    for i in date_list:
        date_date = datetime.strptime(i, '%Y-%m-%d')
        today = date_date.strftime("%Y%m%d")
        yesone_day = date_date - timedelta(days=1)
        yesone_day_1 = yesone_day.strftime(f"%Y%m%d")
        yesone_day_2 = yesone_day.strftime(f"%Y{date_spar}%m{date_spar}%d")
        # yesone_day_2 = yesone_day.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
        date_dict [today] = [yesone_day_1,yesone_day_2]
    return date_dict