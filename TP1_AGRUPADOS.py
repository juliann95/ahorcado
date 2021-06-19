from typing import Type
from texto import obtener_texto
texto_a_trabajar = obtener_texto()
import string
import random 
#etapa 1
########################################################################
#LEANDRO NAVEIRO    
########################################################################
def validar_ingreso(ingreso):
    #si la letra ni es un cararter alfabetico o tiene mas de un elemento no es valido
    if len(ingreso)>1 or not ingreso.isalpha():
        validar = False
    else:
        validar = True    
    return validar
########################################################################
#codigo de valen 
########################################################################
def pasar_listas_a_cadenas(lista):
    #funcion complementaria de 'remplazar_letras_adivinadas' que se encarga de pasar una lista de cadenas
    # a una sola cadena
    cadena = ""
    for caracter in lista:
        cadena += caracter
    return cadena 

def reemplazar_letras_adivinadas(palabra,palabra_adivinar,letra):
    #se encarga de reemplazar las letras que va ingresando el usuario, dentro de la 'palabra_a_adivinar'
    palabra_a_adivinar = list(palabra_adivinar) 
    indice = []
    contar_letras = -1
    for l in palabra:
        contar_letras += 1
        if l == letra:
            indice.append(contar_letras)
    for i in indice:
        palabra_a_adivinar[i] = letra
    return pasar_listas_a_cadenas(palabra_a_adivinar)

def ocultar_palabra(palabra):
    #genera una cadena de '?' con la longitud de la palabra que se quiere adivinar
    palabra_adivinar = "?" * len(palabra)
    return palabra_adivinar
########################################################################
#valen
########################################################################
def interaccion(palabra_a_adivinar, ACIERTOS, DESACIERTOS,mensaje):
    #funcion que se encarga de imprimir por panatalla el avance del programa a medida que interactua con  
    # el usuario
    print("--------------------------------------------------------------")
    print(mensaje,"→" ,palabra_a_adivinar, 'Aciertos:', ACIERTOS, 'Desaciertos:',len(DESACIERTOS))
    print(DESACIERTOS)
    
########################################################################
#valen y LEANDRO NAVEIRO
########################################################################
def ahorcado(palabra,lista_letras_ingresadas,ACIERTOS): 
    palabra_a_adivinar = ocultar_palabra(palabra)
    interaccion(palabra_a_adivinar,0,lista_letras_ingresadas,"Palabra a adivinar:")
    letra = input("Ingrese letra: ")
    letra = letra.lower()
    #se ejecuta el siclo mientras ganas, pierdas, o te rindas
    while palabra_a_adivinar != palabra and letra != "fin" and letra != "0" and len(lista_letras_ingresadas)<7:
        #valida la letra ingresada sino es una ingreso invalido
        if validar_ingreso(letra) :
            #dentro de esta validacion hay 4 posibilidades 
            #si ela letra esta y no esta ingresada
            if letra in palabra and letra not in palabra_a_adivinar:
                palabra_a_adivinar = reemplazar_letras_adivinadas(palabra,palabra_a_adivinar,letra)
                ACIERTOS += 1
                interaccion(palabra_a_adivinar,ACIERTOS,lista_letras_ingresadas,"Muy bien!!!")
            #esta la letra y ya esta infresada 
            elif letra in palabra and letra in palabra_a_adivinar:
                interaccion(palabra_a_adivinar,ACIERTOS,lista_letras_ingresadas,"Letra ya ingresada")
            #la letra no esta en la palabra y no esta ingresada se ingresa la letra a la lista
            elif letra  not in palabra and letra not in lista_letras_ingresadas:
                lista_letras_ingresadas.append(letra)
                interaccion(palabra_a_adivinar,ACIERTOS,lista_letras_ingresadas,"Lo siento!!!")
            #y que la letra ya este ingresado
            else:
                interaccion(palabra_a_adivinar,ACIERTOS,lista_letras_ingresadas,"letra ya ingresada")
        #
        else:
            interaccion(palabra_a_adivinar,ACIERTOS,lista_letras_ingresadas,"Ingreso Inválido")
        #de cualquier manera pide la letra al 
        # terminar el siclo a menos que ya este que ganes o pierdas
        if palabra_a_adivinar != palabra and len(lista_letras_ingresadas)<7:
            letra = input("Ingrese letra: ")
            letra = letra.lower()
    #una ves terminado el siclo se 
    if palabra_a_adivinar == palabra:
        print("felicidades a ganado")
    elif len(lista_letras_ingresadas)==7: 
        print("A Perdido!!","\n","la palabra es: ",palabra)
    else:
        print("has finalizado el juego")
    return [ACIERTOS, lista_letras_ingresadas]
######################################################################## 
            ###################ETAPA 2##################    
#########################################################################
#LEANDRO NAVEIRO
def acento(cadena):
    #entra al texto entero en cada letra con acento 
    # la cambia por la misma letra sin acento
    #repitiendo el siclo por cada letra
    reemplazo = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))
    for a, b in reemplazo:
        cadena = cadena.replace(a, b).replace(a.upper(), b.upper())
    return cadena
#LEANDRO NAVEIRO
def limpiador(lista_texto): 
    contador = 0
    #recorre una lista con un contador indicando la posicion
    for i in lista_texto:
        #
        lista_texto[contador] = lista_texto[contador].lower()
        #quita los elementos finales de cada cadena
        if i[-1:] == "." or i[-1:] == "!" or i[-1:] == "," or i[-1:] == "_":
            lista_texto[contador] = i[:len(i)-1]
        #quita los elementos iniciales
        #este if esta demas porque ya viene sin los simbolos finales un la funcino del main
        if i[:1] == "¡" or i[:1] == "_" or i[:1] == "¿" or i[:1] == "«":
            lista_texto[contador] = i[1:len(i)]
        contador += 1
    return lista_texto
##########################################################
#LEANDRO NAVEIRO 
#esta fucion recorre tora la lista guarda posiciones las ordena 
# desde la ultima se elimina con el metodo .pop() eliminando los 
# ultmpos elementos para no cambiar la posicion una ves borrados
def borrador(lista):
    posicion = []
    for i in range(len(lista)-1):
        if len(lista[i])< 5:
            posicion.append(i)
    ordenados = sorted(posicion , reverse = True)
    for i in ordenados:
        lista.pop(i)
    return lista
#########################################################
#CODIGO: JOSE BLANCO
def diccionario_ordenado(frecuencia):
  contadorPalabras={} 
  #Se crea un diccionario vacio 
  for palabra in frecuencia: 
    #Se recorre cada lina en el texto 
    if palabra in contadorPalabras:
      #Se suma 1 cada vez que una palabra se repite, en este caso la palabra seria la key y el numero de repeticiones de esta seria el value.
      contadorPalabras[palabra.lower()]+=1 
      #Usamos el metodo ".lower()" para hacer todas las palabras minusculas, porque si tuvieramos palabras mayusculas contarian como
    else:
      contadorPalabras[palabra.lower()]=1 
      #Si la palabra no esta en el diccionario, la registra y le asigna el valor 1
  return sorted(contadorPalabras.items(),key=lambda x:x[0],reverse=False) 
#usamos el "dict.items()" para obtener los key,value del diccionario y se ordena alfabeticamente con palabra,valor respectivamente
#########################################################
def generardic(lista):
    dic = {}
    for i in lista:
        dic[i[0]] = [1]
    return dic
#CODIGO: JOSE BLANCO, LEANDRO NAVEIRO
def generador():
    #esta funcion de con import string saca los simbolos basicos ASCII
    texto = obtener_texto().translate(str.maketrans('', '', string.punctuation)) 
    texto = acento(texto)
    lista_texto =  texto.split() 
    #se ejecuta dos veces para eliminar los caracteres dobres que puedar estar en el texto
    lista_texto = limpiador(lista_texto)
    lista_texto = limpiador(lista_texto)
    # elimina de la lista las palabras con menos de 5 caracteres
    lista_texto = borrador(lista_texto)
    #ordena y crea diccionario
    diccionario_texto  = dict(diccionario_ordenado(lista_texto))
    return diccionario_texto
######################################################################## 
            ###################ETAPA 3##################    
#########################################################################
#CODIGO: JOSE BLANCO
def sus(dictOrdenado,longitudPalabra):
    listaPalabras=[]
    #Creamos una lista para almacenar todas las palabras segun la longitud que queremos
    for palabra in dictOrdenado.items():
        #usamos el "dict.items()" para recorrer una lista de tuplas
        if len(palabra[0])==longitudPalabra:
            #Usamos la funcion "len()" y seleccionamos la posicion "0" para seleccionar solo la palabra
            listaPalabras.append(palabra[0])
            #Luego de comparar la longitud de la palabra con la longitud que se busca, si estas coinciden se agregan a la listaPalabras
        elif longitudPalabra==0:
            #Definimos que pasa si el parametro longitudPalabra es cero, que en este caso, si el parametro es cero, se toma todo el diccionario
            listaPalabras=list(dictOrdenado)
    return listaPalabras
###########################################################################
#CODIGO: JOSE BLANCO
def amogus(palabraCandidata):
    #Recibe como parametro las palabras filtradas anteriormente
    return random.choice(palabraCandidata)
    #Regresa una palabra aleatoria de las palabras posibles

def seleccion(long,diccionario): 
    #si la longitus es menor a 5 redefine la longitud para que elija 
    # cualquier elemento del diccionario 
    if long >= 5:
        palabras_candidatas =sus(diccionario, long)
        palabra = amogus(palabras_candidatas)
    else:
        long = 0 
        palabras_candidatas = sus(diccionario, long)
        palabra = amogus(palabras_candidatas)
    return palabra

######################################################################## 
            ###################ETAPA 4##################    
######################################################################### 
# etapa 4 
#LEANDRO NAVEIRO
def integracion():
    #crea dicionario
    diccionario = generador()
    #pide longitud
    longitud = int(input("ingrese la longitud de la palabra a adivinar\n debe ingresar un numero entero: "))
    #busca una palabra
    palabra = seleccion(longitud, diccionario)
    #envia palabra al juego y ejecuta el juego
    respuesta = ahorcado(palabra,[],0)
    return respuesta 

######################################################################## 
            ###################ETAPA 5##################    
#########################################################################.
#etapa 5 valen
def puntuacion():
    #se encaraga de llevar el puntaje del jugador a medida que quiera seguir jugando otras partidas
    # en caso de no querer continuar retorna el puntaje que ha acomulado a lo largo de las partidas
    puntaje = 0
    pregunta = "continuar"
    while pregunta != "no":
        #efecuta el juego
        ahorcado = integracion()
        #suma puntos
        puntaje += ahorcado[0] * 10 + (len(ahorcado[1])) * -5
        print("su puntuacion es: ",puntaje,"\n")
        pregunta = input("desea continuar?\npara salir del juego escriba ´no´ o presione enter para continuar\n")
    return puntaje
def main():  
    juego = puntuacion()
main()