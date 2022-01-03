def saludar(username): 
    # closure -> retorna una función aún cuando la primera función haya terminado
    mensaje = f'Hola {username}' # Variable local

    def mostrar_mensaje(): # Anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)

username = 'Eduardo'
# closures siguen teniendo memoria, a pesar de que referencias el attr de la clase a otro valor, es decir a la variable local
respuesta()


# CLOSURES son funciones que retornan funciones las cuáles a su vez aún pueden acceder a variables locales