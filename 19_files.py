def read():
    numbers = []
    #abrir el archivo solo en modo lectura
    with open("./files/numbers.txt", "r") as f: 
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Débora","Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    #Escribir en el archivo names, si no existe se crea, si existe se sobre escribe
    #EL encoding es para poder trabajar con acentos, el conjunto de caracteres
    with open("./files/names.txt", "w",encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n")


def run():
    write()
    read()


if __name__ == '__main__':
    run()