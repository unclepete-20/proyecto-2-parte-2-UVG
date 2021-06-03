from csv import reader

# Proyecto 2
# Estructuras de Datos
# Yong Bum Park 20117
# Pedro Pablo Arriola Jimenez 20188
# Oscar Fernando Lopez Barrios 20679

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

# Se crea el ciclo para el menu
i=0
ciclo = True
while ciclo:
    print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴\n")
    print("Bienvenido al Sistema de Recomendacion de Alimentos")
    print("___________________________________")
    print("Ingrese la opcion que desee:")
    print("1. Recibir Recomendacion de comida")
    print("2. ")
    print("3. Seleccionar contenido nutricional")
    print("4. Seleccionar precio")
    print("5. Buscar listado de recomendaciones")
    print("6. Salir del programa\n")
        
        print("1. Seleccionar ingredientes principales")
        print("2. Seleccionar tiempo de entrega")
        print("3. Seleccionar contenido nutricional")
        print("4. Seleccionar precio")
        print("5. Buscar listado de recomendaciones")
        print("6. Salir del programa\n")
        
        opcion = input("Ingrese una opcion: ")
        print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

        # Se escogen los tipos de ingredientes para los platos del usuario
        if(opcion=="1"):
            
            # Se muestran los platillos disponibles para el usuario
            comida = True
            while comida:
                for tipoPlatillo in platillos:
                    print("\n------- INGREDIENTES -------\n")
                    print(tipoPlatillo)
                    print("1. Agregar ingrediente a la lista")
                    print("2. Siguiente ingrediente")
                    print("3. Quitar ingrediente de la lista")
                    print("4. Regresar al menu principal\n")
                    
                    op = input("Ingrese una opcion: ")
                    if(op=="1"):
                        if(list.__contains__(myfood,tipoPlatillo)):
                            print("\nYa tienes seleccionado dicho ingrediente")
                        else:
                            myfood.append(tipoPlatillo)
                    elif(op=="2"):
                        True
                    elif(op=="3"):
                        if(list.__contains__(myfood,tipoPlatillo)):
                            myfood.remove(tipoPlatillo)
                            print("\nSe ha eliminado el ingrediente de la lista")
                    elif(op=="4"):
                        comida=False
                        break
                    else:
                        print("Error, ingresa solo del 1-3")
                    print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

            print("\n\n___________________________________")
            print("Ingredientes escogidos:")
            print(myfood)
            print("Tiempos de preparacion escogidos:")
            print(mytime)
            print("Contenidos Nutrcionales escogidos:")
            print(mynutricion)
            print("Precios escogidos:")
            print(myprice)
                
        #escoger tiempo
        elif(opcion=="2"):
            tiempo = True
            while tiempo:
                for tipoTiempo in timeGeneral:
                        print("\n------- TIEMPO DE PREPARACION -------\n")
                        print(tipoTiempo)
                        print("1. Seleccionar tiempo de preparacion")
                        print("2. Siguiente opcion")
                        print("3. Eliminar opcion de tiempo de preparacion")
                        print("4. Regresar al menu principal\n")
                        op = input("Ingrese una opcion: ")
                        if(op=="1"):
                            if(list.__contains__(mytime,tipoTiempo)):
                                print("\nYa tienes seleccionado dicho tiempo de preparacion")
                            else:
                                mytime.append(tipoTiempo)
                        elif(op=="2"):
                            True
                        elif(op=="3"):
                            if(list.__contains__(mytime,tipoTiempo)):
                                mytime.remove(tipoTiempo)
                                print("\nSe ha eliminado el tiempo de preparacion de la lista")
                        elif(op=="4"):
                            tiempo=False
                            break
                        else:
                            print("Error, ingresa solo del 1-3")
                        print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

            print("\n\n___________________________________")
            print("Ingredientes escogidos:")
            print(myfood)
            print("Tiempos de preparacion escogidos:")
            print(mytime)
            print("Contenidos Nutrcionales escogidos:")
            print(mynutricion)
            print("Precios escogidos:")
            print(myprice)
            
        #escoger contenido nutricional
        elif(opcion=="3"):
            nutri = True
            while nutri:
                for tipoNutricion in nutricionGeneral:
                        print("\n------- CONTENIDO NUTRICIONAL -------\n")
                        print(tipoNutricion)
                        print("1. Agregar el contenido nutricional deseado a la lista")
                        print("2. Siguiente opcion de contenido nutricional")
                        print("3. Eliminar seleccion de contenido nutricional de la lista")
                        print("4. Regresar al menu principal\n")
                        op = input("Ingrese una opcion: ")
                        if(op=="1"):
                            if(list.__contains__(mynutricion,tipoNutricion)):
                                print("\nYa tienes seleccionado dicho contenido nutricional")
                            else:
                                mynutricion.append(tipoNutricion)
                        elif(op=="2"):
                            True
                        elif(op=="3"):
                            if(list.__contains__(mynutricion,tipoNutricion)):
                                mynutricion.remove(tipoNutricion)
                                print("\nSe ha eliminado el contenido nutricional de la lista")
                        elif(op=="4"):
                            nutri=False
                            break
                        else:
                            print("Error ingresa solo del 1-3")
                        print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

            print("\n\n___________________________________")
            print("Ingredientes escogidos:")
            print(myfood)
            print("Tiempos de preparacion escogidos:")
            print(mytime)
            print("Contenidos Nutrcionales escogidos:")
            print(mynutricion)
            print("Precios escogidos:")
            print(myprice)
        
        #escoger precio
        elif(opcion=="4"):
            precio = True
            while precio:
                for tipoPrecio in priceGeneral:
                        print("\n------- PRECIO -------\n")
                        print(tipoPrecio)
                        print("1. Agregar el tipo de precio deseado a la lista")
                        print("2. Siguiente opcion de tipo de precio")
                        print("3. Eliminar el precio deseado de la lista")
                        print("4. Regresar al menu principal\n")
                        op = input("Ingrese una opcion: ")
                        if(op=="1"):
                            if(list.__contains__(myprice,tipoPrecio)):
                                print("\nYa tienes seleccionado dicha opcion del tipo de precio deseado")
                            else:
                                myprice.append(tipoPrecio)
                        elif(op=="2"):
                            True
                        elif(op=="3"):
                            if(list.__contains__(myprice,tipoPrecio)):
                                myprice.remove(tipoPrecio)
                                print("\nSe ha eliminado la seleccion del tipo de precio")
                        elif(op=="4"):
                            precio=False
                            break
                        else:
                            print("Error ingresa solo del 1-3")
                        print("\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴")

            print("\n\n___________________________________")
            print("Ingredientes escogidos:")
            print(myfood)
            print("Tiempos de preparacion escogidos:")
            print(mytime)
            print("Contenidos Nutrcionales escogidos:")
            print(mynutricion)
            print("Precios escogidos:")
            print(myprice)

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
            print("\n\n🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴 RECOMENDACIONES EN BASE A SU BUSQUEDA 🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴🍴\n")
            for plato in foodInterest:
                if(plato!="0"):
                    print(plato)
            
        #terminar el ciclo
        elif(opcion=="6"):
            print("\n🍴 Vuelve pronto al sistema de recomendaciones alimenticias 🍴\n")
            ciclo=False
        #mostrar error
        else:
            print("Error, Ingrese solo del 1-6")
