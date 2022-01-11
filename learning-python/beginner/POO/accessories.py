class User:
    __edad = 0
    
    # Método constructor
    def __init__(self, nombre):
        self._nombre = nombre

    # Método saludar
    def saludar(self, saludo):
        print(saludo + self.nombre)

    @property # <- getter
    def edad(self):
        return self.__edad

    @edad.setter # <- setter
    def edad(self, valor):
        if(valor < 0):
            raise ValueError("Edad no puede ser menor que 0")
        self.__edad = valor

class Empleado(User):
    __salario = 0

    def modificar_salario(self, salario): # setter <- retorna nuevo valor, altera el valor
        self.__salario = salario

    def ver_salario(self):
        print(self.salario) # <- getter

    def saludar(self):
        super().saludar("Hola!")
        print("Mi nombre es: " + self.nombre + "y gano: " + str(self.__salario))

empleado = Empleado("Uriel")
empleado.edad = 26
print(empleado.edad)