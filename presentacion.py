import os

def Presentacion():
  
    archivo = open("logo.txt", "r",encoding="utf-8") 
    contenido = archivo.read()  
    print(contenido)  
    archivo.close()  
    print("                           **************")
    print("                            LISTOS YA!!!")
    print("                           **************")
    print("                  *******APP LISTOS-YA V 1.0*********")

def continuar_presentacion():
    
    opcion = input("              Desea continuar? (s/n): ").upper()
    if opcion == "S":
        return True
    else:
        return False    

def Imprimir_carrito(direccion):
    archivo=open("impresora.txt","r",encoding="utf-8")
    contenido=archivo.read()
    print(contenido)
    archivo.close()
    print("****************************************")
    print("TICKET IMPRESO")
    print("****************************************")
    if direccion=="LOCAL":
        print("Esperamos por su retirto ")
        print("GRACIAS POR USAR NUESTRO SERVICIO")
        print("*****************************************")
    else:
        print("Su pedido será enviado a la dirección: ",direccion)
        print("GRACIAS POR USAR NUESTRO SERVICIO")
        print("*****************************************")

 
    

def limpiar_consola():
    os.system('cls')