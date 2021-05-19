from csv import reader
#contendra todo los datos del csv
food =[]
price =[]
time =[]
nutricion =[]
relation =[]
platillos=[]
#es para guardar lo que el consumidor desea
myfood =[]
myprive =[]
mytime=[]
mynutricion=[]
#lectura de los datos y separarlos segun su categoria
with open('export.csv', 'r') as csvDataFile:    
    csvReader = reader(csvDataFile)
    i=0
    for row in csvReader:
        #print(row)
        food.append(row[0])
        price.append(row[1])
        time.append(row[2])
        nutricion.append(row[3])
        relation.append(row[4])
        #este serivara para guardar los tipos de platillos en el platillos
        if(i!=0):
            foodtype = row[4].split()
            print(foodtype)
            for add in foodtype:
                #si lo contiene no lo guardara
                if(list.__contains__(platillos,add)):
                    print("")
                else:
                    platillos.append(add)
        else:
            i=i+1


print(food)
print(price)
print(time)
print(nutricion)
print(relation)
print(platillos)
#menu
i=0
ciclo = True
while ciclo == True:
    print("1. Escoger platillos")
    print("2. Escoger tiempo de entrega")
    print("3. Escoger contenido nutricional")
    print("4. Escoger precio")
    print("5. Buscar")
    print("6. Salir")
    opcion = input("Ingrese una opcion: ")
    #Escoger tipos de platillos de interes
    if(opcion=="1"):
        #mostrar los platillos dispobibles, para este se utilizara el del realcion y mostraremos cada una
        print("hola")
    #escoger tiempo
    elif(opcion=="2"):
        print("hola")
    #escoger contenido nutricional
    elif(opcion=="3"):
        print("hola")
    #escoger precio
    elif(opcion=="4"):
        print("hola")
    #buscar platillos que satisfacen con lo que se desea
    elif(opcion=="5"):
        print("hola")
    #terminar el ciclo
    elif(opcion=="6"):
        print("Gracias, espero que vuelvas pronto")
        ciclo=False
    #mostrar error
    else:
        print("Error, Ingrese solo del 1-6")


    

