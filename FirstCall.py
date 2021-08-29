import requests
import json

r = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=-43.55&lon=172.63&units=metric&appid=c6c81eeeb20fa8a564cc6f7edf295fa5')

parsed = json.loads(r.text)

print(json.dumps(parsed,indent=4,sort_keys=True))


#-43.55, 172.63