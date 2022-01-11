from abc import ABC, abstractmethod

# class abstract
class EstructuraAbstracta(ABC):
    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass


class Hash(EstructuraAbstracta):
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def agregar(self,llave,valor):
        datos[llave] = valor

class Queue(EstructuraAbstracta):
    datos = []

    def obtener(self):
        datos[0]

    def agregar(self,llave,valor):
        datos[len(datos)-1] = valor
        
class FilaBanco:
    usuarios = {}

    def __init__(self,almacen_usuarios):
        if not isinstance(almacen_usuarios,EstructuraAbstracta):
            raise ValueError("Store is not supported")

    def siguiente_usuario(self):
        # Implementacion
        return self.usuarios.obtener(numero)

    def formar_usuario(self,numero,usuario):
        self.usuarios.agregar(numero,usuario)

FilaBanco(Queue())