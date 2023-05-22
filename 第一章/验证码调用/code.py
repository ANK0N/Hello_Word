def code_test(address):
    import test

    test.chaojiying = test.Chaojiying_Client('506036507', '506036507', '948744')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(address, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # print(test.chaojiying.PostPic(im, 9501))  # 1902 验证码类型

    my_dict = test.chaojiying.PostPic(im, 9501)["pic_str"]
    print(my_dict.split("|"))  # 打印列表

    my_list = my_dict.split("|")
    str_of = ''
    for i in my_list:
        str_of += i[0]
    print(f"坐标字符排序 : {str_of}")  # 打印字符

    import requests
    import json

    url = 'http://ml-jsonrpc.banmahui.cn/resolve-chaos-word'
    headers = {'content-type': 'application/json', 'apikey': 'Rahm3xu6Ohng5ohm9Ieth5leeghahD8i'}
    payload = {
        'method': 'resolve_chaos_word',
        'params': [str_of],
        'id': 1,
        'jsonrpc': '2.0'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    result = response.json()

    print(f"排序结果 : {result['result']}")

    str_in = result['result']
    str_yz = ''
    for l in str_in:
        for s in my_list:
            if s[0] == l:
                str_yz += f"{s}|"
    str_yz += "|"
    # print(str_yz)
    str_yz = str_yz.replace("||", "")
    # print(str_yz.split("|"))
    return str_yz.split("|")


if __name__ == '__main__':
    print(code_test("C:\\Users\\ANKON\\Desktop\\png_1.png"))
