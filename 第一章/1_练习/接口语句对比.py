old_edition = open('D:/ankon文件下载位置/旧版本拉取到的语句.txt', 'r', encoding='utf-8')
new_edition = open('D:/ankon文件下载位置/新版本拉取到的语句.txt', 'r', encoding='utf-8')
print(old_edition.read())
print(new_edition.read())
old_edition = open('D:/ankon文件下载位置/旧版本拉取到的语句.txt', 'r', encoding='utf-8')
new_edition = open('D:/ankon文件下载位置/新版本拉取到的语句.txt', 'r', encoding='utf-8')
old_dict = old_edition.read()
new_dict = new_edition.read()
if old_edition.read() == new_edition.read():
    print("相同")
else:
    print("不中")
old_edition.close()
new_edition.close()

