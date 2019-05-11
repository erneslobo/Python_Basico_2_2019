#Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona.
# La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco,
# la segunda columna la cantidad en crédito en miles de colones y
# la tercer columna en miles de colones en deuda.

hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
print(b) #sea b la tabla resultante luego de aplicar transpuesta

#Por otro lado, se puede aplicar matemática o cualquier otra operación a alguna fila en específico.
# Por ejemplo: dividir todos los números entre 10. Obteniendo:


#b[1] = list(map(lambda x: x/10, b[1]))
#print(b)
#print(b[1::])

#Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:
#Promedio
#La suma
#La multiplicación

import functools

promedio = lambda x,y : x / y
suma = lambda x,y : x + y
multiplicacion = lambda x,y : x * y
intereses = lambda x: x*1.20

fm = {
    'promedio' : promedio,
    'suma' : suma,
    'multiplicacion' : multiplicacion,
    'intereses' : intereses
}

#Obtenga utilizando el diccionario de funciones:
#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.

print('El promedio de la cantidad miles de colones en débito:', (fm['promedio'])(sum(b[1]),len(b[1])))

#2. La suma de todas las deudas

print('La suma de todas las deudas:',functools.reduce(fm['suma'],b[3]))

#3. la multiplicación de todos los crédito entre si
print('La suma de todas las deudas:',functools.reduce(fm['multiplicacion'],b[2]))

#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20% (esto es multiplicar por 1.2) a toda la fila de créditos usando el diccionario de funciones.

b[2] = list(map(fm['intereses'], b[2]))

print(b)

pass





