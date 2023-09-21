def oper_date(date_spar):
    """
    :param date_spar: 时间分隔符
    :return: 与当日差值3,7,30天的日期
    """
    from datetime import datetime, timedelta

    to_date = datetime.now().date()
    today = to_date.strftime("%Y%m%d")
    date_num = ['3', '7', '30']
    date_dict = {}
    date_list = []
    for da_nm in date_num:
        yes_day = to_date - timedelta(days=int(da_nm))
        yes_day_1 = yes_day.strftime(f"%Y%m%d")
        yes_day_2 = yes_day.strftime(f"%Y{date_spar}%m{date_spar}%d")
        date_list.append([yes_day_1, yes_day_2])
    date_dict[today] = date_list
    return date_dict


