import requests
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
    print (response.json()['data']['user'], response.json()['data']['password'], response.json()['data']['ossPath'])
else:
    print('请求失败，错误码为：', response.status_code)