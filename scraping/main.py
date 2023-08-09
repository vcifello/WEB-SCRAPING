import requests
import json
import sys

from scraping.wiki_fighters import get_opponents, get_fighter_info, get_opponents_with_info

def default():
    if len(sys.argv) == 1:
        raise Exception("missing argument...")

    target = sys.argv[1]
    url = sys.argv[2]
    output = sys.argv[3]

    handler= None
    if target =='ops':
        handler = get_opponents
    if target =='ops+info':
        handler = get_opponents_with_info
    elif target =="info":
        handler = get_fighter_info

    response = requests.get(url)
    results = handler(response.text)
    #json_payload= json.dumps(results, ensure_ascii=False)
    json_payload= json.dumps(results)

    with open(f'{output}.json','w', encoding='utf-8') as f:
        #f.write(json_payload.encode('ascii', 'ignore').decode("utf-8"))
        f.write(json_payload)
