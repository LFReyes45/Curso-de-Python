class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, cuenta, balance):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta  # Número de cuenta
        self.balance = balance  # Balance de la cuenta

    def __str__(self):
        return (f'Hola {self.nombre} {self.apellido}, tu número de cuenta {self.cuenta} tiene un saldo de '
                f'${self.balance}')

    def depositar(self, deposito):
        self.balance += deposito
        return self.balance

    def retirar(self, retiro):
        if self.balance >= retiro:
            self.balance -= retiro
            print(f'Has retirado {retiro}, tu cuenta tiene ahora {self.balance}')
        else:
            print('Saldo insuficiente, ingrese un monto valido')


def inicio():
    clients = ingresar_usuario()
    print(clients)
    seleccion = ''
    while seleccion != '3':
        seleccion = input('''¿Qué acción deseas realizar?
        1. Depositar dinero
        2. Retirar dinero
        3. Salir\n→''')
        if not seleccion.isdigit():
            print('Elige un número válido')
        else:
            if 0 > int(seleccion) > 3:
                print('Elige un número dentro del rango')
            else:
                if seleccion == '1':
                    deposito = float(input('Ingrese el monto a depositar: $'))
                    clients.depositar(deposito)
                    print(f'Tu cuenta tiene ${clients.balance}')
                elif seleccion == '2':
                    retirar = float((input('Ingrese el monto a retirar: $')))
                    clients.retirar(retirar)
                else:
                    seleccion = '3'


def ingresar_usuario():
    cuenta = ''
    balance = 0
    nombre = input('Hola y Bienvenido a tu cuenta de banco, por favor, ingresa tu(s) nombre(s) de pila: \n')
    apellido = input('Ahora ingresa tus apellidos: \n')
    while len(cuenta) != 10 or not cuenta.isdigit():
        cuenta = input('Por último, ingresa tu número de cuenta: \n')
    clients = Cliente(nombre, apellido, cuenta, balance)
    return clients


inicio()
print('Gracias por visitarnos y esperamos verte pronto')
