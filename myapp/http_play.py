import urllib.request
import json
import requests


r = urllib.request.urlopen("http://127.0.0.1:8000/api/quest1",)

data = r.read()
encoding = r.info().get_content_charset('utf-8')
s = json.loads(data.decode(encoding))
for i in s.keys():
    print(s[i])
answer = int(input('ваш ответ:'))
name = str(input('введите ваше имя:'))

url = 'http://127.0.0.1:8000/api/quest1'
payload = {'answer': answer, 'name': name}
x = json.dumps(payload)
print(x)
requests.post(url, data=x, verify=False)
