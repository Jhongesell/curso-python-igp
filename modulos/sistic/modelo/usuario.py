

class Usuario:

    id = None

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return 'Usuario(%d): %s' % (self.id, self.nombre)

