from controlador.ticket import Ticket as TicketController


def enrutar():
    while (True):
        menu()
        opcion = raw_input('Escoja una opcion: ')
        if opcion == '0':
            exit('Chau ! ')
        if opcion == '1':
            cTicket = TicketController()
            cTicket.listar()

def menu():
    print """
Opciones:
    1) Listar Tickets
    2) Nuevo Ticket
    3) Listar Usuarios
    4) Nuevo Usuario
    5) Asignar Ticket
    0) Salir
"""

