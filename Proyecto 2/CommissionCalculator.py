# Programa que calcule la comisión del 13%, en el que pregunte el nombre al usuario y cuánto vendió

# Mi Solución
print("Bienvenido a la calculadora de comisiones, FYI la comisión que recibes de las ventas totales es del 13%")
nombre = input("¿Cómo te llamas?: ")
ventas = float(input("¿Cuánto vendiste en el mes?: $"))
total = round(((ventas * 13) / 100), 2)

print(f"Hola {nombre}, tu comisión es de: ${total}")

# Solución del instructor
nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

comision = round(ventas * 13 / 100, 2)

print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
