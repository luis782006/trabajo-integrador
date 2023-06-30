import presentacion
import m_manejo_usuario
import m_manejo_menu
import m_manejo_comidas

presentacion.LimpiarConsola()
presentacion.Presentacion()
if (presentacion.ContinuarPresentacion()):
    presentacion.LimpiarConsola()

def login():
    #Obtengo Usuario y Contraseña ingresadas por el usuario
    usuario_contraseña=m_manejo_usuario.PedirDatosLogin()

    #verifico si usuario existe el en archivo user.json
    existe=m_manejo_usuario.Usuario_Existe(usuario_contraseña[0])

    #Verifico si el usuario y contraseña ingresados son correctos
    if existe:
        m_manejo_usuario.ControlUsuario(usuario_contraseña[0],usuario_contraseña[1])
        #Bienvenida al usuario       
        m_manejo_usuario.Bienvenida(usuario_contraseña[0])
    else:
        print("El usuario no existe")
        print("Desea crear un usuario? (s/n)")
        opcion=input()
        if opcion=="s":
            presentacion.LimpiarConsola()
            #Se piden los datos de usuario y contraseña nuevamente
            usuario_contraseña=m_manejo_usuario.PedirDatosLogin()
            #envio el usuario y contraseña para crear el usuario
            m_manejo_usuario.CrearUsuario(usuario_contraseña[0],usuario_contraseña[1])
            #Se piden los datos de usuario y contraseña nuevamente
            usuario_contraseña=m_manejo_usuario.PedirDatosLogin()
        else:
            print("Gracias por usar la app")
            exit()
    return usuario_contraseña[0],usuario_contraseña[1]


# datos_login[1] es el usuario
# datos_login[2] es la contraseña
datos_login=login()
#inicializo variable para saber si tipo usuario= admin
es_Admin=False
#consulto si finalmente se logeo el usuario
if len(datos_login)!=0:
   #verifico si el usuario logeado es usuario o admin
   es_Admin=m_manejo_usuario.TipoUsuario(datos_login[0],datos_login[1])

opcion_menu=0
if es_Admin:
    opcion_menu=m_manejo_menu.menu_admin()
    m_manejo_comidas.Procesar_Opcion(opcion_menu)
else:   
    print("menu usuario")

