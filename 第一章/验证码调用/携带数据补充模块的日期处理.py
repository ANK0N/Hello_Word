def oper_date(date_list):
    date_list = list(date_list)
    from datetime import datetime, timedelta

    # 需要补数据时,当日数据不介入
    if len(date_list) == 0:
        to_date = datetime.now().date().strftime("%Y-%m-%d")
        date_list.append(to_date)
    # 获取当日时间,追加到全部日期列表
    date_dict = {}
    for i in date_list:
        i_date = datetime.strptime(i, '%Y%m%d')
        i_date_str = i_date.strftime(f"%Y%m%d")
        # 获取昨日日期
        yesone_day_base = i_date - timedelta(days=1)
        yesone_day = yesone_day_base.strftime(f"%Y-%m-%d")
        yesone_day_ymd = yesone_day_base.strftime("%Y%m%d")
        date_dict[i_date_str] = [yesone_day, yesone_day_ymd]
    my_date_list = [datetime.now().date().strftime("%Y%m%d"), date_dict]
    return my_date_list


my_list = ["2023-07-01", "2023-07-02", "2023-07-11", "2023-07-30"]
print(oper_date(my_list))
