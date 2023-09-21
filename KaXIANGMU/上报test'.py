import requests
url_acc = f'https://admin.pre.banmahui.cn/api/zhidou/access_token'
data = {
    'client_id': '4566450985',
    'client_secret': 'IXNZpHgXbdbCGIff8viMpphntGFEvKPl',
    'grant_type': 'client_credentials',
}
response = requests.post(url_acc, data=data)
access_token = response.json().get('access_token')

url = "https://admin.pre.banmahui.cn/api/zhidou/customer/report/log"
headers = {'Authorization': access_token, 'accept': "application/json"}
data = {
    "login_id": "66",
    "biz_date": "2023-09-02",
    "name": "test_error",
    "describe": "error",
    "status": "1",
    "type": "1"
}
response = requests.post(url, headers=headers, data=data)
print(response)

url = "https://admin.pre.banmahui.cn/api/zhidou/customer/report/log"
headers = {'Authorization': access_token, 'accept': "application/json"}
params = {
    "login_id": '66',
    "biz_date": '2023-09-02',
    "type": '1'
}
response_in = requests.get(url, headers=headers, params=params)
print(response_in.text)



