"""
使用for循环对等级1的员工增加一个级别并且工资涨1000
"""
dept_dict = {
    '周杰伦': {'部门': '科技部', '工资': 3000, '级别': 1},
    '林俊杰': {'部门': '市场部', '工资': 6000, '级别': 3},
    '王力宏': {'部门': '市场部', '工资': 6000, '级别': 2},
    '米津玄师': {'部门': '市场部', '工资': 5000, '级别': 2},
    '宫本昊次': {'部门': '科技部', '工资': 4000, '级别': 1}}
for i in dept_dict:
    if dept_dict[i]['级别'] == 1:
        dept_dict[i]['工资'] += 1000
        dept_dict[i]['级别'] += 1
for i in dept_dict:
    print(i)
    print(dept_dict[i])
