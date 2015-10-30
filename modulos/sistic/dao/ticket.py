

class Ticket:

    def listar(self):
        filas = []
        for fila in [x.strip() for x in open('./tickets.csv').readlines()]:
            filas.append(fila.split(','))
        return filas