def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    try:
        assert num.isnumeric(), "Debes ingresar un número entero positivo"
    except AssertionError as msg:
        print(msg)
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()