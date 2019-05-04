#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número
# y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

cantidadPalabras = int(input('Dígame cuántas palabras tiene la lista: '))
listaPalabras=[]

for x in range(1,cantidadPalabras+1):
    listaPalabras.append(str(input('Dígame la palabra ' + str(x) + ' : ')))

print('La lista creada es:', listaPalabras)

palabras = int(input('Dígame cuántas palabras tiene la lista: '))

if palabras != len(listaPalabras):
    print('¡Imposible!')
else:
    print('¡Excelente!')

#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
palabraBuscar = str(input('Dígame la palabra a buscar: '))
cantveces = int(listaPalabras.count(palabraBuscar))

if cantveces == 1:
    print("La palabra '" + palabraBuscar + "' aparece una vez en la lista.")
elif cantveces > 1:
    print("La palabra '" + palabraBuscar + "' aparece " + str(cantveces) +" una vez en la lista.")
else:
    print("La palabra '" + palabraBuscar + "' no aparece en la lista.")

#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista

palabraEliminar = str(input('Palabra a eliminar: '))

while palabraEliminar in listaPalabras:
    listaPalabras.remove(palabraEliminar)

print('La lista es ahora:', listaPalabras)

#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

cantidadPalabrasEliminar=int(input('Dígame cuántas palabras tiene la lista de palabras a eliminar: '))
listaPalabrasEliminar = []

for x in range(1,cantidadPalabrasEliminar+1):
    listaPalabrasEliminar.append(str(input('Dígame la palabra ' + str(x) + ' : ')))

print('La lista de palabras a eliminar es:', listaPalabrasEliminar)

for x in listaPalabrasEliminar:
    while x in listaPalabras:
        listaPalabras.remove(x)

print('La lista es ahora:', listaPalabras)

#Escriba un programa que permita crear una lista de palabras y que, a continuación,
#cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

listaPalabrasAlRevez = listaPalabras[::-1]
print('La lista inversa es:',listaPalabrasAlRevez)

#Escriba un programa que permita crear una lista de palabras y que, a continuación,
# elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

listaSinRepeticiones = list(dict.fromkeys(listaPalabras))
print('La lista sin repeticiones es:',listaSinRepeticiones)

#Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
#Lista de palabras que aparecen en las dos listas. Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# Lista de palabras que aparecen en la segunda lista, pero no en la primera. Lista de palabras que aparecen en ambas listas.
# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.


cantidadPalabrasLista2 = int(input('Dígame cuántas palabras tiene la segunda lista: '))
listaPalabras2=[]

for x in range(1,cantidadPalabrasLista2+1):
    listaPalabras2.append(str(input('Dígame la palabra ' + str(x) + ' : ')))

print('La segunda lista es: ', listaPalabras2)

a = set(listaPalabras)
b = set(listaPalabras2)


print('Palabras que aparecen en las dos listas:', a.intersection(b))
print('Palabras que sólo aparecen en la primera lista:', a.difference(b))
print('Palabras que sólo aparecen en la segunda lista: ', b.difference(a))
print('Todas las palabras: ', a.union(b))