import re

r = re.compile('(?P<ministerio>MTC|MVV)-(?P<decreto>[0-9]{3})')

pruebas = ['MTC-005','MVV-002','MTC-002','MVV-102','MTC-423','ABC-123','MTC-1242']

for p in pruebas:
    if r.match(p):
        print p + ' es VALIDA'
        for resultado in r.finditer(p):
            print resultado.groupdict()
    else:
        print p + ' es INVALIDA'


regex = '^/(?P<cat>politica|mundo|tvmas|economia)/(?P<tag>congreso|desastres|farandula|peru|actualidad|justicia)/(?P<slug>[a-z0-9-]+)-(?P<id>[0-9]+)$'

pruebas = ["/politica/congreso/congreso-se-niega-entregar-informacion-pese-que-publica-noticia-1848916",
"/mundo/desastres/argentina-fuerte-sismo-salta-59-grados-deja-muerto-noticia-1848917",
"/tvmas/farandula/natalia-oreiro-da-que-hablar-esta-fotografia-noticia-1848886",
"/economia/peru/que-acusan-corporacion-lindley-y-como-se-defiende-noticia-1848891",
"/politica/actualidad/mauricio-fiol-senti-pena-que-humala-declare-sin-informarse-noticia-1848923",
"/politica/justicia/nadine-heredia-su-defensa-critica-apuro-tc-su-caso-noticia-1848907",
"/mundo/actualidad/chapo-guzman-sufrio-heridas-reciente-huida-dice-mexico-noticia-1848902"]


r = re.compile(regex)

for p in pruebas:
    if r.match(p):
        print p + ' es VALIDA'
        for resultado in r.finditer(p):
            print resultado.groupdict()
            print

    else:
        print p + ' es INVALIDA'