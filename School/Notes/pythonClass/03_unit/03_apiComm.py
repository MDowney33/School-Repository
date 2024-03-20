
#use requests module to pull data from api

url = 'https://api.openligadb.de/getavailableleagues'


# to make GET request using requests module, import it first

import requests, json
from pprint import pprint

#get lets us perfor requests

res = requests.get(url)
res = json.loads(res.content)
allLeagues = []
for i in res:
    allLeagues.append(i['leagueName'].lower())
allLeagues.sort()

ourLeague = "1. Rollhockey Bundesliga Herren"
for i in res:
    if i['leagueName'].lower() == ourLeague.lower():
        leagueShortcut = i['leagueShortcut']
        leagueSeason = i['leagueSeason']

# api.openligadb.de/inde,.html

url = f'https://api.openligadb.de/getmatchdata/{leagueShortcut}/{leagueSeason}'

res = requests.get(url)

res = json.loads(res.content)
pprint(res)
