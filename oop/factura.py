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

    def __str__(self):
        cadena = ''
        cadena += self.razon_social + ' - '
        cadena += 'RUC: ' + self.ruc
        return cadena


class ErrorFactura(Exception):
    pass

class Factura(Base):

    CONTADOR = 1

    subtotal = 0

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

    def agregarDetalle(self, detalle):
        if (detalle.__class__.__name__ != 'DetalleFactura'):
            raise Exception('el detalle debe ser de tipo "DetalleFactura"')
        self.detalles.append(detalle)
        self.subtotal += detalle.getValorVenta()


    def __str__(self):
        cadena = ''
        cadena += 30 * '*' + '\n'
        cadena += self.empresa_emisora.__str__() + '\n'
        cadena += 'Factura: %03.f-%s' % (self.serie, self.numero) + '\n'
        cadena += 'Fecha: %s' % self.fecha_emision + '\n'
        cadena += 30 * '*' + '\n'
        cadena += self.empresa_receptora.__str__() + '\n'
        cadena += ''.join(['+',51*'-','+']) + '\n'
        for i in self.detalles:
            cadena += i.__str__() + '\n'
        cadena += ''.join(['+',51*'-','+']) + '\n'
        cadena += 'Sub Total: %s' % factura.subtotal + '\n'
        cadena += 'IGV (18%%): %s' % (factura.subtotal * .18) + '\n'
        cadena += 'Total: S/. %s' % (factura.subtotal * 1.18) + '\n'
        return cadena

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

    def getValorVenta(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return '| %02.f | % 30s | % 4s | % 4s |' % (
            self.cantidad,
            self.descripcion,
            str(self.precio_unitario),
            str(self.getValorVenta())
        )


if __name__ == '__main__':
    empresa_emisora = Empresa(
        ruc = '20123456789',
        razon_social = 'Python S.A.C.',
        direccion = 'Av. acb #123'
    )
    empresa_receptora = Empresa(
        ruc = '20987654321',
        razon_social = 'IGP',
        direccion = 'Av. zyx #321'
    )
    factura = Factura(
        empresa_emisora= empresa_emisora,
        empresa_receptora= empresa_receptora,
        numero= 1020
    )
    detalle1 = DetalleFactura(
        factura= factura,
        cantidad= 4,
        descripcion= 'Chompas de Dralom',
        precio_unitario= 70
    )
    detalle2 = DetalleFactura(
        factura= factura,
        cantidad= 2,
        descripcion= 'Chompas de Orlon',
        precio_unitario= 50
    )
    detalle3 = DetalleFactura(
        factura= factura,
        cantidad= 5,
        descripcion= 'Chompas de Lana De Alpaca',
        precio_unitario= 120
    )
    #factura.detalles.append(detalle1)
    #factura.detalles.append(detalle2)
    #factura.detalles.append(detalle3)
    factura.agregarDetalle(detalle1)
    factura.agregarDetalle(detalle2)
    factura.agregarDetalle(detalle3)

#print empresa_emisora
#print empresa_receptora
print factura

#factura.agregarDetalle(detalle1)
