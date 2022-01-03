promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

print(promedio(10, 2, 3, 4, 5))
print(aprobatorio(7))

def es_aprobatorio(calificacion):
    return calificacion >= 90

# CALLBACKS
def mostrar_mensaje(func_prom, func_aprobatorio, *args):
    promedio = func_prom(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print(f'No aprobaste la materia')

mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)
mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 7, 7)

