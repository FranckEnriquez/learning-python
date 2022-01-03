# los valores fijos siempre van a la derecha
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)

resultado2 = area_circulo(10, 3.141592)
print(resultado2)