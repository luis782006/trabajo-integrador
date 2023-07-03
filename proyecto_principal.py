import presentacion
import m_manejo_usuario
import m_manejo_comidas
import m_manejo_carrito

'''def login():
    while True:
        # Obtengo Usuario y Contraseña ingresadas por el usuario
        usuario_contraseña = m_manejo_usuario.pedir_datos_login()

        # Verifico si usuario existe en el archivo user.json
        existe = m_manejo_usuario.usuario_existe(usuario_contraseña[0])

        # Verifico si el usuario y contraseña ingresados son correctos
        if existe and m_manejo_usuario.control_usuario(usuario_contraseña[0], usuario_contraseña[1]):
            # Bienvenida al usuario
            m_manejo_usuario.bienvenida(usuario_contraseña[0])
            return usuario_contraseña[0], usuario_contraseña[1]
        else:
            print("El usuario y/o contraseña son incorrectos.")
            print("Elija que desea hacer:")
            print("R - Registrarse")
            print("I - Ingresar nuevamente")
            print("S - Salir")

            opcion = input("Presione 'R' para registrarse  o cualquier tecla para salir: ").upper()
            if opcion == "R":
                presentacion.limpiar_consola()
                # Se piden los datos de usuario y contraseña nuevamente
                usuario_creado = False
                while not usuario_creado:
                    print("Ingrese nuevamente su usuario y contraseña deseado")
                    usuario_contraseña = m_manejo_usuario.pedir_datos_login()
                    if m_manejo_usuario.usuario_existe(usuario_contraseña[0]):
                        print("¡El usuario '{}' ya está registrado! Por favor, elija otro nombre.".format(usuario_contraseña[0]))
                    else:
                        # Envío el usuario y contraseña para crear el usuario
                        usuario_creado = m_manejo_usuario.crear_usuario(usuario_contraseña[0], usuario_contraseña[1])

                # Se piden los datos de usuario y contraseña nuevamente para que ingrese con el usuarios creado
                usuario_contraseña = m_manejo_usuario.pedir_datos_login()
                return usuario_contraseña[0], usuario_contraseña[1]
            elif opcion == "I":
                presentacion.limpiar_consola()

                pass
            else:
                presentacion.Presentacion()
                print("                    GRACIAS POR USAR NUESTRA APP")# le doy estos espacios para que se vea mejor
                exit()

'''
def login():
    while True:
        # Obtengo Usuario y Contraseña ingresadas por el usuario
        usuario_contraseña = m_manejo_usuario.pedir_datos_login()

        # Verifico si usuario existe en el archivo user.json
        existe = m_manejo_usuario.usuario_existe(usuario_contraseña[0])

        # Verifico sabiendo que ya está registrado ese usuario si el usuario y contraseña ingresados son correctos
        if existe and m_manejo_usuario.control_usuario(usuario_contraseña[0], usuario_contraseña[1]):
            # Bienvenida al usuario
            m_manejo_usuario.bienvenida(usuario_contraseña[0])
            return usuario_contraseña[0], usuario_contraseña[1]
        else:
            print("El usuario y/o contraseña son incorrectos.")
            print("Elija qué desea hacer:")
            print("R - Registrarse")
            print("I - Ingresar nuevamente")
            print("S - Salir")


            opcion = input("Presione 'R' para registrarse o 'S' para salir: ").upper()
            opcion = input().upper()
            if opcion == "R":
                presentacion.limpiar_consola()
                # Se piden los datos de usuario y contraseña nuevamente
                usuario_creado = False
                while not usuario_creado:
                    print("Ingrese nuevamente su usuario y contraseña deseado")
                    usuario_contraseña = m_manejo_usuario.pedir_datos_login()
                    if m_manejo_usuario.usuario_existe(usuario_contraseña[0]):
                        print("¡El usuario '{}' ya está registrado! Por favor, elija otro nombre.".format(usuario_contraseña[0]))
                    else:
                        # Envío el usuario y contraseña para crear el usuario
                        usuario_creado = m_manejo_usuario.crear_usuario(usuario_contraseña[0], usuario_contraseña[1])

                # Se piden los datos de usuario y contraseña nuevamente para que ingrese con el usuario creado
                return usuario_contraseña[0], usuario_contraseña[1]
            elif opcion == "I":
                presentacion.limpiar_consola()
                # Vuelve al inicio del bucle y solicita los datos de inicio de sesión nuevamente porque de nuevo se equivoco
                continue  
            else:
                presentacion.Presentacion()
                print("              GRACIAS POR USAR NUESTRA APP")
                exit()

    #return False


# datos_login[1] es el usuario
# datos_login[2] es la contraseña

#Inicio de la app

def inicio_app():
    presentacion.limpiar_consola()
    presentacion.Presentacion()
    es_admin = False
        
    if presentacion.continuar_presentacion():
            presentacion.limpiar_consola()
            datos_login = login()

            if len(datos_login) != 0:
                es_admin = m_manejo_usuario.tipo_usuario(datos_login[0], datos_login[1])

            if es_admin:
                m_manejo_comidas.menu_admin()
            else:
                m_manejo_carrito.vaciar_carrito()
                m_manejo_carrito.menu_usuario(datos_login[0])

            exit()

inicio_app()