import requests
Hun_Jig = 'admin.yikuaigao.com'
url = f'https://{Hun_Jig}/api/zhidou/access_token'
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
url_1 = f'https://{Hun_Jig}/api/zhidou/customer/login?id=1'  # 1可以替换
headers = {
    'Authorization': access_token}
response = requests.get(url_1, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print('请求失败，错误码为：', response.status_code)
