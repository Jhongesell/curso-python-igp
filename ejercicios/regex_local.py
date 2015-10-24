import re


regextests = {}

regextests['dni'] = {}
regextests['dni']['regex'] = '^[0-9]{8}$'
regextests['dni']['valid'] = ['43501043','01234567']
regextests['dni']['invalid'] = ['','0','x','1234567','123']

regextests['placa_antigua'] = {}
regextests['placa_antigua']['regex'] = '^[A-Z]{2}-[0-9]{4}$'
regextests['placa_antigua']['valid'] = ['AB-1234','OB-4321']
regextests['placa_antigua']['invalid'] = ['','0','x','AB1234','3124-CA','ab-1234','A-1234','AB-123']

regextests['placa_nueva'] = {}
regextests['placa_nueva']['regex'] = '^[A-Z]{3}-[0-9]{3}$'
regextests['placa_nueva']['valid'] = ['ABC-123','OBF-321']
regextests['placa_nueva']['invalid'] = ['','0','x','AB1234','3124-CA','ab-1234','A-1234','AB-123','AB-1232']


for nombre, rgxtest in regextests.items():
    regex, valid, invalid = rgxtest.values()
    r = re.compile(regex)
    print nombre.upper() + ':'
    print '  Tests Validos:'
    for test in valid:
        if r.match(test):
            res = 'VALIDO'
        else:
            res = 'INVALIDO'
        print '    "%s" : %s' % (test, res)
    print '  Tests Invalidos:'
    for test in invalid:
        if r.match(test):
            res = 'VALIDO'
        else:
            res = 'INVALIDO'
        print '    "%s" : %s' % (test, res)


#r = re.compile('(?P<letras>[a-z]+)-(?P<numeros>[0-9]+)','adsf-1312')
#print r.finditer()
#print [m.groupdict() for m in r ]