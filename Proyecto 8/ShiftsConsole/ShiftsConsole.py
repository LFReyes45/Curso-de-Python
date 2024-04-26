import NumbersGenerator


def decorar_saludo(funcion):
    def otra_funcion():
        print('\n***************************')
        print(f'Su turno es: {next(funcion)}\nEspere un momento, se le atenderá en breve')
        print('***************************\n')

    return otra_funcion


def boletos():
    continuar = ''
    while continuar != 's' and continuar != 'n':
        continuar = input('¿Deseas salir del programa? (s/n): ').lower()
    return continuar


val = 0
while True:
    try:
        val = int(input('Hola y bienvenido a este programa, de qué area requieres atención: '
                        '\n1. Perfumería'
                        '\n2. Farmacia'
                        '\n3. Cosméticos'
                        '\n4. Salir del programa'
                        '\n→ '))
    except ValueError:
        print('********** Procura eligir un número, no un carácter **********\n')
    else:
        if val < 1 or val > 4:
            print('********** Elige un número dentro del rango **********\n')
            continue
        else:
            match val:
                case 1:
                    perf = decorar_saludo(NumbersGenerator.generadorperf)
                    perf()
                case 2:
                    far = decorar_saludo(NumbersGenerator.generadorfarm)
                    far()
                case 3:
                    cos = decorar_saludo(NumbersGenerator.generadorcos)
                    cos()
                case 4:
                    break
            salida = boletos()
            if salida == 's':
                break
