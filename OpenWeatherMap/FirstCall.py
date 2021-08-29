import requests
import json
from os import path

file_path = path.abspath(__file__)
dir_path = path.dirname(file_path)
token_file_path = path.join(dir_path,'OWtoken.txt')

tokenfile = open(token_file_path,'r')
token = tokenfile.read()

r = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat=-43.55&lon=172.63&units=metric&appid={token}')

parsed = json.loads(r.text)

print(json.dumps(parsed,indent=4,sort_keys=True))