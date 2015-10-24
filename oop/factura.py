#!/usr/env/bin python
# -*- coding: utf8 -*-

import datetime

class Base(object):

    ATRIBUTO_OBLIGATORIO = 1
    ATRIBUTO_OPCIONAL = 2

    @classmethod
    def validar_parametros(cls, kwargs):
        # Identificar atributos no reconocidos
        for k in kwargs:
            if k not in cls.ATRIBUTOS:
                msg = u'Atributo \'%s\' no reconocido'
                raise ErrorFactura(msg % k)
        # Identificar atributos faltantes
        for atributo, tipo in cls.ATRIBUTOS.iteritems():
            if tipo == cls.ATRIBUTO_OBLIGATORIO and \
                atributo not in kwargs:
                    msg = 'El atributo \'%s\' no fue encontrado'
                    raise ErrorFactura(msg % atributo)

    def __init__(self, **kwargs):
        self.__class__.validar_parametros(kwargs)
        for k,v in self.__class__.DEFAULTS.iteritems():
            kwargs.setdefault(k, v)
        for k in kwargs:
            setattr(self, k, kwargs[k])


class Empresa(Base):

    ATRIBUTOS = {
        'ruc': Base.ATRIBUTO_OBLIGATORIO,
        'razon_social': Base.ATRIBUTO_OBLIGATORIO,
        'direccion': Base.ATRIBUTO_OBLIGATORIO,
        'telefono': Base.ATRIBUTO_OPCIONAL
    }

    DEFAULTS = {
        'telefono': None
    }

class ErrorFactura(Exception):
    pass

class Factura(Base):

    CONTADOR = 1

    ATRIBUTOS = {
        'empresa_emisora': Base.ATRIBUTO_OBLIGATORIO,
        'empresa_receptora': Base.ATRIBUTO_OBLIGATORIO,
        'numero': Base.ATRIBUTO_OBLIGATORIO,
        'detalles': Base.ATRIBUTO_OPCIONAL,
        'guia_remision': Base.ATRIBUTO_OPCIONAL,
        'serie': Base.ATRIBUTO_OPCIONAL,
        'fecha_emision': Base.ATRIBUTO_OPCIONAL
    }

    DEFAULTS = {
        'serie': 1,
        'fecha_emision': datetime.datetime.now().date(),
        'detalles': [],
        'guia_remision': None
    }

class DetalleFactura(Base):

    ATRIBUTOS = {
        'factura': Base.ATRIBUTO_OBLIGATORIO,
        'cantidad': Base.ATRIBUTO_OPCIONAL,
        'descripcion': Base.ATRIBUTO_OBLIGATORIO,
        'precio_unitario': Base.ATRIBUTO_OBLIGATORIO
    }

    DEFAULTS = {
        'cantidad': 1
    }


if __name__ == '__main__':
    pass

