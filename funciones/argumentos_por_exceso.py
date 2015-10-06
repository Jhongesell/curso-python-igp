#def sumar(a, b, *args, **kwargs):
#     resultado = a + b
#     print por_posicion
#     print por_nombre
#     return resultado

def sumar(a, b, *por_posicion, **por_nombre):
     resultado = a + b
     print por_posicion
     print por_nombre
     return resultado

if __name__ == '__main__':
    print sumar(10, 10, 11, 12, 13, x=14, y=15, z=16)

    a = 10
    b = 10
    args = [11, 12, 13]
    kwargs = {'x': 14, 'y': 15, 'z': 16}
    # No confundir con el uso de *args y **kwargs
    # momento de definir una funcion
    print sumar(a, b, *args, **kwargs)
