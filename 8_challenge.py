# crear un comprehension que de los numeros que son multiplos de 4, 6 y 9

def run():

    # multiples = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]    
    multiples = [i for i in range(1, 100000) if i % (36) == 0]    
    print(multiples)


if __name__ == "__main__":
    run()