import requests
import hashlib

url = f'https://admin.pre.banmahui.cn/api/zhidou/access_token'
data = {
    'client_id': '4566450985',
    'client_secret': 'IXNZpHgXbdbCGIff8viMpphntGFEvKPl',
    'grant_type': 'client_credentials',
}
response = requests.post(url, data=data)
if response.status_code == 200:
    access_token = response.json().get('access_token')
    url_1 = f'https://admin.pre.banmahui.cn/api/zhidou/customer/report/log'
    headers = {'Authorization': access_token}
    response_in = requests.get(url_1, headers=headers)
    print(response_in.json())
