def generarador_numeros(area, x=0):
    while True:
        x += 1
        yield f'{area}{x}'


generadorperf = generarador_numeros('P-')
generadorfarm = generarador_numeros('F-')
generadorcos = generarador_numeros('C-')
