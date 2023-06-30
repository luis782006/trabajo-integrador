import json
import m_manejo_menu
import presentacion

def Obtener_Lista_Comidas():
    try:
        #lee y obtengo la lista de comidas rapidas 
        with open("comidas_rapidas.json", "r", encoding="utf-8") as dataComidas:
            lista_comidas = json.load(dataComidas)
        
       
        return lista_comidas
    except Exception as e:
        print("Error al obtener lista de comidas" , str(e))
    
def Procesar_Opcion(opc):

    lista_comidas=Obtener_Lista_Comidas()
    if opc==1:
        Mostrar_Lista_Comidas(lista_comidas)
    elif opc==2:
        Buscar_Comida(lista_comidas)
        
    return opc    
        


def Mostrar_Lista_Comidas(lista):
    for comida in lista:
        print("ID:", comida['id'])
        print("Descripción:", comida['descripcion'])
        print("Ingredientes:")
        print("Ingredientes:", "-".join(comida['ingredientes']))
        print("Tiempo:", comida['tiempo'])
        print("Precio:", comida['precio'])
        print("Calorías:", comida['calorias'])
        print("Vegana:", comida['vegana'])
        print("--------------------")

def Buscar_Comida(lista):
    id = int(input("Ingrese el ID de la comida a buscar: "))
    for comida in lista:
        if comida['id'] == id:
            print("ID:", comida['id'])
            print("Descripción:", comida['descripcion'])
            print("Ingredientes:")
            for ingrediente in comida['ingredientes']:
                print("",ingrediente, end="-")
            print("")
            print("Tiempo:", comida['tiempo'])
            print("Precio:", comida['precio'])
            print("Calorías:", comida['calorias'])
            print("Vegana:", comida['vegana'])
            print("--------------------")
            break
    else:
        print("No se encontró la comida con el ID:", id)

def Modificar_Comida(lista):
    #Muestro toda las comidas
    Mostrar_Lista_Comidas(lista)
    #pregunto que comida desea modificar
    id = int(input("Ingrese el ID de la comida a modificar: "))
    #La muestro
    for comida in lista:
        if comida['id'] == id:
            print("ID:", comida['id'])
            print("Descripción:", comida['descripcion'])
            print("Ingredientes:")
            for ingrediente in comida['ingredientes']:
                print("",ingrediente, end="-")
            print("")
            print("Tiempo:", comida['tiempo'])
            print("Precio:", comida['precio'])
            print("Calorías:", comida['calorias'])
            print("Vegana:", comida['vegana'])
            print("--------------------")
            print("Ingrese los nuevos datos de la comida")
            descripcion = input("Ingrese la descripción: ")           
            tiempo = int(input("Ingrese el tiempo de preparación: "))
            comida['ingredientes'] = ingresar_ingredientes()
            precio = float(input("Ingrese el precio: "))
            calorias = int(input("Ingrese las calorías: "))
            vegana = input("Ingrese si es vegana (S/N): ")
            comida['descripcion'] = descripcion
            #los nuevos ingredientes se los paso desde una funcion por fuera
            comida['tiempo'] = tiempo
            comida['precio'] = precio
            comida['calorias'] = calorias
            #Control que si es Vengana guarde True y si no False
            if vegana=="S" or vegana=="s":
                comida['vegana'] = vegana == "True"
            else:
                comida['vegana'] = vegana == "False"
            break
    else:
        print("No se encontró la comida con el ID:", id)

    #actualizo el archivo user.json guarda do los cambios de la comida seleccionada
    with open("comidas_rapidas.json", "w", encoding="utf-8") as dataComidas:
        json.dump(lista, dataComidas)
    print("Comida modificada con éxito")
    if (presentacion.ContinuarPresentacion()!=True):
        exit()
    else:
        presentacion.LimpiarConsola()

#funcion para agregar los ingredientes a la lista 
def ingresar_ingredientes():
    ingredientes = []
    while True:
        entrada = input("Ingrese un ingrediente ( n para terminar): ")
        if entrada.lower() == "N" or entrada.lower() == "n":
            break
        ingredientes.append(entrada)
    return ingredientes

def Agregar_Comida(lista):
    ingredientes = []
    # Pedir todos los datos de comida
    print("Se solicitarán todos los datos de la comida")
    descripcion = input("Ingrese la descripción: ")
    tiempo = int(input("Ingrese el tiempo (en minutos) de preparación: "))
    ingredientes = ingresar_ingredientes()
    precio = float(input("Ingrese el precio: "))
    calorias = int(input("Ingrese las calorías: "))
    vegana = input("Ingrese si es vegana (S/N): ")

    if vegana.lower() == "s":
        vegana = True
    else:
        vegana = False

    # Obtengo el último id de la lista y le sumo 1 para asignarle el nuevo id
    id = lista[-1]['id'] + 1
    if Guardar_Nueva_Comida(lista,id,descripcion,ingredientes,tiempo,precio,calorias,vegana):
        menu_admin()
    

def Guardar_Nueva_Comida(lista,id,descripcion,ingredientes,tiempo,precio,calorias,vegana):
    # Crear el nuevo objeto comida
    nueva_comida = {
        "id": id,
        "descripcion": descripcion,
        "ingredientes": ingredientes,
        "tiempo": tiempo,
        "precio": precio,
        "calorias": calorias,
        "vegana": vegana
    }
    lista.append(nueva_comida)   
    try:    
        # Actualizo el archivo comidas_rapidas.json guardando los cambios de la comida seleccionada
        with open("comidas_rapidas.json", "w", encoding="utf-8") as dataComidas:
            json.dump(lista, dataComidas)
        print("Comida Insertada")
    except Exception as e:
        print("Error al registrar usuario" , str(e))
    return True
    
def menu_admin():
    presentacion.LimpiarConsola()
    opcion = -1  # Inicializamos la opción con un valor diferente de cero
    while opcion != 0:
        print("**************")
        print("MENU ADMIN")
        print("**************")
        print("1. Mostrar comidas rápidas")
        print("2. Buscar comida rápida")
        print("3. Modificar usuario")
        print("4. Agregar comidas rápidas")
        print("5. Borrar comidas rápidas")
        print("0. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            lista=Obtener_Lista_Comidas()
            Mostrar_Lista_Comidas(lista)
        elif opcion == 2:
            lista=Obtener_Lista_Comidas()
            Buscar_Comida(lista)
        elif opcion == 3:
            lista=Obtener_Lista_Comidas()
            Modificar_Comida(lista)
        elif opcion == 4:
            lista=Obtener_Lista_Comidas()
            Agregar_Comida(lista)
        elif opcion == 5:
            lista=Obtener_Lista_Comidas()
            Filtrar_Comida(lista)
    print("Gracias por usar la app")

   