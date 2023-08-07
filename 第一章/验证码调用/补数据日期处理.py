from datetime import datetime, timedelta


def get_date_range(start_date_str, end_date_str,date_spar):
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
        date_dict [today] = [yesone_day_1,yesone_day_2]
    return date_dict

print(get_date_range("2023-07-20", "2023-07-25","/"))
