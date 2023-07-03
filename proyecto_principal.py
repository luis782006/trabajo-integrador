import presentacion
import m_manejo_usuario
import m_manejo_comidas
import m_manejo_carrito

es_Admin=False

def login():
    #Obtengo Usuario y Contraseña ingresadas por el usuario
    usuario_contraseña=m_manejo_usuario.pedir_datos_login()

    #verifico si usuario existe en el archivo user.json
    existe=m_manejo_usuario.usuario_existe(usuario_contraseña[0])

    #Verifico si el usuario y contraseña ingresados son correctos
    if existe:
        while existe and not m_manejo_usuario.control_usuario(usuario_contraseña[0],usuario_contraseña[1]):
            print("Contraseña incorrecta, intente de nuevo")
            usuario_contraseña=m_manejo_usuario.pedir_datos_login()
            #Bienvenida al usuario       
        m_manejo_usuario.bienvenida(usuario_contraseña[0])
        return usuario_contraseña[0],usuario_contraseña[1]
        

    else:
        print("NO ESTA REGISTRADO EN LA APP")
        opcion=input("PRESIONE R PARA REGISTRARSE O CUALQUIER TECLA PARA SALIR").upper()

        if opcion=="R":
            presentacion.limpiar_consola()
            #Se piden los datos de usuario y contraseña nuevamente
            usuario_creado=False
            while not usuario_creado:
                print("Ingrese nuevamente su usuario y contraseña deseado")
                usuario_contraseña=m_manejo_usuario.pedir_datos_login()
                #envio el usuario y contraseña para crear el usuario
                usuario_creado=m_manejo_usuario.crear_usuario(usuario_contraseña[0],usuario_contraseña[1])
            
            #Se piden los datos de usuario y contraseña nuevamente
            usuario_contraseña=m_manejo_usuario.pedir_datos_login()
            return usuario_contraseña[0],usuario_contraseña[1]
        else:
            print("GRACIAS POR USAR NUESTRA APP")
            exit()

    

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