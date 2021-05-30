from csv import reader

# Proyecto 2
# Estructuras de Datos
# Yong Bum Park
# Pedro Pablo Arriola Jimenez
# Oscar Fernando Lopez Barrios

# Variables que guardaran los datos de la comida 
# y los datos elegidos por el usuario
food =[]
price =[]
time =[]
nutricion =[]
relation =[]
platillos=[]
# Los distintos tipos de elecciones
timeGeneral=["rapido","medio","lento"]
nutricionGeneral=["alta","media","baja"]
priceGeneral=["alto","medio","bajo"]

# Se guarda la eleccion del usuario
myfood =[]
myprice =[]
mytime=[]
mynutricion=[]

# Listas donde se guarda la recomendacion
foodInterest=[]
timeInterest=[]
priceInterest=[]
nutricionInterest=[]

# Se leen los datos y se separan por medio de su categoria
with open('export.csv', 'r') as csvDataFile:    
    csvReader = reader(csvDataFile)
    # Se crea un ciclo para agregar los parametros
    i=0
    for row in csvReader:
        # Se agregan los parametros de busqueda
        food.append(row[0])
        price.append(row[1])
        time.append(row[2])
        nutricion.append(row[3])
        relation.append(row[4])

        #Se guardan los tipos de platillos que existen
        if(i!=0):
            foodtype = row[4].split()
            for add in foodtype:
                # Si se contiene el tipo de platillo se guarda
                if(list.__contains__(platillos,add)):
                    True
                else:
                    platillos.append(add)
        else:
            i=i+1

i=0
ciclo = True
while ciclo:
    print("___________________________________")
    print("Bienvenido al Sistema de Recomendacion de Alimentos")
    print("___________________________________")
    print("1. Escoger ingredientes principales")
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
                print("2. Siguiente opcion")
                print("3. Quitar seleccion")
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
        nutricioncopy=[]
        #limpiar el original
        foodInterest.clear()
        timeInterest.clear()
        priceInterest.clear()
        nutricionInterest.clear()

        #para el tipo de platillo
        if(len(myfood)!=0):
            i=0
            for types in relation:
                for cliente in myfood:
                    if(types.__contains__(cliente)):
                        if(foodInterest.__contains__(food[i])):
                            True
                        else:
                            #original
                            foodInterest.append(food[i])
                            timeInterest.append(time[i])   
                            priceInterest.append(price[i])   
                            nutricionInterest.append(nutricion[i])                 
                #aumentar
                i=i+1

        #para el tiempo
        if(len(mytime)!=0):
            i=0
            for types in timeInterest:
                yes=0
                for cliente in mytime:
                    if(types.__contains__(cliente)):
                        yes = yes + 1
                #si es igual a 0 no tiene ninguno que cumpla con el requisito del tiempo y se quitara de la lista
                if(yes==0):
                    indice = foodInterest.index(foodInterest[i])
                    foodInterest[indice]= "0"
                    timeInterest[indice]= "0"
                    priceInterest[indice]= "0"
                    nutricionInterest[indice]= "0"
                #aumentar
                i=i+1

        #para nutricion 
        if(len(mynutricion)!=0):
            i=0
            for types in nutricionInterest:
                yes=0
                for cliente in mynutricion:
                    if(types.__contains__(cliente)):
                        yes = yes + 1
                #si es igual a 0 no tiene ninguno que cumpla con el requisito del tiempo y se quitara de la lista
                if(yes==0):
                    indice = foodInterest.index(foodInterest[i])
                    foodInterest[indice]= "0"
                    timeInterest[indice]= "0"
                    priceInterest[indice]= "0"
                    nutricionInterest[indice]= "0"
                #aumentar
                i=i+1

        #para precio
        if(len(myprice)!=0):
            i=0
            for types in priceInterest:
                yes=0
                for cliente in myprice:
                    if(types.__contains__(cliente)):
                        yes = yes + 1
                #si es igual a 0 no tiene ninguno que cumpla con el requisito del tiempo y se quitara de la lista
                if(yes==0):
                    indice = foodInterest.index(foodInterest[i])
                    foodInterest[indice]= "0"
                    timeInterest[indice]= "0"
                    priceInterest[indice]= "0"
                    nutricionInterest[indice]= "0"
                #aumentar
                i=i+1

        #mostar resultado final
        print("\n======================= RECOMENDACIONES EN BASE A SU BUSQUEDA =======================\n")
        for plato in foodInterest:
            if(plato!="0"):
                print(plato)
        
    #terminar el ciclo
    elif(opcion=="6"):
        print("\n¡Vuelve pronto al sistema de recomendaciones alimenticias :)!\n")
        ciclo=False
    #mostrar error
    else:
        print("Error, Ingrese solo del 1-6")

    if(opcion != 5 and opcion != 6):
        print("\n\n___________________________________")
        print("Platillos escogidos:")
        print(myfood)
        print("Tiempos de Entrega escogidos:")
        print(mytime)
        print("Contenidos Nutrcionales escogidos:")
        print(mynutricion)
        print("Precios escogidos:")
        print(myprice)
