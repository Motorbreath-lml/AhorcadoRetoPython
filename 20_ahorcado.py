from ast import While
import platform
import os
import random
from runpy import run_path
import re

def hangman():
    oportunidad=[
                """
                __________
                |/      |
                |      
                |      
                |      
                |      
                |___
                """,
                """
                __________
                |/      |
                |      (_)
                |       |
                |       |
                |      
                |___
                """,
                """
                __________
                |/      |
                |      (_)
                |      \|
                |       |
                |      
                |___
                """,
                """
                __________
                |/      |
                |      (_)
                |      \|/
                |       |
                |      
                |___
                """,
                """
                __________
                |/      |
                |      (_)
                |      \|/
                |       |
                |      /
                |___
                """,
                """
                __________
                |/      |
                |      (_)
                |      \|/
                |       |
                |      / \\
                |___
                """
    ]
    return oportunidad


def banner_inicio():
    banner="""
    _    _                             _       
   / \  | |__   ___  _ __ ___ __ _  __| | ___  
  / _ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ 
 / ___ \| | | | (_) | | | (_| (_| | (_| | (_) |
/_/   \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/ 
                                               
 _____ _     _                        
| ____| |   (_)_   _  ___  __ _  ___  
|  _| | |   | | | | |/ _ \/ _` |/ _ \ 
| |___| |   | | |_| |  __/ (_| | (_) |
|_____|_|  _/ |\__,_|\___|\__, |\___/ 
          |__/            |___/       
    """
    return banner


def lista_palabras():
    lista=[]
    with open("./files/data.txt", "r",encoding="utf-8") as f: 
        for line in f:
            lista.append(line)
    return lista


def limpiar_pantalla():
    sistema = platform.system()
    sistema="cls" if sistema=="Windows" else "clear"
    os.system(sistema)


def game_over(conseguido,palabra):
    limpiar_pantalla()
    banner=""
    ruta="./files/"
    if conseguido:
        ruta+="win"
    else:
        ruta+="lose"
    ruta+=".txt"
    with open(ruta, "r",encoding="utf-8") as f: 
        for line in f:
            banner+=line
    print(banner)
    input("La palabra es: "+palabra+"\nPresiona una enter para salir al menu principal")


def letra_encontrada(diccionario_palabra,letra_entrada,mostrar_palabra):
    for indice in diccionario_palabra[letra_entrada]:
        mostrar_palabra[indice]=" "+letra_entrada+" "
    del diccionario_palabra[letra_entrada]


def letra_azar(dificultad,diccionario_palabra,mostrar_palabra):
    regex=""
    if dificultad==1:
        regex="[aeiou]"
    else:
        regex="[^aeiou]"

    for key in diccionario_palabra:
        x=re.search(regex,key)
        if x:
            letra_encontrada(diccionario_palabra,key,mostrar_palabra)
            break

def dificultad_letrero(dificultad):
    if (dificultad==2):
        dificultad_letra="Dificil"
    elif (dificultad==1):
        dificultad_letra="Intermedio"
    else: 
        dificultad_letra="Facil"
    return dificultad_letra


def jugar(dificultad):
    lista=lista_palabras()
    indice=random.randint(0,len(lista)-1)
    palabra=lista[indice]
    diccionario_palabra={letra:[] for letra in palabra if letra!='\n'}
    mostrar_palabra=[" _ " for letra in palabra if letra !='\n']
    for i in range(len(palabra)-1):
        diccionario_palabra[palabra[i]].append(i)
    ahorcado=hangman()
    intentos=-1
    conseguido=False

    dificultad_letra=dificultad_letrero(dificultad)
    
    if dificultad!=2:        
        letra_azar(dificultad,diccionario_palabra,mostrar_palabra)


    while intentos<6 and not conseguido:
        limpiar_pantalla()
        print("Numero de intentos: "+str(intentos+1)+" Dificultad: "+dificultad_letra)
        if intentos>-1:
            print(ahorcado[intentos])
        for caracter in mostrar_palabra:
            print(caracter,end="")
        print("\n")
        letra_entrada=input("Teclea una letra, que piense que este en la palabra\n: ")
        if diccionario_palabra.get(letra_entrada) is not None:
            letra_encontrada(diccionario_palabra,letra_entrada,mostrar_palabra)            
        else:
            intentos+=1
        if(len(diccionario_palabra)==0):
            conseguido=True
    
    game_over(conseguido,palabra)

    print("indice: "+str(indice)+" No.Palabras: "+str(len(lista))+" Palabra: "+palabra)
    print("EL diccionario")
    print(diccionario_palabra)


def run():    
    banner=banner_inicio()    
    salir=True
    dificultad=0

    while salir==True:
        limpiar_pantalla()
        print(banner)
        print("Dificultad: "+dificultad_letrero(dificultad))
        print("Selecciona una opcion del menu, presionando la tecla correspondiente y enter")
        seleccion=input("\n1 - Jugar\n2 - Seleccionar dificultad\n3 - Revisar la lista de palabras\n0 - Salir\n")
        #El siguiente switch solo funciona en python 3.10
        #https://towardsdatascience.com/switch-case-statements-are-coming-to-python-d0caf7b2bfd3
        match seleccion:
            case "1": #jugar, pasar como argumento dificultad
                jugar(dificultad)
            case "2": #dificultad
                limpiar_pantalla()
                dificultad=int(input("Nivel de dificultad\n0 - Facil(Ayuda de una letra)\n1 - Intermedio(Ayuda de una vocal)\n2 - Dificil(Sin ayudas)\n"))
                if(dificultad<0 or dificultad>2):
                    dificultad=0                
            case "3": #Lista de palabras
                for palabra in lista_palabras():
                    print(palabra)
                input("Presiona enter para continuar.")
            case "0": #Salir
                salir=False
            case _:
                print("Opcion no valida")


if __name__ == '__main__':
    run()