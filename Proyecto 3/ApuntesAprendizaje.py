# Apuntes importantes necesarios para el proyecto:

# Metodo 'index()', sirve para:
    # 1. conocer el indice de un caracter (var.index("[a-Z]"))
    # 2. conocer qué caracter hay en un indice (var[3])

    # mi_texto = "Esta es una prueba"
    # resultado = mi_texto.index("a")
    # print(resultado)

# Extraer sub-strings
    # texto= "ABCDEFGHIJKLM"
    # fragmento = texto[2:10:1]
    # print(fragmento)

# Si quitas el primer parametro toma hasta antes del 5to y si quitas el segundo parámetro toma desde el primer hasta
# el final
# Nota extra, si lo dejas como [::-1] es decir sin parametro de inicio ni limite final, toma toda la secuencia y va
# en reversa


# Funciones adicionales:
    # upper()   - pasar a mayusculas
    # lower()   - pasar a minusculas
    # split()   - separar texto en partes (lista) - Not. dentro del parentesis puedes definir el delimitador
    # join()    - unir items usando separador
    # find()    - encontrar un substring
    # replace() - reemplazar un substring

    # texto = "Este es el texto de Fernando"
    # resultado = texto.replace("e","x")
    # print(resultado)

    # a = "Aprender"
    # b = "Python"
    # c = "es"
    # d = "necesario"
    # e = " ".join([a,b,c,d])
    # print(e)

# Strings
    # palabras = ("""mi casa ich das has perro
    # neos ksal kesak ekesa casaca
    # sorelsa lresala""")
    # print("casacasa" not in palabras)
    # print(len(palabras))

# Listas
    # lista1 = ["a","b","c"]
    # lista2 = ["d","e","d"]
    # lista3 = lista1 + lista2

    # resultado = len(lista1)
    # resultado = lista1[0:2]

    # lista3[0] = 'alfa'
    # lista3.append('g')
    # eliminado = lista3.pop(0) #sin index elimina el ultimo elemento

# Más metodos de listas
    # lista4 = ['a','x','s','v','c']
    # lista4.sort()
    # lista4.reverse()
    # print(lista4)

# Diccionarios
    # diccionario = {'c1':'valor','c2':'valor2'}
    # resultado = diccionario['c1']
    # print(resultado)

    # cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.76}
    # consulta = (cliente['apellido'])
    # print(consulta)

    # dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
    # print(dic['c2'][1])
    # print(dic['c3']['s2'])

    # dic = {'c1':['a','b','c'],'c2':['d','e','f']}
    # print(dic['c2'][1].upper())

    # dic = {1:'a',2:'b'}
    # print(dic)
    # dic[3] = 'c' #Cabe mencionar que el 3 se refiere a la nueva llave y no a la posición
    # print(dic)
    # dic[2] = 'B'
    # print(dic)
    # print(dic.keys())
    # print(dic.values())
    # print(dic.items())

# Tuples - inmutables
    # mi_tuple = (1,2,(10,20),4)
    # print(type(mi_tuple))

    # t = (1,2,3,1)
    # x,y,z = t
    # print(x,y,z)
    # print(t.count(1))
    # print(t.index(2))

# Sets - admite tuplas (por ser inmutable) y no listas ni diccionarios
    # mi_set = set([1,2,3,4,5])
    # print(type(mi_set))
    # set2 = {1,2,3,4,5}
    # print((set2))

    # mi_set = set([1,2,3,4,5])
    # print(len(mi_set))
    # print(2 in mi_set)

    # s1 = {1,2,3}
    # s2 = {3,4,5}
    # s3 = s1.union(s2)
    # sorteo = s1.pop()
    #
    # print(s3)
    # s1.add(4)
    # print(s1)
    # s1.remove(3)
    # print(s1)
    # print(sorteo)
    # s1.clear()
    # print(s1)

# Booleanos
    # num = not(bool(5>6))        # '=' asignar valor, '==' igualdad; puedes usar 'and', 'or' y 'not' tambien
    # print(num)

    # lista = [1,2,3,4]
    # control = 5 in lista
    # print(control)

