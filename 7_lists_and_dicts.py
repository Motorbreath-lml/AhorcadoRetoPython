#Principal program
def run():
    #Declaration of a list
    my_list = [1, "Hello", True, 4.5]
    #Declaration of a dictonary
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    #Declaration of a dictionary arrangement
    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    #Declaration of dicionary of array
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    #Tour the Arrangement Dictionary
    for key, value in super_dict.items():
        print(key, ">", value)

    #Tour the dictionary array
    for item in super_list:
        print()
        for key,value in item.items():
            print(key,":", value, ",",end="")


#Entry point
if __name__ == '__main__':
    run()