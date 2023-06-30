import json
import presentacion

def PedirDatosLogin():
    print("               **************")
    print("                   LOGIN")
    print("               **************")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    return usuario,contraseña

#Verifico si el usuario existe en arcihvo user.json
def Usuario_Existe(nombre_usuario):
    usuarioValido = False
    with open('user.json','r') as dataUser:
        usuarios = json.load(dataUser)

    for usuario in usuarios:
        if usuario["user"] == nombre_usuario:
            usuarioValido = True
            break

    return usuarioValido

def CrearUsuario(usuario,contraseña):
    nuevoUsuario = {
        "user": usuario,
        "password": contraseña
    }
    try:
        #lee y obtengo la lista de usuarios
        with open("user.json", "r", encoding="utf-8") as dataUser:
            lista_usuarios = json.load(dataUser)
        
       
        #addiciono el nuevo usuario a la lista de usuarios
        lista_usuarios.append(nuevoUsuario)
        #actualizo el archivo user.json
        with open("user.json", "w", encoding="utf-8") as dataUser:
            json.dump(lista_usuarios, dataUser)
        print("**************")
        print("Usuario registrado con éxito")
        print("**************")
        if (presentacion.ContinuarPresentacion()!=True):
            exit()
        else:
            presentacion.LimpiarConsola()
       
    except Exception as e:
        print("Error al registrar usuario" , str(e))
        


#Verifica si el usuario y contraseña ingresados son correctos
def  ControlUsuario(usuario,contraseña):
    with open('user.json') as lista_usuario:
        lst_usuarios = json.load(lista_usuario)
    for usuario in lst_usuarios:
        if usuario["user"] == usuario and usuario["password"] == contraseña:
            return True
    return False

def Bienvenida(usuario):
    presentacion.LimpiarConsola()   
    print("**************")
    print("BIENVENIDO ", usuario.upper())
    print("**************")

def TipoUsuario(usuario,contraseña):
    if usuario == "admin" and contraseña == "admin":
        return True
    else:
        return False