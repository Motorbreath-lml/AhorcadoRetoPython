from ast import While
import platform
import os
import random

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


def jugar(dificultad):
    lista=lista_palabras()
    indice=random.randint(0,len(lista)-1)
    print("indice: "+str(indice)+" No.Palabras: "+str(len(lista)))




def run():
    banner=banner_inicio()    
    salir=True
    dificultad=0

    while salir==True:
        print(banner)
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
            case "0": #Salir
                salir=False
            case _:
                print("Opcion no valida")


if __name__ == '__main__':
    run()