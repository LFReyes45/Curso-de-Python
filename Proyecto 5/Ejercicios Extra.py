# Ejercicio 1
'''
Crear una función llamada devolver_distintos que reciba 3 integers como parámetros
Si la suma de los 3 es mayor a 15, devolverá el número mayor
Si la suma es menor a 10, devolverá el menor
Si la suma de los 3 es un valor entre 10 y 15 (incluido), devolverá el valor intermedio
'''


def devolver_distintos(*args):
    suma = sum(args)
    sort = sorted(args)
    if suma > 15:
        return f'el valor máximo es: {max(args)}'
    elif suma < 10:
        return f'el valor mínimo es: {min(args)}'
    elif range(10, 16):
        return f'el valor de mediana es: {sort[1]}'


print(devolver_distintos(8, 0, 1))

# Ejercicio 2
'''
Escribe una función que reciba cualquier palabra como parámetro
y que devuelva todas sus letras únicas en orden alfabético
'''


def remove_duplicates(*args):
    lista = []
    for arg in args:
        for i in arg:
            lista.append(i)
    setting = list(set(lista))
    setting.sort()

    return setting


print(remove_duplicates("Tecnología en México".lower().replace(' ', '')))

# Ejercicio 3

'''
Escribe un función que requiera una cantidad indefinida de argumentos.
La función devolverá True si se ingresa el número cero repetido dos veces consecutivas
'''


def checking(*args):
    i = 0
    lista = list(args)
    while i < len(lista) - 1:
        if lista[i] == lista[i + 1] and lista[i] == 0:
            return True
        else:
            i += 1
    return False


print(checking(5, 6, 1, 0, 0, 9, 3, 5))
print(checking(6, 0, 5, 1, 0, 3, 0, 1))

# Ejercicio 4 - solamente este fue realizado con el instructor

'''
Escribir una función llamada contar_primos() que requiera un solo argumento numérico.
La función mostrará en pantalla todos los númerps primos existentes en el rango que va desde el cero hasta
ese número definido incluido, y devolverá la cantidad de números primos que encontró. El 0 y 1 no cuentan
'''

def contar_primos (limite):
    primos = [2]
    contador = 3
    if limite<=1:
        return 0
    while contador <= limite:
        for i in range(3,contador,2):
            if contador % i == 0:
                contador+=2
                break
        else:
            primos.append(contador)
            contador+=2
    print(primos)
    return len(primos)

print(contar_primos(50))