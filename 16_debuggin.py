def divisors(num):
    #Si existe una condicion que impida el flujo normal del programa se puede lanzar una exception
    if(num<0):
        raise ValueError("No hay divisores de numeros negativos")
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    #Uso de try y except para entradas que no son numeros
    #Codigo a intentar si hay un error
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    #Lo que se ejecuta si hay una excepcion
    #except :
    #    print("Debes ingresar un numero.")
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    run()