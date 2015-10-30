from dao.ticket import Ticket as DaoTicket


class Ticket:

    def listar(self):
        print '\nListar Tickets...'
        dTicket = DaoTicket()
        print dTicket.listar()


    def nuevo(self):
        print 'Nuevo Ticket...'

