import requests
from bs4 import BeautifulSoup
import json


response = requests.get('https://en.wikipedia.org/wiki/Khabib_Nurmagomedov')
print(response.status_code) 

soup = BeautifulSoup(response.text, 'html.parser')

print (soup.title.string)

tables = soup.find_all("table", attrs={'class': "wikitable"})
matches =tables[1]
trs = matches.find_all("tr")

opponents = []

for tr in trs:
    tds = tr.find_all("td")
    if not tds:
        continue

    opponents_node = tds[2]
    opponent_name = opponents_node.string
    if opponent_name is None:
        opponent_name = opponents_node.a.string

    opponents.append(opponent_name.strip('\n'))

print(opponents)
opponents_json = json.dumps(opponents)
print(opponents_json)

#print(trs)
#print(len(tables))


with open('khabib_opponents.json','w', encoding='utf-8') as f:
    f.write(opponents_json)
