import requests
import hashlib


# 解码函数
def decrypt(up_str, up_key):
    data = up_key
    AKO_md5 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    AKO_md5 = AKO_md5[2:2 + 9].upper()
    if up_str[-9:] != AKO_md5:
        print("传入值异常")
    scr_pas = up_str[:-9]
    src_len = len(scr_pas)
    AKO_str = ''
    for i in range(0, src_len, 2):
        AKO_char = int(scr_pas[i:i + 2], 16) ^ 0x10
        AKO_str += chr(AKO_char)
    return AKO_str


# 接口函数
def main(up_key):
    url = 'https://admin.yikuaigao.com/api/zhidou/access_token'
    data = {
        'client_id': '5320410763',
        'client_secret': 'XIdrjd0e3bzBrIe\/1xyDJpFYUoQPm2lB',
        'grant_type': 'client_credentials',
    }
    response = requests.post(url, data=data)
    access_token = ''
    if response.status_code == 200:
        access_token = response.json().get('access_token')
    else:
        print('Error:', response.status_code, response.json())
    url_1 = 'https://admin.yikuaigao.com/api/zhidou/customer/login?id=1'
    headers = {
        'Authorization': access_token}
    response = requests.get(url_1, headers=headers)
    if response.status_code == 200:
        print(response.json()['data'])
    else:
        print('请求失败，错误码为：', response.status_code)
    my_user = decrypt(response.json()['data']['user'], up_key)
    my_password = decrypt(response.json()['data']['password'], up_key)
    my_oss = response.json()['data']['ossPath']
    return my_user, my_password, my_oss
