# Web Scraping: Cómo el Front-end entrega información al navegador, es con HTML, CSS y JS. Usaremos las bibliotecas de
# beautifulsoup4, lxml, requests

import bs4
import requests

resultado_titulo = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

sopa = bs4.BeautifulSoup(resultado_titulo.text,'lxml')

# print(sopa.select('title'))
# print(sopa.select('p'))
# print(len(sopa.select('p')))
# print(sopa.select('title')[0])
# print(sopa.select('title')[0].getText())

# parrafo_especial = sopa.select('p')[3].getText()
# print(parrafo_especial)

'''
Sintaxis para el web Scrapping

Carácter        Sintaxis                        Resultados
    "           soup.select('div)               Todos los elementos con la etiqueta 'div'
    #           soup.select('#estilo_4')        Elementos que contengan id = 'estilo4'
    .           soup.select('.columna_der')     Elementos que contengan class = 'columna_der'
(ESPACIO)       soup.select('div span')         Cualquier elemento llamado 'span' dentro de un elemento 'div'
    >           soup.select('div>span')         Cualquier elemento llamado span dentro del elemento 'div', nada en medio
'''

'''Extraer según las clases'''
# columna_lateral = sopa.select('aside.sidebar-container')
# for p in columna_lateral:
#     print(p.getText())

'''Extraer imagenes'''
# resultado_imagen = requests.get('https://www.escueladirecta.com/courses/')
# sopa2 = bs4.BeautifulSoup(resultado_imagen.text, 'lxml')
#
# images = sopa2.select('img.course-box-image')[0]['src']
# print(images)
#
# imagen_curso_1 = requests.get(images)
# # print(imagen_curso_1.content)
# f = open('imagen.jpg','wb')
# f.write(imagen_curso_1.content)
# f.close()