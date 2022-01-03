# Número pares que contengan del 1 al 100

def pares(): # Generador -> Lazy iterator
    for numero in range(0, 12, 2):
        # La función suspende su ejecución de manera temporal
        yield numero


generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print("El generador finalizo.")
        break

