print(">>>>>>>>>: *args")
def promedio(*args):
    # el prefijo * del nombre del parámetro, se tomará en cuenta todos sus elementos
    print(args)
    print(type(args))

    return sum(args) / len(args)


resultado = promedio(10, 10, 5, 6, 10, 20, 40, 60)
print(resultado)


def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)


print(">>>>>>>>>: **kwargs")
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])

def combinacion2(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion2(1, 2, 3, 4, 5, cody=True, curso='Python', level='Beginner')