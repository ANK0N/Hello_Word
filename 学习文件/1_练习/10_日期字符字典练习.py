my_str = "1-31,3-14,3-16,3-19,3-18,3-25,3-23,3-21,3-29,11-30,3-27"
my_list = my_str.split(",")
for i in range(0, len(my_list)):
    my_list2 = my_list[i].split("-")

    day = int(my_list2[1])+1
    month = int(my_list2[0])
    if month in (1,3,5,7,8,10,12) and day > 31:
        day -= 31
        month += 1
    elif month in (4,6,9,11) and day > 30:
        day -= 30
        month += 1
    elif month == 2 and day > 28:
        day -= 28
        month += 1
    if len(str(day)) == 1:
        day = "0"+str(day)
    if len(str(month)) == 1:
        month = "0"+str(month)
    print(f"2023-{month}-{day}")
