# import code
# print(code.code_test("C:\\Users\\ANKON\\Desktop\\png_1.png"))

import time
times = "2023-01-01 00:00:00"
print(time.strptime(times, "%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y年%m-%d %H:%M:%S",times))


