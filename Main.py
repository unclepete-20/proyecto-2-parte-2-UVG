from csv import reader
#contendra todo los datos del csv
food =[]
price =[]
time =[]
nutricion =[]
relation =[]
platillos=[]
timeGeneral=["rapido","medio","lento"]
nutricionGeneral=["alta","media","baja"]
priceGeneral=["alto","medio","bajo"]
#es para guardar lo que el consumidor desea
myfood =[]
myprice =[]
mytime=[]
mynutricion=[]
foodInterest=[]
#lectura de los datos y separarlos segun su categoria
with open('export.csv', 'r') as csvDataFile:    
    csvReader = reader(csvDataFile)
    i=0
    for row in csvReader:
        print(row)
        #x=row[0]
        #y = x.split(";")
        #print(y)

        food.append(row[0])
        price.append(row[1])
        time.append(row[2])
        nutricion.append(row[3])
        relation.append(row[4])
        #este serivara para guardar los tipos de platillos en el platillos
        if(i!=0):
            foodtype = row[4].split()
            for add in foodtype:
                #si lo contiene no lo guardara
                if(list.__contains__(platillos,add)):
                    True
                else:
                    platillos.append(add)
        else:
            i=i+1


print(food)
#print(price)
#print(time)
#print(nutricion)
print(relation)
#print(platillos)
#menu
i=0
ciclo = True
while ciclo:
    print("___________________________________")
    print(myfood)
    print(mytime)
    print(mynutricion)
    print(myprice)
    print("___________________________________")
    print("1. Escoger platillos")
    print("2. Escoger tiempo de entrega")
    print("3. Escoger contenido nutricional")
    print("4. Escoger precio")
    print("5. Buscar")
    print("6. Salir")
    opcion = input("Ingrese una opcion: ")
    print("___________________________________")
    #Escoger tipos de platillos de interes
    if(opcion=="1"):
        #mostrar los platillos dispobibles, para este se utilizara el del realcion y mostraremos cada una
        comida = True
        while comida:
            for tipoPlatillo in platillos:
                print(tipoPlatillo)
                print("1. Agregar")
                print("2. Siguiente")
                print("3. Quitar")
                print("4. Regresar")
                op = input("Ingrese una opcion: ")
                if(op=="1"):
                    if(list.__contains__(myfood,tipoPlatillo)):
                        print("Ya lo contiene")
                    else:
                        myfood.append(tipoPlatillo)
                elif(op=="2"):
                    True
                elif(op=="3"):
                    if(list.__contains__(myfood,tipoPlatillo)):
                        myfood.remove(tipoPlatillo)
                        print("Se quito el platillo")
                elif(op=="4"):
                    comida=False
                    break
                else:
                    print("Error ingresa solo del 1-3")
                print("___________________________________")
            
    #escoger tiempo
    elif(opcion=="2"):
        tiempo = True
        while tiempo:
            for tipoTiempo in timeGeneral:
                    print(tipoTiempo)
                    print("1. Agregar")
                    print("2. Siguiente")
                    print("3. Quitar")
                    print("4. Regresar")
                    op = input("Ingrese una opcion: ")
                    if(op=="1"):
                        if(list.__contains__(mytime,tipoTiempo)):
                            print("Ya lo contiene")
                        else:
                            mytime.append(tipoTiempo)
                    elif(op=="2"):
                        True
                    elif(op=="3"):
                        if(list.__contains__(mytime,tipoTiempo)):
                            mytime.remove(tipoTiempo)
                            print("Se quito el tiempo")
                    elif(op=="4"):
                        tiempo=False
                        break
                    else:
                        print("Error ingresa solo del 1-3")
                    print("___________________________________")
        
    #escoger contenido nutricional
    elif(opcion=="3"):
        nutri = True
        while nutri:
            for tipoNutricion in nutricionGeneral:
                    print(tipoNutricion)
                    print("1. Agregar")
                    print("2. Siguiente")
                    print("3. Quitar")
                    print("4. Regresar")
                    op = input("Ingrese una opcion: ")
                    if(op=="1"):
                        if(list.__contains__(mynutricion,tipoNutricion)):
                            print("Ya lo contiene")
                        else:
                            mynutricion.append(tipoNutricion)
                    elif(op=="2"):
                        True
                    elif(op=="3"):
                        if(list.__contains__(mynutricion,tipoNutricion)):
                            mynutricion.remove(tipoNutricion)
                            print("Se quito el tipo de nutricion")
                    elif(op=="4"):
                        nutri=False
                        break
                    else:
                        print("Error ingresa solo del 1-3")
                    print("___________________________________")
    
    #escoger precio
    elif(opcion=="4"):
        precio = True
        while precio:
            for tipoPrecio in priceGeneral:
                    print(tipoPrecio)
                    print("1. Agregar")
                    print("2. Siguiente")
                    print("3. Quitar")
                    print("4. Regresar")
                    op = input("Ingrese una opcion: ")
                    if(op=="1"):
                        if(list.__contains__(myprice,tipoPrecio)):
                            print("Ya lo contiene")
                        else:
                            myprice.append(tipoPrecio)
                    elif(op=="2"):
                        True
                    elif(op=="3"):
                        if(list.__contains__(myprice,tipoPrecio)):
                            myprice.remove(tipoPrecio)
                            print("Se quito el precio")
                    elif(op=="4"):
                        precio=False
                        break
                    else:
                        print("Error ingresa solo del 1-3")
                    print("___________________________________")

    #buscar platillos que satisfacen con lo que se desea
    elif(opcion=="5"):
        foodInterest.clear()
        #para el tipo de platillo
        if(len(myfood)!=0):
            i=0
            for types in relation:
                for cliente in myfood:
                    if(types.__contains__(cliente)):
                        if(foodInterest.__contains__(food[i])):
                            True
                        else:
                            foodInterest.append(food[i])                        
                #aumentar
                i=i+1

        #para el tiempo, no funciona correctamente, ver como arreglarlo para que funcione adecuadamente
        '''if(len(mytime)!=0):
            i=0
            for types in time:
                verificar =True
                for cliente in mytime:
                    eliminar = False
                    if (verificar):
                        if(types.__contains__(cliente)):
                            True
                            break

                if(eliminar):

                    
                #aumentar
                i=i+1'''

        #mostar resultado
        for plato in foodInterest:
            print(plato)
        
    #terminar el ciclo
    elif(opcion=="6"):
        print("Gracias, espero que vuelvas pronto")
        ciclo=False
    #mostrar error
    else:
        print("Error, Ingrese solo del 1-6")


    

