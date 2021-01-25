import datetime
import os
import sys
import requests
from bs4 import BeautifulSoup

today = datetime.date.today()
create_dir_name = today.strftime('%Y%m%d')

if not os.path.exists(create_dir_name):
    os.mkdir(create_dir_name)

else:
    print('すでにディレクトリは存在します。終了します')
    sys.exit()

url = 'https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html'
print('StartPage:' + url)

def linkget(url,depth=0):

    indent =' ' * depth
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    for a_tag in soup.find_all('a'):

            text = a_tag.string
            href = a_tag.get('href')
            html = str(href)

            file_name = html.split('/')[-1]
            fullpath = os.path.join(create_dir_name, file_name)

            with open(fullpath, 'w', encoding='utf-8', newline='') as f:
                        f.write(response.text)

            print(indent + ' {}: {}'.format(text, href))
            linkget(href, depth + 1)


linkget(url)