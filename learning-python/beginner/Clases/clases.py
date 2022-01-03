## Attrs de clase
## Attrs de instancia

class Usuario:
    # Definición de la clase
    # métodos

    # __init__
    # object -> todas las clases heredan
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    '''
    def inicializar(self, username, password):
        # self hace referencia al objeto per se
        self.username = username
        self.password = password
    '''

user1 = Usuario("User1", "password1")
user2 = Usuario("User2", "password2")
user3 = Usuario("User3", "password3")

user4 = Usuario()
'''
user1.inicializar("User1", "password1")
user2.inicializar("User2", "password2")
user3.inicializar("Cody", "password3")
'''

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)