class SerVivo:
    def dormir(self):
        print('El ser duerme')

class Animal(SerVivo): # Clase Padre de Mascota y hereda de SerVivo
    def comer(self):
        print('El animal come.')
    
    def dormir(self):
        print('El animal duerme.')

class Mascota(Animal): # Clase padre
    def comer(self):
        super().comer()
        print("La mascota come.")

# la clase perro y mascota heredan todos los métodos de Mascota
'''
class Perro(Mascota): # Clase hija
    pass
'''

class Felino:
    def cazar(self):
        print("El felino caza.")

class Gato(Mascota, Felino): # Clase hija 
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come.')
    
    def dormir(self):
        # con super() se accede a los métodos de la clase padre
        super().comer()
        print(f'{self.nombre} duerme.')

'''
duke = Perro()
duke.comer()
duke.dormir()
'''

patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()
patricio.cazar()
print(patricio.__dict__)