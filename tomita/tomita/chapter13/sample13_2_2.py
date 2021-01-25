import requests

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_1_1.html'

response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)