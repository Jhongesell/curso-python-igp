

class Ticket:

    id = None

    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo

    def __str__(self):
        return 'Ticket(%d): %s' % (self.id, self.titulo)
