import requests
import hashlib


# 解码函数
def decrypt(up_str, up_key):
    data = up_key
    AKO_md5 = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    AKO_md5 = AKO_md5[2:2 + 9].upper()
    if up_str[-9:] != AKO_md5:
        print("")
    scr_pas = up_str[:-9]
    src_len = len(scr_pas)
    AKO_str = ''
    for i in range(0, src_len, 2):
        AKO_char = int(scr_pas[i:i + 2], 16) ^ 0x10
        AKO_str += chr(AKO_char)
    return AKO_str


# 接口函数
def up_defd(up_key, Client_ID, Client_Secret, url_add, url_id):
    # 获取access_token
    url = f'https://{url_add}/api/zhidou/access_token'
    data = {
        'client_id': Client_ID,
        'client_secret': Client_Secret,
        'grant_type': 'client_credentials',
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        # 利用接口对access_token进行解析,其中ID可控
        url_1 = f'https://{url_add}/api/zhidou/customer/login?id={url_id}'
        headers = {'Authorization': access_token}
        response_in = requests.get(url_1, headers=headers)

        if response_in.status_code == 200:  # 获取结果未出错
            if response_in.json()['code'] != 0:  # 结果中无登录信息不存在的异常
                # 调用解密函数
                my_user = decrypt(response_in.json()['data']['user'], up_key)
                my_password = decrypt(response_in.json()['data']['password'], up_key)
                my_oss = response_in.json()['data']['ossPath']
                return my_user, my_password, my_oss
    # 多种异常返回,注意判断内容是否含有 Error
            else:
                return 'Error:登录信息不存在,请检查ID'  # 末层异常,登录信息不存在,请检查ID
        else:
            return 'Error:', response_in.status_code  # 内层异常,加密信息获取失败
    else:
        return 'Error:', response.status_code, response.json()  # 外层异常,解密内容获取失败
