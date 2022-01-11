class User:
    nombre = "Uriel"
    
    # Método constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Método saludar
    def saludar(self, saludo):
        print(saludo + self.nombre)

uriel = User("Marcos")
uriel.saludar("Hola!, mi nombre es:")

"""
-----> Sin método método constructor (__init__)
uriel.nombre = "Marcos" # <- modificación del attr nombre
print(uriel.nombre) 
uriel.saludar()
"""

'''
-----> Sin método método constructor (__init__)
cody = User()
cody.nombre = "Cody"
print(cody.nombre)
'''

# Ejemplo de herencia
class Empleado(User):
    salario = 0

    def modificar_salario(self, salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)

    def saludar(self):
        super().saludar("Hola!") # super <- permite utilizar las propiedades del método padre
     print("Mi nombre es: " + self.nombre + "y gano: " + str(self.salario))

empleado = Empleado("Uriel")
# empleado.saludar("Hola! Me llamo: ") <- con la clase heredada empleado y el nuevo 
# método saludar(), ya se modificó por lo que no recibe las mismas variables
empleado.modificar_salario(1000)
empleado.ver_salario()
empleado.saludar()

# Ejemplo en especifico de como super la palabra "super"
class Pagina:
    def imprimir_pie_pagina(self):
        print(self.pie_pagina)

class PaginaLegal(Pagina):
    def imprimir_pie_pagina(self):
        print("Derechos reservados")
        super().imprimir_pie_pagina()

html = PaginaLegal()
html.pie_pagina = "<p>Hola</p>"

html.imprimir_pie_pagina()