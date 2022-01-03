# Scope
animal = 'Leon' # Variable global -> Función, Condición o Ciclo

def imprimir_animal():
    global animal # con esto vamos utilizar la variable global y la cual se va poder modificar

    animal = 'Ballena'

    # animal = "Ballena" # Variable local

    tipo = "Mamifero" # Variable local

    # las variables locales sólo pueden acceder donde fueron asignadas
    print("linea 5:", animal)
    print("linea 5 id:", id(animal))

imprimir_animal()

print("linea 2:", animal)
print("linea 2 id:", id(animal))


