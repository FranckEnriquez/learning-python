# los decoradores son una función que toman como input una función y retornan una función
# decoradores -> siempre se trabajará con 3 funciones
'''
Las funciones a, b, c
a -> La función principal (Decorador)
b -> La función de decorar
c -> La función decorada

a(b) -> c
'''
# Estructura base para cualquier función con decoradores
# Decoradores permiten extender funcionales a funciones
def funcion_a(funcion_b):
    
    def funcion_c(*args, **kwargs):
        print(">>>> Antes del llamado.")
        resultado = funcion_b(*args, **kwargs)

        print(">>>> Después del llamado.")

        return resultado 

    return funcion_c


@funcion_a
def sumar(numero_1, numero_2):
    print(numero_1 + numero_2)

resultado = sumar(15, 60)
print(resultado)
