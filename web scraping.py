import requests
from bs4 import BeautifulSoup

res = requests.get('http://127.0.0.1:8000/home/')

soup = BeautifulSoup(res.content, 'html.parser')

s = soup.find('div', class_='activities')
for data in s:
    print(data)