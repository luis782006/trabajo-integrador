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

def ContinuarPresentacion():
    
    opcion = input("              Desea continuar? (s/n): ").upper()
    if opcion == "S":
        return True
    else:
        return False    

def LimpiarConsola():
    os.system('cls')