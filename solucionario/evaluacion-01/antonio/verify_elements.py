#!/usr/bin/env python
# -*- coding: utf8 -*-

def verify_elements(vf, default=[]):
    def decorator(f):
        def aux(*args, **kwargs):
            output = f(*args, **kwargs)
            check = reduce(
                lambda a, b: a and b,
                map(vf, output),
                True
            )
            if check:
                return output
            else:
                return default
        return aux
    return decorator

def verify_elements_alt(vf, default=[]):
    def decorator(f):
        def aux(*args, **kwargs):
            output = f(*args, **kwargs)
            check = True
            for val in output:
                if vf(val) == False:
                    check = False
                    break
            if check:
                return output
            else:
                return default
        return aux
    return decorator

if __name__ == '__main__':

    f1 = lambda x: [2, 4, 6, 8]
    f1 = verify_elements(lambda x: x % 2 == 0)(f1)
    print f1(10) # Cualquier valor, es ignorado

    f2 = lambda x: [2, 4, 7, 8]
    f2 = verify_elements(lambda x: x % 2 == 0, None)(f2)
    print type(f2(10))

    f1 = lambda x: [2, 4, 6, 8]
    f1 = verify_elements_alt(lambda x: x % 2 == 0)(f1)
    print f1(10) # Cualquier valor, es ignorado

    f2 = lambda x: [2, 4, 7, 8]
    f2 = verify_elements_alt(lambda x: x % 2 == 0, None)(f2)
    print type(f2(10))
