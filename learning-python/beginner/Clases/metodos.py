class Circulo:

    pi = 3.141592

    # cls es sólo por convernción y lo toma como método de instancia y
    # no como método de clase, para ello utilizaremos un decorador

    @classmethod
    def area(cls, radio):
        return cls.pi * radio ** 2

resultado = Circulo.area(14)
print(resultado)