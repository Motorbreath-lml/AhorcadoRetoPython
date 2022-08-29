#Lista de diccionarios
from pprint import pprint


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    #SE creara una lista con los nombres de todos los trabajadores en DATA que manejen python
    # del diccionario worker quiero el valor de la llave name, un for each de data, donde cada elemento de data lo llamaremos worker, la condicion que deve cumplir, de la llaver language quiero al worker si lenguage es python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print(f"Lista de todos los desarrolladores: \n{all_python_devs}\n")
    
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print(f"Lista de todos los que trabajan en Platzi: \n{all_Platzi_workers}\n")
    
    adults =  [worker["name"] for worker in DATA if worker["age"] >= 18]
    print(f"Lista de todos los adultos: \n{adults}\n")

    old_people_comprehension=[worker["name"] for worker in DATA if worker["age"]>70]
    print(f"Lista de todos los adultos mayores de 70 años: \n{old_people_comprehension}\n")

    #High order functions  
    print("Data antes de agregar la llaver 'old'")
    pprint(DATA)
    #EL operador pipe '|' en python 9 y superiores permite agregar una llave y valor a los diccionarios
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    print("\nLa variables 'old_people' tiene la variable  DATA despues de agregar la llaver 'old'")
    pprint(old_people)

    #EL filtro regresa el diccionario que cumple con la condicion en la llave, y list lo enlista en una varibale
    adults= list(filter(lambda worker: worker["age"]>=18, DATA))    
    print("\nTodos los adultos como lista de diccionarios:")
    pprint(adults)

    #De la lista de diccionarios solo quiero recuperar los nombres y pasarlos a una lista, en este caso adults apuntara a esta nueva lista
    adults= list(map(lambda worker: worker["name"], DATA))
    print(f"\nTodos los adultos como lista de nombres: {adults}")

    #LAs funciones lambda siempre necesitan regresar un valor, si se usa un if, siempre se debe usar tambien un else ya que se necesita un valor afuerza si la condicion falla, por eso hay que unsar un filter para limpiar los datos que no cimplen con la condicion
    all_python_devs=list(map(lambda worker: worker["name"] if worker["language"]=="python" else None, DATA))
    print(f"Todos los desarroladores de python antes de filtrar la lista: {all_python_devs}")
    all_python_devs=list(filter(lambda worker: worker!=None, all_python_devs))
    print(f"Todos los desarroladores de python: {all_python_devs}")

    #filter siempre regresa el mismo tipo del que se le pasa, por ejemplo en diccionario simepre regresara un diccionario, no regresaria el valor o la llave de un diccionario, la funcion lamba que usa es un if, si se sumple la condicion regresa el objeto, adiferencia de map, que siempre tiene que regresar algo aunque no se cumpla la condicion
    all_Platzi_workers=list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    print("\nTods los trabajadores de Platzi:")
    pprint(all_Platzi_workers)
    all_Platzi_workers=list(map(lambda worker:worker["name"],all_Platzi_workers))
    print(f"\nLa lista de los nombres de los trabajadores de Platzi: {all_Platzi_workers}")


if __name__ == '__main__':
    run()