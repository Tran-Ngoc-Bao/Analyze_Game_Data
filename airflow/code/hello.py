# import requests
# from bs4 import BeautifulSoup

# a = requests.get("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi")
# t = a.text
# soup = BeautifulSoup(t, "html.parser")
# l = soup.find_all('a')
# sum = 0
# for i in l:
#     if i['href'].find('/vn/app/') != -1:
#         print(i['href'])

from hdfs import InsecureClient
client = InsecureClient('hdfs://namenode:9000', user='root')

from json import dump, dumps
records = [
  {'name': 'foo', 'weight': 1},
  {'name': 'bar', 'weight': 2},
]

# As a context manager:
with client.write('records.jsonl', encoding='utf-8') as writer:
  dump(records, writer)