import csv

food =[]
price =[]
time =[]
nutricion =[]
relation =[]

with open('export.csv', 'r') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    
    for row in csvReader:
        print(row)
        "food.append(row)"
        """price.append(row[0])
        time.append(row[0])
        nutricion.append(row[0])
        relation.append(row[0])"""

print(food)
print(price)
print(time)
print(nutricion)
print(relation)
