import requests
import json

#from bs_opponents import get_opponents
#from bs_select_opponents import get_opponents
from bs_xpath_opponents import get_opponents

response = requests.get('https://en.wikipedia.org/wiki/Khabib_Nurmagomedov')

opponents = get_opponents(response.text)

print(opponents)

opponents_json = json.dumps(opponents)

with open('khabib_opponents.json','w', encoding='utf-8') as f:
    f.write(opponents_json)
