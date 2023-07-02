import presentacion
import m_manejo_usuario
import m_manejo_comidas
import m_manejo_carrito

es_Admin=False

def login():
    #Obtengo Usuario y Contraseña ingresadas por el usuario
    usuario_contraseña=m_manejo_usuario.PedirDatosLogin()

    #verifico si usuario existe el en archivo user.json
    existe=m_manejo_usuario.Usuario_Existe(usuario_contraseña[0])

    #Verifico si el usuario y contraseña ingresados son correctos
    if existe:
        if m_manejo_usuario.ControlUsuario(usuario_contraseña[0],usuario_contraseña[1]):
             #Bienvenida al usuario       
             m_manejo_usuario.Bienvenida(usuario_contraseña[0])
             return usuario_contraseña[0],usuario_contraseña[1]
    else:
        print("NO ESTA RESGISTRADO EN LA APP")
        opcion=input("PRESIONE R PARA REGISTRASE O CUALQUIER TECLA PARA SALIR").upper()

        if opcion=="R":
            presentacion.LimpiarConsola()
            #Se piden los datos de usuario y contraseña nuevamente
            usuario_creado=False
            while not usuario_creado:
                print("Ingrese nuevamente su Usuario y contraseña deseado")
                usuario_contraseña=m_manejo_usuario.PedirDatosLogin()
                #envio el usuario y contraseña para crear el usuario
                usuario_creado=m_manejo_usuario.CrearUsuario(usuario_contraseña[0],usuario_contraseña[1])
            
            #Se piden los datos de usuario y contraseña nuevamente
            usuario_contraseña=m_manejo_usuario.PedirDatosLogin()
            return usuario_contraseña[0],usuario_contraseña[1]
        else:
            print("GRACIAS POR USAR NUESTRA APP")
            exit()

    

# datos_login[1] es el usuario
# datos_login[2] es la contraseña

#Inicio de la app

def InicioApp():
    presentacion.LimpiarConsola()
    presentacion.Presentacion()
    es_Admin = False
   

    if presentacion.ContinuarPresentacion():
        presentacion.LimpiarConsola()
        datos_login = login()

        if len(datos_login) != 0:
            es_Admin = m_manejo_usuario.TipoUsuario(datos_login[0], datos_login[1])

        if es_Admin:
            m_manejo_comidas.menu_admin()
        else:
            m_manejo_carrito.vaciar_carrito()
            m_manejo_carrito.menu_usuario(datos_login[0])

    exit()

InicioApp()