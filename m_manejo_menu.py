import presentacion

def menu_admin():
    presentacion.LimpiarConsola()
    print("**************")
    print("MENU ADMIN")
    print("**************")
    print("1. Mostrar comidas rapidas")
    print("2. Buscar comida rapida")
    print("3. Modificar usuario")
    print("4. Agregar comidas rapidas")
    print("5. Borrar comidas rapidas")
    print("0. Salir")
    opcion=int(input("Ingrese una opción: "))
    return opcion