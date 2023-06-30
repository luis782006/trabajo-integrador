import json

def Obtener_Lista_Comidas():
    try:
        #lee y obtengo la lista de comidas rapidas 
        with open("comidas_rapidas.json", "r", encoding="utf-8") as dataComidas:
            lista_comidas = json.load(dataComidas)
        
       
        return lista_comidas
    except Exception as e:
        print("Error al obtener lista de comidas" , str(e))
    
def Procesar_Opcion(opc):
    lista_comidas=Obtener_Lista_Comidas()
    if opc==1:
        Mostrar_Lista_Comidas(lista_comidas)

def Mostrar_Lista_Comidas(lista):
    for comida in lista:
        print("ID:", comida['id'])
        print("Descripción:", comida['descripcion'])
        print("Ingredientes:")
        for ingrediente in comida['ingredientes']:
            print("- ", ingrediente)

        print("Tiempo:", comida['tiempo'])
        print("Precio:", comida['precio'])
        print("Calorías:", comida['calorias'])
        print("Vegana:", comida['vegana'])
        print("--------------------")