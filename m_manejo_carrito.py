import json
import presentacion
import m_manejo_comidas
import datetime


def Obtener_Lista_Carrito():
    
    with open('carrito.json','r',encoding="utf-8") as dataCarrito:
        lista_carrito=json.load(dataCarrito)
    return lista_carrito

def Elegir_comida(lista):
    #esta linea me esta reseteando la lista del carrito
    lista_carrito=[]
    lista_carrito_aux=Obtener_Lista_Carrito()
    lista_carrito=lista_carrito_aux['lista_carrito']
    # aqui tengo que ir concatenando la lista[lista_carrito] que ya tiene productos.
    print("-----------------------------")
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
            comida['cantidad']=cant_comida
            comida['precio_total']=comida['precio']*cant_comida
            #Le paso la cantidad que pidio el usuario para mostrarlo en el ticket. AGREGANDO UNA NUEVA CLAVE
            lista_carrito.append(comida)

    #obtengo lista del carrito para insertar los nuevos datos
    lst_carrito=Obtener_Lista_Carrito()
    lst_carrito['lista_carrito']=lista_carrito
    #paso los datos a la lista y paso el total de la compra(valor que se va a ser una suma sumatoria)
    try:      
        with open("carrito.json",'w',encoding="utf-8") as dataCarrito:
            json.dump(lst_carrito, dataCarrito)
            presentacion.limpiar_consola()
            print("COMIDA AGREGADA AL CARRITO")
    except Exception as e:
        print("Error no se realizo la accion" , str(e))
    return True   
    
def Consultar_carrito(lista):
   
    if len(lista['lista_carrito'])!=0:
        print("*-------------------CARRITO------------------*")
        for comida_en_carito in lista['lista_carrito']:
            print("     ID:", comida_en_carito['id'])
            print("     DESCRIPCION: ", comida_en_carito['descripcion'])
            print("     CANTIDAD DEL PRODUCTO SELECCIONADO: ", comida_en_carito['cantidad'])
            print("     TOTAL POR PRODUCTO: ", comida_en_carito['precio_total'])
            print("*--------------------------------------------*")
            
    else:
        print("     NO TIENE NADA EN EL CARRITO")        

    print("     IVA Resp-INSCRIPTO")
    print("     CUIT:", "20-12345678-9")
    print("     A CONSUMIDOR FINAL")
    total=0
    #Obtengo la fecha actual y le doy un formato pa mostrar al final
    fecha_actual = datetime.datetime.now()
    fecha_format = fecha_actual.strftime("%d-%m-%Y")
    hora_format = fecha_actual.strftime("%H:%M")

    #Recorro y sumo los valores
    lista_carrito_total=Obtener_Lista_Carrito()
    for comida_carrito in lista_carrito_total['lista_carrito']:
        total+=comida_carrito['precio_total']
    print("     TOTAL A PAGAR:", total)
    print("     FECHA:", fecha_format, "HORA:", hora_format)
    print("**************************************")
    lista_carrito_total['total_carrito']=total
    print("**************************************")

    #Si la lista esta vacia no pido la direccion
    if len(lista_carrito_total['lista_carrito'])!=0:
        if lista_carrito_total['direccion']=="":
            print("MIENTRAS PREPARAMOS SU ENVIO LE PEDIMOS NOS CONFIRME SU RETIRO")
            opcion_envio=input("Ingrese Tipo de entrega (Local( L ) / Domicilio ( D )) y continue su compra:").upper()
            if opcion_envio=="D" :
                direccion=input("Ingrese la direccion de envio: ")
                presentacion.limpiar_consola()    
                #cargo la lista de carrito
                lista=Obtener_Lista_Carrito()
                #le paso el valor de la direccion
                lista['direccion']=direccion
                almacenar_direccion(lista)
            else: 
                direccion="LOCAL"
                #cargo la lista de carrito
                lista=Obtener_Lista_Carrito()
                #le paso el valor de la direccion
                lista['direccion']=direccion
                almacenar_direccion(lista)    
                presentacion.limpiar_consola()   
                print("RETIRO EN LOCAL")     
            return direccion
      

def almacenar_direccion(lista):
    try:
       with open("carrito.json",'w',encoding="utf-8") as dataCarrito:
                json.dump(lista, dataCarrito)
                print("DIRECCION CARGADA")
    except Exception as e:
            print("Error no se realizo la accion" , str(e))

def vaciar_carrito():
    try:
        with open("carrito.json", 'r', encoding="utf-8") as dataCarrito:
            lista = json.load(dataCarrito)

        lista_carrito = lista['lista_carrito']
        lista_carrito.clear()
        lista['total_carrito'] = 0
        lista['direccion']=""

        with open("carrito.json", 'w', encoding="utf-8") as dataCarrito:
            json.dump(lista, dataCarrito)
        
        print("CARRITO VACIO")
        return True
    except Exception as e:
        print("Error: no se realizó la acción", str(e))
        return False

def menu_usuario(usuario):
    presentacion.limpiar_consola()
    print(f"****BIENVENIDO {usuario} **********")
    opcion = -1  # Inicializamos diferente de cero
    while opcion != 0:
        print("**************")
        print("MENU USUARIO")
        print("**************")
        print("1. Mostrar comidas rápidas")
        print("2. Elegir una comida rapida")
        print("3. Consultar y Confirmar el carrito")
        print("4. Imprimir ticket")
        print("5. Limpiar Carrito compras")
        print("0. Salir")
        
       
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            lista=m_manejo_comidas.Obtener_Lista_Comidas()
            m_manejo_comidas.mostrar_lista_comidas(lista)
        elif opcion == 2:
            presentacion.limpiar_consola()
            lista=m_manejo_comidas.Obtener_Lista_Comidas()

            m_manejo_comidas.Mostrar_Comidas_Abreviadas(lista)
            Elegir_comida(lista)
        elif opcion == 3:
            presentacion.limpiar_consola()
            lista=Obtener_Lista_Carrito()
            direccion=Consultar_carrito(lista)
        elif opcion == 4:
            presentacion.limpiar_consola() 
            lista=Obtener_Lista_Carrito()
            direccion=lista['direccion']

            if len(lista['lista_carrito'])!=0:
                if lista['direccion']=="":
                    print("NO TIENE DIRECCION CARGADA, NO SE PUEDE IMPRIMIR EL TICKET")
                    print("POR FAVOR CARGUE LA DIRECCION EN OPCION 3 CONSULTA DE CARRITO")
                    print("*----------------------------------------------------------*")
                else:
                    if len(lista['lista_carrito'])!=0:
                        respuesta=input("SI IMPRIME SU TICKET NO PODRA MODIFICAR EL CARRITO Y SE VACIARA AUTOMATICAMENTE (S/N):").upper()
                        if respuesta=="S":
                            presentacion.limpiar_consola()                            
                            presentacion.Imprimir_carrito(direccion)
                            vaciar_carrito()
                        else:
                            print("NO SE IMPRIMIO EL TICKET")
                            continue
                            
            else:
                print("CARRITO VACIO")
        elif opcion == 5:
            lista=Obtener_Lista_Carrito()
            presentacion.limpiar_consola()
            vaciar_carrito()
        elif opcion == 0:
            presentacion.limpiar_consola()
            presentacion.Presentacion()
            print("                     GRACIAS POR USAR NUESTRO SERVICIO")

       
                
    