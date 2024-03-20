#with statements guarantees that a file will be closed regardless of what happens in the program
#form is "with <object> as <var>:"
#csv: comma seperated values (like spreadsheet), dilimiter is what seperates it.
import pprint
with open("file.csv", "r") as file:
    #file.readline() #skip first 2 lines
    #file.readline()
    key = file.readline()
    print(key)
    key = key.strip()
    print(key)
    key = key.split(';')
    print(key)
    carTemp = {}
    for i in key:
        carTemp[i.lower()] = None

    pprint.pprint(carTemp)

    file.readline()
    cars = []

    for i in file:
        car = file.readline()
        car = car.strip()
        car = car.split(';')
        carDict = carTemp.copy()
        for i in range(len(car)):
            carDict[key[i].lower()] = car[i]
        cars.append(carDict)
    pprint.pprint(cars)

    efficientCars = []

    for i in cars:
        if float(i['mpg']) >= 45:
            efficientCars.append(i['mpg'])

    print(efficientCars)
