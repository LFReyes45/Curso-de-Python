# Página para practicar el web Scraping: https://toscrape.com/
import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
# resultado = requests.get(url_base.format('1'))
# sopa = bs4.BeautifulSoup(resultado.text,'lxml')
#
# libros = sopa.select('.product_pod')
#
# ejemplo = libros[0].select('a')[1]['title']
# print(ejemplo)

# lista de titulos con 4 o 5 estrellas
titulos_alto = []

# iterar paginas de la web
for pagina in range(1, 51):
    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:
        # checar que sean de alto promedio
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardar el titulo
            titulo_libro = libro.select('a')[1]['title']
            # agregar libro a la lista
            titulos_alto.append(titulo_libro)

# Ver los titulos de más de 4 estrellas en consola
for t in titulos_alto:
    print(t)
