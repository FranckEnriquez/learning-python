class User:
    nombre = "Uriel"
    
    # Método constructor
    def __init__(self, nombre):
        self.nombre = nombre

    # Método saludar
    def saludar(self, saludo):
        print(saludo + self.nombre)

class Empleado(User):
    __salario = 0

    def modificar_salario(self, salario): # setter <- retorna nuevo valor, altera el valor
        self.__salario = salario

    def ver_salario(self):
        print(self.salario) # <- getter

    def saludar(self):
        super().saludar("Hola!")
     print("Mi nombre es: " + self.nombre + "y gano: " + str(self.__salario))

class Administrativo(Empleado):
    def mi_salario(self):
        print(self.__salario) # <- no puede acceder porque es una clase privada