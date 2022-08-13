def run():
    # Uso comun de lsitas y for
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # Comprehensions
    # Si se cumple la condicion que esta al final de la expresion
    # En el for intermedio de la exprexion
    # se agrega a la lista lo primero de la expresione
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    print(squares)


if __name__ == "__main__":
    run()