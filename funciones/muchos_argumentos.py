def subrayar(titulo, caracter='=', **kwargs):
    salto_de_linea = kwargs.get('salto_de_linea', False)
    print titulo
    print caracter * len(titulo)
    if salto_de_linea:
        print    

if __name__ == '__main__':
    # Esto falla con TypeError
    # print subrayar('Capitulo 1', '*', True)
    subrayar('Capitulo 1', '*', salto_de_linea=True)
    params = {}
    params['caracter'] = '-'
    params['salto_de_linea'] = True
    subrayar('Capitulo 1', **params)
