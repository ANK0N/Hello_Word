import requests
import json

url = 'http://ml-jsonrpc.banmahui.cn/resolve-chaos-word'
headers = {'content-type': 'application/json', 'apikey': 'Rahm3xu6Ohng5ohm9Ieth5leeghahD8i'}
payload = {
    'method': 'resolve_chaos_word',
    'params': ['成科果研'],
    'id': 1,
    'jsonrpc': '2.0'
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
result = response.json()

print(result['result'])
