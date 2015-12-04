

class HelperTicket(object):

    def __init__(self, p):
        self.p = p

    def __str__(self):
        return 'ejemplo 3: ' + self.p

    #def __unicode__(self):
    #    return 'ejemplo 4: ' + self.p

    def __call__(self):
        return 'ejemplo 2: ' + self.p

