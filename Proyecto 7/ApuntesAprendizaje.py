# Este proyecto es importante, es de la POO (Programación Orientada a Objetos) - Primero lo teórico

'''
POO - Es un modo de programación que nos permite organizar el código de una manera que se asemeja a cómo pensamos,
diseñando objetos digitales a los que podemos crear, manipular o destruir.

    Clase : Código que define a un objeto. Nos permiten agrupar un conjunto de variables y funciones para que nuestros
    objetos tengan vida. (Silla, edificio, pajaro).

    Atributos : En el ejemplo del pájaro, podemos definir distintas caracteristicas que podrían ser su color, tipo de
    pájaro, hábitat, edad, tamaño. Las características son atributos

    Métodos - las clases tienen un conjunto de funcionalidad o cosas que pueden hacer. Con el pajaro, volar, comer o
    piar.

    Objetos - Podemos hacer que existan muchos pajaros, cada pajaro es distinto y que en tu programa será creado desde
    la clase de pajaro. Podemos tener un Pepe, Twitty, Ricardo. El concepto abstracto de pájaro es la clase pero Pepe o
    cualqueir otro pajaro sería un objeto, una instancia de la clase (yo - es como el instanciamiento en Java que vi).
    Cada instancia de la clase objeto será considerada como objeto.

La POO está basada en seis principios o pilares básicos, los cuales son:
    • Herencia
    • Polimorfismo
    • Cohesión
    • Abstracción
    • Acoplamiento
    • Encapsulamiento
'''

'''Pasamos a las Clases'''

# Para crear una clase, se defienn de la siguiente forma

# class Pajaro:
# Código interno

# Por convención se escribe como se propuso de ejemplo, capitalizando cada palabra si fuera Elemento sería,
# class ElementoPajaro:

# Para el instanciamiento se llamaría de la siguiente forma:
# mi_pajaro = Pajaro([puedes enviar argumentos])

''' ***********EJEMPLO****************'''

# class Pajaro:
#     pass
#
#
# mi_pajaro = Pajaro()
# otro_pajaro = Pajaro()
# print(mi_pajaro)
# print(otro_pajaro)

'''Pasamos a los Atributos'''

# Existen dos tipos de atributos
# • Atributos de clase: Se tratan de atributos que pertenecen a la clase y, por tanto, serán los mismos para todos
# los objetos que vayan a ser creados desde esta clase. Por ejemplo, si nuestra clase tiene
# el atributo (alas = True), eso significa que todos los pajaros tendrán ese atributo
# • Atributos de instancia: Pertenecen a la instancia de la clase o al objeto. Son atributos particulares que pueden
# ser distintos en cada instancia. Por ejemplo, el color tendrá un valor distinto para
# cada pájaro que vayamos a crear.

''' EJEMPLOS ATRIBUTOS DE INSTANCIA'''

'''*****************************************************************************************************************'''
# class Pajaro:
#     alas = True     #Este es un atributo de tipo clase
#
#     def __init__(self,mi_color,especie): # Este es el método constructor que asignará atributos a nuestro pajaro en el parentesis.
#         self.color = mi_color    # self es la instancia del objeto que se va a crear a cada uno de los pájaros que creemos
#         self.especie = especie
#
# mi_pajaro = Pajaro('Negro','Tucán')
#
# print(f'Mi pájaro es un {mi_pajaro.especie} de color {mi_pajaro.color} y con {mi_pajaro.alas}')
'''*****************************************************************************************************************'''

'''Notas por mencionar'''
# En la explicación, init es un método , el constructor de la clase. Cada vez que creamos una clase, Python llamará
# automáticamente a su constructor para ver qué necesita para crearse adecuadamente. self representa la instancia del
# objeto que vaya a ser creado. Python exige que siempre pongamos self de modo explicito. Y como podemos ver en el
# el metodo 'color' es Atributo y 'mi_color' es el parámetro

'''Pasamos a los Métodos'''

# Para los métodos de una clase, ya lo hemos hecho con el '__init__', que de hecho es especial y viene incorporado
# en todas las clases por defecto. Métodos que le den funcionalidades a nuestras clases. Es lo que ya hemos visto
# con las funciones ya que basicamente es lo mismo.

# class Pajaro:
#     def __init__(self,color,especie):
#         self.color = color
#         self.especie = especie
#
'''Con los métodos se vería así uno'''
#     def piar(self):
#         # Código
#
#     def volar (self,metros):
#         print(f'Voló {metros}mts')


# Cosas por mencionar es que, la unica diferencia con las variables es que dentro de las clases siempre vamos a pasar
# al menos un argumento obligatorio, que es la palabra 'self', que hace referencia a cada instancia o cada objeto de la
# clase y luego poner dentro el código

'''EJEMPLOS DE LOS MÉTODOS'''
'''*****************************************************************************************************************'''
# class Pajaro:
#     alas = True
#
#     def __init__(self,color,especie):
#         self.color = color
#         self.especie = especie
#
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color))
#
#     def volar(self,metros):
#         print(f'El pajaro ha volado {metros} metros')
#
# piolin = Pajaro('Amarillo','Canario')
#
# piolin.piar()
# piolin.volar(50)
'''*****************************************************************************************************************'''

'''Notas'''
# Para el método de piar, que hemos invocado el color, cada vez que dentro de la clase construyamos un método que
# invoque a un atributo, necesitamos relacionar a quién pertenece ese atributo, pertenece al objeto o la instancia que
# está invocando a este metodo y 'self' realiza esta asociación

'''Tipos de Métodos'''

# • Métodos de instancia: Son los que una vez fueron creados, pueden ser llamados, pueden acceder y modificar los
#                         atributos del objeto, acceder a otros métodos, modificar el estado de la clase.
#     def mi_metodo(self):
#         print('algo')

# • Métodos de clase @classmethod: Se definen con la palabra clave @classmethod, y pondremos en sus parametros cls, estos
#                                  metodos no estan asociados a las instancias de nuestra clase si no en la clase en si
#                                  misma. Pueden ser llamados desde la clase. No pueden acceder a atributos de la instancia
#     @classmethod
#     def mi_metodo(cls):
#         print('algo')

# • Métodos estáticos @staticmethod: No aceptan ni self ni cls, no pueden modificar los estados ni de la clase ni la
#                                    instancia, pueden aceptar parametros de entrada. Son como funciones normales
#     @staticmethod
#     def mi_metodo(cls):
#         print('algo')

'''EJEMPLOS DE TIPOS DE METODOS'''

# class Pajaro:
#     alas = True
#
#     def __init__(self, color, especie):
#         self.color = color
#         self.especie = especie
#
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color))
#
#     def volar(self, metros):
#         print(f'El pajaro ha volado {metros} metros')
#         self.piar()
#
#     def pintar_negro(self):
#         self.color = 'negro'
#         print(f'Ahora el pajaro es {self.color}')
#
#     @classmethod
#     def poner_huevos(cls, cantidad):  #No pueden acceder a los atributos de la instancia pero si al de clase
#         print(f'Puso {cantidad} huevos')
#         cls.alas = False
#
#     @staticmethod       #No modificar metodos ni las instancias
#     def mirar():
#         print('El pajaro mira')
#
#
# Pajaro.mirar()

'''Herencia'''

# Un ejemplo de la herencia es esta:
# class Animal:
#     def nacer(self):
#     def morir(self):
#     def respirar(self):
#
# class Pajaro (Animal):
#     [codigo]
# class Mamifero(Animal):
#     [codigo]
# class Insecto(Animal):
#     [codigo]

'''EJEMPLO HERENCIA'''

# class Animal:
#
#     def __init__(self,edad,color):
#         self.edad = edad
#         self.color = color
#     def nacer(self):
#         print('Este animal ha nacido')
#
#     def hablar(self):
#         print('Este animal emite un sonido')
#
# class Pajaro(Animal):
#     pass
#
# piolin = Pajaro(2,'amarillo')

# print(piolin.color)

'''HERENCIA EXTENDIDA'''
# Un ejemplo de esto se pudiera representar como:
# class Padre:
#     def metodo1(self):
#         [codigo]
#
# class Hija(Padre):
#     • Métodos heredados
#     • Métodos modificados
#     • Métodos nuevos

'''EJEMPLO DE HERENCIA EXTENDIDA'''

# class Animal:
#
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
#
#     def nacer(self):
#         print('Este animal ha nacido')
#
#     def hablar(self):
#         print('Este animal emite un sonido')
#
#
# class Pajaro(Animal):
#     def __init__(self,edad,color,altura_vuelo):
#         super().__init__(edad,color)
#         self.altura_vuelo = altura_vuelo
#     def hablar(self):
#         print('pio')
#     def volar(self,metros):
#         print(f'El pajaro vuela {metros} metros')
#
#
# piolin = Pajaro(3, 'amarillo',100)
# mi_animal = Animal(5,'negro')
# piolin.volar(100)

'Segundo ejemplo'
# class Padre:
#     def hablar(self):
#         print('Hola')
#
# class Madre:
#     def reir(self):
#         print('ja ja')
#
#     def hablar(self):
#         print('que tal')
#
# class Hijo(Padre,Madre):
#     pass
#
# class Nieto (Hijo):
#     pass
#
# mi_nieto = Nieto()
# mi_nieto.hablar()
# print(Nieto.mro())

'''POLIMORFISMO'''
# Ejemplo explicado de polimorfismo

# mi_perro.hablar()
# mi_pajaro.hablar()
# mi_madre.hablar()
# mi_abogado.hablar()
# mi_estudiante.hablar()
#
# for ser in lista:
#     ser.hablar()

'''EJEMPLOS DE POLIMORFISMO'''

# class Vaca:
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#     def hablar(self):
#         print(self.nombre + ' dice mu')
#
#
# class Oveja:
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#     def hablar(self):
#         print(self.nombre + ' dice beee')
#
#
# vaca1 = Vaca('Aurora')
# oveja1 = Oveja('Nube')
#
# animales = [vaca1, oveja1]
#
#
# # for animal in animales:
# #     animal.hablar()
# def animal_habla(animal):
#     animal.hablar()
#
#
# animal_habla(vaca1)

'''Cohesión'''
# La cohesión se refiere al grado de relación entre los elementos de un módulo. Cuando diseñamos una función, debemos
# identificar de un modo específico qué tarea va a realizar, reduciendo su finalidad a un objetivo único y definido.

# En resumen: para que una función sea cohesiva debe hacer solo una cosa, y si tiene que hacer más de una cosa, estas
# deben tener una alta relación entre sí. Existen dos tipos de cohesión:

# •Cohesión débil: indica que la relación entre los elementos es baja, y por lo tanto no tienen una única funcionalidad.
# •Cohesión fuerte: indica que existe una alta relación entre los elementos existentes dentro del módulo. Este debe ser
#                  nuestro objetivo al diseñar programas.

'''EJEMPLO DE COHESIÓN'''

# def suma(num1,num2):            # Cohesión fuerte, ya que se realiza solo una operación
#     resultado = num1+num2
#     return resultado
#
# def suma():                     #Cohesión débil porque realiza distintas funcionalidades
#     num1 = float(input('Elige un número: '))
#     num2 = float(input('Elige otro numero: '))
#     resultado = num1 + num2
#     return resultado
#
# def suma(lista_numeros):
#     resultado = 0
#     for n in lista_numeros:
#         resultado += n
#     return resultado

'''Acoplamiento'''
# El acoplamiento es un concepto que mide la dependencia entre dos módulos distintos (como por ejemplo, clases).
# Podemos hablar de dos tipos:

# •Acoplamiento débil: Implica que no hay dependencia entre un módulo y otros. Esta es la situación ideal.
# •Acoplamiento fuerte: Es la situación contraria, e indica que el módulo tiene dependencias internas con otros.

# Se trata de un pilar vinculado con la cohesión, ya que por lo general un acoplamiento débil se asocia a una cohesión
# fuerte. Esta última es la situación buscada al escribir código. Es decir, buscamos que una clase o función no tenga
# dependencias con otras clases o funciones, y que las tareas que realizan estén relacionadas entre sí. Esto simplifica
# la lectura y mantenimiento del código , a la vez que permite reutilizarlo en otros programas.

'''EJEMPLO DE ACOPLAMIENTO'''

# class Mascota:                          # Ejemplo de Acoplamiento fuerte
#     tiene_patas = True
#     pass
#
#
# class Perro:
#     def correr(self, velocidad):
#         if Mascota.tiene_patas:
#             self.velocidad = velocidad
#
#
# mi_mascota = Perro()
# mi_mascota.correr("rápido")
# print(mi_mascota.velocidad)
#
# class Mascota:                         # Ejemplo de Acoplamiento débil
#     def tiene_patas(self):
#         return True
#
# class Perro(Mascota):  # Perro hereda de Mascota
#     def correr(self, velocidad):
#         if self.tiene_patas():
#             self.velocidad = velocidad
#
# mi_mascota = Perro()
# mi_mascota.correr("rápido")
# print(mi_mascota.velocidad)

'''Abstracción'''

# La abstracción es el pilar de la programación orientada a objetos que se relaciona con ocultar toda la complejidad
# que algo puede tener por dentro, ofreciendo una interfaz con funciones de alto nivel, por lo general sencillas de
# usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que hay dentro.

# Un ejemplo simple de abstracción en Python sería una clase Vehículo, que tiene métodos para arrancar, detener y
# conducir. Los detalles internos de cómo se implementan estos métodos, como si el vehículo funciona con gasolina o
# electricidad, o qué tipo de motor tiene, están ocultos al usuario de la clase. El usuario solo necesita saber que
# puede usar estos métodos para controlar el vehículo.

'''Encapsulamiento'''

# El encapsulamiento es el pilar de la programación orientada a objetos que se relaciona con ocultar al exterior
# determinados estados internos de un objeto, tal que sea el mismo objeto quien acceda o los modifique, pero que dicha
# acción no se pueda llevar a cabo desde el exterior, llamando a los métodos o atributos directamente.

# Si bien en algunos lenguajes (como Java), puede resultar un procedimiento habitual, Python no lo implementa por
# defecto, pero nos propone una vía alternativa para lograrlo. Esto se hace anteponiendo dos guiones bajos (__) al
# nombrar un método o atributo. De esa manera, los mismos quedarán definidos como “privados”, y únicamente el mismo
# objeto podrá acceder a ellos.

'''EJEMPLO'''

# class Persona:
#
#     atributo_publico = "Mostrar"   # Accesible desde el exterior
#     __atributo_privado = "Oculto"  # No accesible
#
#     # No accesible desde el exterior
#     def __metodo_oculto(self):
#         print("Este método está oculto")
#         self.__variable = 0
#
#     # Accesible desde el exterior
#     def metodo_normal(self):
#         # El método si es accesible desde el interior
#         self.__metodo_oculto()
#
#
# alumno = Persona()
# # alumno.__metodo_oculto()  # Este método no es accesible desde el exterior
# alumno.metodo_normal()      # Este método es accesible

'''Métodos Especiales'''

# Son métodos que son como "__nombre__", algunos son "__init__", "__mro__", "__bases__", "__subclases". Son usados para
# crear funcionalidades que no pueden ser representadas en un método regular.

'''EJEMPLO'''


class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print('Se ha eliminado el nombre del CD')


mi_cd = CD('The Beatles', 'Please Please Me', 14)

print(len(mi_cd))
