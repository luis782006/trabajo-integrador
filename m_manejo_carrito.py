import json
import presentacion
import m_manejo_comidas
'''
# Función para mostrar las comidas rápidas existentes
def mostrar_comidas(comidas):
    print("Comidas rápidas existentes:")
    for comida in comidas:
        print("Código:", comida["id"])
        print("Descripción:", comida["descripcion"])
        print("Precio:", comida["precio"])
        print("Ingredientes:", ", ".join(comida["ingredientes"]))
        print("Tiempo de elaboración:", comida["tiempo"])
        print("Calorías:", comida["calorias"])
        print("Vegana:", comida["vegana"])
        print("--------------------------------")

# Función para agregar una nueva comida rápida
def agregar_comida(comidas):
    codigo = int(input("Ingrese el código de identificación: "))
    descripcion = input("Ingrese la descripción de la comida: ")
    precio = float(input("Ingrese el precio de la comida: "))
    ingredientes = input("Ingrese los ingredientes separados por comas: ").split(",")
    tiempo_elaboracion = int(input("Ingrese el tiempo de elaboración en minutos: "))
    calorias = int(input("Ingrese las calorías de la comida: "))
    vegana = input("¿Es vegana? (Si/No): ").lower() == "si"

    nueva_comida = {
        "id": codigo,
        "descripcion": descripcion,
        "precio": precio,
        "ingredientes": ingredientes,
        "tiempo_elaboracion": tiempo_elaboracion,
        "calorias": calorias,
        "vegana": vegana
    }

    comidas.append(nueva_comida)
    print("¡Comida rápida agregada con éxito!")

# Función para modificar los datos de una comida rápida existente
def modificar_comida(comidas):
    codigo = int(input("Ingrese el código de identificación de la comida a modificar: "))

    for comida in comidas:
        if comida["id"] == codigo:
            print("Comida encontrada:")
            print("Código:", comida["id"])
            print("Descripción:", comida["descripcion"])
            print("Precio:", comida["precio"])
            print("Ingredientes:", ", ".join(comida["ingredientes"]))
            print("Tiempo de elaboración:", comida["tiempo_elaboracion"])
            print("Calorías:", comida["calorias"])
            print("Vegana:", comida["vegana"])
            print("--------------------------------")

            descripcion = input("Ingrese la nueva descripción de la comida (deje en blanco para no modificar): ")
            if descripcion:
                comida["descripcion"] = descripcion

            precio = input("Ingrese el nuevo precio de la comida (deje en blanco para no modificar): ")
            if precio:
                comida["precio"] = float(precio)

            ingredientes = input("Ingrese los nuevos ingredientes separados por comas (deje en blanco para no modificar): ")
            if ingredientes:
                comida["ingredientes"] = ingredientes.split(",")

            tiempo_elaboracion = input("Ingrese el nuevo tiempo de elaboración en minutos")
            
            # Función para buscar comidas rápidas por ingrediente
def buscar_por_ingrediente(comidas):
    ingrediente = input("Ingrese el ingrediente a buscar: ")
    resultados = []

    for comida in comidas:
        if ingrediente.lower() in [i.lower() for i in comida["ingredientes"]]:
            resultados.append(comida)

    if resultados:
        print("Resultados de búsqueda por ingrediente:")
        mostrar_comidas(resultados)
    else:
        print("No se encontraron comidas rápidas con ese ingrediente.")

# Función para buscar comidas rápidas por precio
def buscar_por_precio(comidas):
    precio = float(input("Ingrese el precio máximo: "))
    resultados = []

    for comida in comidas:
        if comida["precio"] <= precio:
            resultados.append(comida)

    if resultados:
        print("Resultados de búsqueda por precio:")
        mostrar_comidas(resultados)
    else:
        print("No se encontraron comidas rápidas dentro del rango de precio especificado.")

# Función para buscar comidas rápidas por calorías y comidas veganas disponibles
def buscar_por_calorias_veganas(comidas):
    calorias = int(input("Ingrese las calorías máximas: "))
    resultados = []

    for comida in comidas:
        if comida["calorias"] <= calorias and comida["vegana"]:
            resultados.append(comida)

    if resultados:
        print("Resultados de búsqueda por calorías y comidas veganas:")
        mostrar_comidas(resultados)
    else:
        print("No se encontraron comidas rápidas con esas características.")
'''
def Obtener_Lista_Carrito():
    lista_carrito={}
    with open('carrito.json','r',encoding="") as dataCarrito:
        lista_carrito=json.read(dataCarrito)
    return lista_carrito

def Elegir_comida(lista):
    lista_carrito=[]
    comida_id=int(input("Elija por -ID- la comida que desee"))
    cant_comida=int(input("Indique la cantidad "))
    for comida in lista:
        if comida['id']==comida_id:
            #le doy un indice 
            id = lista_carrito[-1]['id'] + 1
            comida['id']=id
            cant_comida*=comida['precio']
            lista_carrito.append(comida)

    try:      
        with open("carrito.json",'w',encoding="utf-8") as dataCarrito:
            json.dump(lista_carrito, dataCarrito)
            print("Comida agregada al carrito")
    except Exception as e:
        print("Error no se realizo la accion" , str(e))
    return True   
    
def Consultar_carrito(lista):
    for comida_en_carito in lista:
        print("*---**---*")
        print("Id:", comida_en_carito['id'])
        print("Descripcion:", comida_en_carito['descripcion'])
    
    print("*---**---*")
    #Recorro y sumo los valores

    
def vaciar_carrito(lista):
    #reseteo la lista carrito
    lista.clear()
    try:
        #lee y obtengo la lista de comidas rapidas 
        with open("carrito.json", "w", encoding="utf-8") as dataComidas:
            json.load(dataComidas)

    except Exception as e:
        print("Error al obtener lista de comidas" , str(e))


def menu_usuario():
    presentacion.LimpiarConsola()
    opcion = -1  # Inicializamos diferente de cero
    while opcion != 0:
        print("**************")
        print("MENU USUARIO")
        print("**************")
        print("1. Mostrar comidas rápidas")
        print("2. Elegir una comida rapida")
        print("3. Consultar el carrito")
        print("4. Confirmar compra")
        print("0. Salir")
       
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            lista=m_manejo_comidas.Obtener_Lista_Comidas()
            m_manejo_comidas.Mostrar_Lista_Comidas(lista)
        elif opcion == 2:
            presentacion.LimpiarConsola()
            lista=Obtener_Lista_Carrito()                       
            Elegir_comida(lista)
        elif opcion == 3:
            lista=Obtener_Lista_Carrito()
            Consultar_carrito(lista)
        elif opcion == 4:
            lista=Obtener_Lista_Comidas()
            Agregar_Comida(lista)
        elif opcion == 5:
            lista=Obtener_Lista_Comidas()
            Borrar(lista)
    print("Gracias por usar la app")
  