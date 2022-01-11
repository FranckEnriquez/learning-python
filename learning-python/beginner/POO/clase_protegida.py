class User:
    nombre = "Uriel"
    
    # Método constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Método saludar
    def saludar(self, saludo):
        print(saludo + self.nombre)
        
class Empleado(User):
    salario = 0

    def modificar_salario(self, salario):
        self._salario = salario

    def ver_salario(self):
        print(self.salario)

    def saludar(self):
        super().saludar("Hola!")
     print("Mi nombre es: " + self.nombre + "y gano: " + str(self._salario))