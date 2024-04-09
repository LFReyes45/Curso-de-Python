#Mi solución del proyecto: Se debe de hacer un generador de nombres con dos preguntas que queramos, siendo que el nombre
# y presentar el nombre de la marca esten en distintas líneas y que el nombre de la marca esté entre comillas
print("Bienvenido al generador de nombres, te haremos 2 sencillas preguntas que serán el nombre de tu marca\n")

#Solución en una línea
#print("El nombre de tu marca es: \n \""+ input("Nombre de tu canción favorita: ") + " "+input("Nombre de tu animal favorito: ") + "\"")


#Solución más sencilla y estructurada
FPart = input("Nombre de tu canción favorita: ")
SPart = input("Nombre de tu animal favorito: ")
print("El nombre de tu marca es: \n \"" + FPart + " " + SPart + "\"")


#Solución del instructor
#print("El nombre de tu cerveza\nes '" + input("Que ciudad te gustaria visitar?: ") + " " + input("Cual es tu color favorito?: ") + "'\nFelicitaciones!")