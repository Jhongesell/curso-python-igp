from modelo.ticket import Ticket
from modelo.usuario import Usuario
from controlador.ticket import Ticket as TicketController
import router

t = Ticket(1, 'Arreglar el cluster')
u = Usuario(1, 'Pepe Perez')
print t
print u

router.enrutar()
