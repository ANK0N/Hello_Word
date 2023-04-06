# 1.查询年龄下标
# 2.查询姓名
# 3.删除爱好D2
# 4,增加爱好APEX

t1 = ("ANKON", 22, ["D2", "music"])
print(f"年龄的下标为 {t1.index(22)}")
print(f"学生的姓名是{t1[0]}")
# 删除D2 __我觉得先查找位置再删除很合理
del t1[2][t1[2].index("D2")]
print(f"删除后的元组值为{t1}")
t1[2].append("APEX")
t1[2].insert(0, "APEX")
print(f"当前列表中的值为 : {t1}")
