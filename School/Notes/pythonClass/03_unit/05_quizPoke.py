import requests,json,random
from pprint import pprint

url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'

res = requests.get(url)
res = json.loads(res.content)
print(type(res['pokemon'][0]))
poke = res['pokemon']

dragons = []

for i in poke:
    for l in i['type']:
        if l == "Dragon":
            dragons.append(i)

pprint(dragons)

heavyweights = []

for i in poke:
    var = i['weight'].split()[0]
    if float(var) > 80:
        heavyweights.append(i)

pprint(heavyweights)
print(len(poke))

rando = []

for i in range(0,5):
    if i not in rando:
        rando.append(poke[random.randint(0,len(poke)-1)])
    else:
        continue

pprint(rando)

twoRand = []

for i in range(0,2):
    if i not in twoRand:
        twoRand.append(poke[random.randint(0,len(poke)-1)])
    else:
        continue

def fight():
    poke1 = twoRand[0]
    poke2 = twoRand[1]

    for i in poke1["weaknesses"]:
        if i in poke2["type"]:
            poke1Win = False
        else: poke1Win = True
    for i in poke2["weaknesses"]:
        if i in poke1["type"]:
            poke2Win = False
        else: poke2Win = True

    if poke1Win and not poke2Win:
        print(poke1["name"] + " wins!")
    elif poke2Win and not poke1Win:
        print(poke2["name"] + ' wins!')
    else:
        print('draw')

fight()
