import urllib.request

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_1_1.html'

with urllib.request.urlopen(url) as conn:
    data = conn.read()
    text = data.decode('utf-8')
    print(text)