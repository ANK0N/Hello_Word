# def oper_date(date_num, date_spar):
from datetime import datetime, timedelta
# date_num : 减去多天的天数
# date_spar : 格式化日期的日期分隔符
to_date = datetime.now().date()
to_date_2 = to_date.strftime("%Y%m%d")
for i in range(0, 10):
    yesone_day = to_date - timedelta(days=i)
    print (yesone_day)
# 减去1天
# yesone_day = to_date - timedelta(days=1)
# yesone_day_1 = yesone_day.strftime(f"%Y{date_spar}%m{date_spar}%d")
# yesone_day_2 = yesone_day.strftime("%Y%m%d")
# my_dict = {
#     "昨天": [yesone_day_1, yesone_day_2]
#     ,"前天": [yestwo_day_1, yestwo_day_2]
#     ,"多天": [yestw_day_1, yestw_day_2]
# }
# my_list = [to_date_2, my_dict]
