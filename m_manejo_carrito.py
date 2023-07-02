import json
import presentacion
import m_manejo_comidas
import datetime
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
    
    with open('carrito.json','r',encoding="utf-8") as dataCarrito:
        lista_carrito=json.load(dataCarrito)
    return lista_carrito

def Elegir_comida(lista):
    lista_carrito=[]
    
    comida_id=int(input("Elija por -ID- la comida que desee: "))
    cant_comida=int(input("Indique la cantidad: "))

    for comida in lista:
        if comida['id']==comida_id:
            #le doy un indice y controlo que la lista tenga ya elementos o no
            if len(lista_carrito)!=0:
                id = lista_carrito[-1]['id'] + 1
            else:
                id = 1

            comida['id']=id
            #voy haciendo el calculo del precio de la comida con la cantidad
            cant_comida*=comida['precio']
            lista_carrito.append(comida)

    #obtengo lista del carrito para insertar los nuevos datos
    lst_carrito=Obtener_Lista_Carrito()

    lst_carrito['total_carrito']=lst_carrito['total_carrito']+cant_comida
    lst_carrito['lista_carrito']=lista_carrito
    #paso los datos a la lista y paso el total de la compra(valor que se va a ser una suma sumatoria)
    try:      
        with open("carrito.json",'w',encoding="utf-8") as dataCarrito:
            json.dump(lst_carrito, dataCarrito)
            print("COMIDA AGREGADA AL CARRITO")
    except Exception as e:
        print("Error no se realizo la accion" , str(e))
    return True   
    
def Consultar_carrito(lista):
   
    if len(lista['lista_carrito'])!=0:
        for comida_en_carito in lista['lista_carrito']:
            print("*-------CARRITO---------*")
            print("*------------------*")
            print("ID:", comida_en_carito['id'])
            print("DESCRIPCION:", comida_en_carito['descripcion'])
            print("*------------------*")
            print("IVA Resp-INSCRIPTO")
            print("CUIT:", "20-12345678-9")
            print("FECHA:", datetime.now().strftime("%d/%m/%Y %H:%M:%S")).upper()
            print("A CONSUMIDOR FINAL")
            print("TOTAL A PAGAR:", lista['total_carrito'])
    else:
        print("NO TIENE NADA EN EL CARRITO")        
    #Recorro y sumo los valores
 
    
def vaciar_carrito():
    try:
        with open("carrito.json", 'r', encoding="utf-8") as dataCarrito:
            lista = json.load(dataCarrito)

        lista_carrito = lista['lista_carrito']
        lista_carrito.clear()
        lista['total_carrito'] = 0

        with open("carrito.json", 'w', encoding="utf-8") as dataCarrito:
            json.dump(lista, dataCarrito)
        
        print("Carrito vacío")
        return True
    except Exception as e:
        print("Error: no se realizó la acción", str(e))
        return False



def menu_usuario(usuario):
    presentacion.LimpiarConsola()
 
    print(f"****BIENVENIDO {usuario} **********")
    opcion = -1  # Inicializamos diferente de cero
    while opcion != 0:
        print("**************")
        print("MENU USUARIO")
        print("**************")
        print("1. Mostrar comidas rápidas")
        print("2. Elegir una comida rapida")
        print("3. Consultar el carrito")
        print("4. Limpiar Carrito compras")
        print("0. Salir")
       
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            lista=m_manejo_comidas.Obtener_Lista_Comidas()
            m_manejo_comidas.Mostrar_Lista_Comidas(lista)
        elif opcion == 2:
            presentacion.LimpiarConsola()
            lista=m_manejo_comidas.Obtener_Lista_Comidas()
            m_manejo_comidas.Guardar_Nueva_Comida(lista)
            Elegir_comida(lista)
        elif opcion == 3:
            presentacion.LimpiarConsola()
            lista=Obtener_Lista_Carrito()
            Consultar_carrito(lista)
        elif opcion == 4:
            lista=Obtener_Lista_Carrito()
            vaciar_carrito()
                
    presentacion.LimpiarConsola()
    presentacion.Presentacion()
    print("                 GRACIAS POR USAR NUESTRA APP")
  