url = 'https://heights.edu/wp-json/heightshelper/v1/faculty'

import requests, json
from pprint import pprint
res = requests.get(url)
res = json.loads(res.content)
res = json.loads(res)

pprint(res)

llist = []
mlist = []
hlist = []

for i in res:
    for l in res[i]['division']:
        if l == 'lower':
            llist.append(i)
        if l == 'middle':
            mlist.append(i)
        if l == 'upper':
            hlist.append(i)

#pprint(llist)
#pprint(mlist)
#pprint(hlist)

hiredListH = []
hiredListL = []

for i in hlist:
    if int(res[i]['hired']) > 2017:
        hiredListH.append(i)
for i in llist:
    if int(res[i]['hired']) > 2017:
        hiredListL.append(i)

pprint(hiredListH)
pprint(hiredListL)
