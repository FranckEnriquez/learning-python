e = 'e' # Variables global

def funcion_principal():
    a = 'a' # Variables locales con mayor alcance
    b = 'b'

    def funcion_anidada():
        c = 'c' # Variables locales con menor alcance
        nonlocal b 
        # sirve para modificar una variable local con mayor alcance, la linea 5
        b = 'Cambio de valor'

        print(a)
        print(b)
        print(id(b))

        print(e)

        funcion_anidada()
        # print(c)
        print(b)
        print(id(b))

funcion_principal()