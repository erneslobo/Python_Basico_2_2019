#Responder las preguntas de manera directa utilizando ejemplos.

#Cuáles son las diferencias en la lista y la tupla?

tupla = (1,2,3,4)
print(type(tupla))
print(tupla)
print(tupla[1])
print(len(tupla))

lista = [1,2,3,4]
print(type(lista))
print(lista)
print(lista[1])
lista.append(6)
print(lista)
lista.insert(4, 5)
print(lista)
lista.remove(6)
print(lista)
del lista[1]
print(lista)
del lista[:]
print(lista)
print(len(lista))


#Cómo se puede usar expresiones if else en una sóloa línea, comúnmente llamadas operaraciones ternarias

var=1
resultado="Tiene valor" if var>0 else "No tiene valor"

#Para que sirve dir() y help()?

#help() se usan para retornar documentacion de python de un objecto, metodo, atributo, etc en particular
my_list = []
help(my_list.append)

#dir() muestra la lista de attributos de un objecto

my_list = []
print(dir(my_list))


#Que son diccionarios?

#Un Diccionario es una estructura de datos y un tipo de dato en Python con características
# especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas,
# listas e incluso otras funciones. Estos diccionarios nos permiten además identificar
# cada elemento por una clave (Key).

diccionario = {'nombre' : 'Carlos',
               'edad' : 22,
               'cursos': ['Python','Django','JavaScript']
                }


#Que son *args y **kwargs ? Como se usan?

'''para que una función tome una cantidad indefinida de argumentos, se utiliza la expresión *args.'''

def f(*args):
    return print(args)

f(1, 5, True, False, "Hello, world!")

'''De forma análoga funcionan los keyword arguments, que son representados con dos asteriscos (**) y el nombre kwargs.
Cabe destacar que los nombres de estos parámetros son indiferentes; args y kwargs son utilizados simplemente por convención.

En este caso kwargs es un diccionario que contiene el nombre de cada uno de los argumentos junto con su valor. Siendo esto así, el orden de los mismos es indistinto.'''

def f(**kwargs):
    return print(kwargs)

f(a=1, b=True, h=50, z="Hello, world!")


'''Ambos métodos pueden ser implementados en una misma función como excepción al error de sintaxis.'''

def f(*args, **kwargs):
    return args, kwargs

args, kwargs = f(True, False, 3.5, message="Hello, world!", year=2014)
print(args)
print(kwargs)

#Qué son índices negativos?

'''Los índices pueden ser enteros negativos tambien. El concepto es sencillo:
lista[-1] hace mención al último elemento de la lista; lista[-2] al penúltimo, y así sucesivamente.'''

semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes',
   'sábado', 'domingo']

# Primer elemento de la lista desde dos ópticas
print('Primer elemento de la lista empleando índices positivos: ',
   semana[0])
print ('Primer elemento de la lista empleando índices negativos: ',
    semana[-len(semana)])

print ('-------------------------------') # Separador

# Último elemento de la lista desde dos ópticas
print('Último elemento de la lista empleando índices positivos: ',
   semana[len(semana) - 1])
print ('Último elemento de la lista empleando índices negativos: ',
    semana[-1])

#Como se puede order aleatoriamente -o desordenar- una lista?

from random import shuffle
for i in range(12):
    lista = ['A', 'K', 'Q']
    shuffle(lista)
    print(lista)

#Como se puede ordenar una lista ?

nombres_masculinos = ['Jose', 'Jose', 'Ricky', 'Jacinto', 'David', 'Alvaro', 'Ricky']

##Ordenar una lista en reversa (invertir orden)

nombres_masculinos.reverse()

#Ordenar una lista en forma ascendente

nombres_masculinos.sort()

#Ordenar una lista en forma descendente

nombres_masculinos.sort(reverse=True)

#Explique o justifique los resultados de A0,A1,A2,A3,A4,A5,A6 ?

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

'''zip basicamente mapea el conjunto a con el conjunto b basados en la posicion y con dict se crea un diccionario'''

A1 = range(10)

'''Funcion que genera numeros enteros entre dos numero, si se usa solo un arguemento el rango seria entre 0 y el interger que se pone como argumento'''

A2 = sorted([i for i in A1 if i in A0])

'''A2 create una lista vacia, porque se trata de comparar numero en A1 con los keys del dictionario creado en A0 '''

A3 = sorted([A0[s] for s in A0])

'''Crea una lista en orden ascendente de los valores del dictionario A0. Se utiliza el for para recorrer A0, s es el valor de cada key'''

A4 = [i for i in A1 if i in A3]

'''Crea una lista con valores de 1 a 5, que son los valores que esan en A3 y A1.'''

A5 = {i:i*i for i in A1}

'''Se genera una diccionario, donde el key son los valores de A1, y los valores es el valor en A1 multiplado por el mismo'''

A6 = [[i,i*i] for i in A1]

'''se genera una lista de lista donde cada lista tiene como elementos 2 valor, valores de A1 y el mismo valor multiplicado por el mismo'''

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)


#Cómo se pueden generar números aleatorios? enteros y decimales

'''La biblioteca random contiene una serie de funciones relacionadas con los valores aleatorios
El modulo random proporciona un generador de números aleatorios'''

import random

#random.randrange([start,] stop [,step]) , random.randrange(stop)

print (random.randrange(10))

#Nos devolverá un numero aleatorio entre 0 y 9 (el 10 no es incluido en el rango)

print (random.randint(0, 5)) #La salida va a ser: 0, 1, 2, 3, 4 o 5

print (random.randrange(1, 12, 2)) #Las opciones son (1, 3, 5, 7, 9, 11)
print (random.randrange(0, 11, 2)) #Las opciones son (0, 2, 4, 6, 8, 10)

#Nos devolverá un numero aleatorio entre 0 y 10 contando de 2 en 2 (0, 2, 4, 6, 8, 10)

'''random.choice(secuencia)'''

#Devuelve un elemento aleatorio de una secuencia no vacía.
random.choice(["rojo", "negro", "verde"])

'''random.random()

Devuelve un numero aleatorio de punto flotante entre 0.0 y 1.0
También se puede utilizar de la siguiente manera:'''

random.random() * 100 #Nos devuelve un numero de punto flotante entre 0.0 y 100.0

'''random.uniform(a, b)

Al igual que random.random, devuelve un numero de punto flotante entre a y b:'''

random.uniform(1, 2)  # Devuelve un numero aleatorio entre 1.0 y 2.0

''''Generar números enteros: la función randint()
La función randint(a, b) genera un número entero entre a y b, ambos incluidos. a debe ser inferior o igual a b.'''

print(random.randint(10, 20))

#Qué es pickling y unpickling?

'''El módulo pickle implementa un algoritmo básico pero potente de ``estibar'' (o serializar, encurtir o aplanar) objetos Python casi arbitrarios. 
Esto se define como el acto de convertir objetos a una cadena de bytes (y viceversa, ``desestibar'').'''

import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f)

import pickle

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data1 = pickle.load(f)

#Para que sirve la función map, lambda y filter?

'''Operador lambda:  
El operador lambda o función lambda, es una forma de crear funciones anónimas, es decir, funciones sin nombre. 
Estas funciones son desechable, es decir, solo se necesitan donde se han creado. 
Las funciones lambda se utilizan principalmente en combinación con las funciones Map, Filter y Reduce.

La sintaxis general de una funcion lambda es bastante simple:
lambda argument_list : expresison'''

#Función lambda que devuelve la suma de sus dos argumentos:
f = lambda x, y : x + y
f(2,2)

#Resultado:
#4

#Segundo ejemplo de lambda
#Función lambda que devuelve la raíz cuadrada de su argumento
a = lambda x : x**1/2
a(233)

#Resultado:
#15,2643

'''Operador Map: 
El operador Map, toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento '''

#Ejemplo del operador Map y Lambda
nums = [11, 25, 34, 100, 23]
result = list(map(lambda x:x+5, nums))
print(result)

#Resultado:
#[16, 30, 39, 105, 28]

'''Operador Filter:

El operado filter (función, lista) ofrece una forma elegante de filtrar todos los elementos de una lista, 
para los que la función de función devuelve True.  
El operador filter(f, l) necesita una función f como primer argumento. f devuelve un valor booleano, es decir, 
verdadero o falso. Esta función se aplicará a cada elemento de la lista. 
Solo si f devuelve True, el elemento de la lista se incluirá en la lista de resultados.'''

#Usando el operador Filter
nums = [0, 2, 5, 8, 10, 23, 31, 35, 36, 47, 50, 77, 93]
result = filter(lambda x: x % 2 == 0, nums)
print(result)

#Resultado:
#[2, 8, 10, 36, 50]

#Como pueden observar, el operador filter no incluyo a los elementos que no fueran divisibles entre 2,
# otra cosa es que hacemos uso de lambda, ya que es utilizado especialmente para este tipo de situaciones.


#Qué es list comprehension, set comprehension y dict comprehension?

#list comprehension
# Create the lists
A = [a for a in range(20) if a % 2 == 0]
B = [b for b in range(20) if b % 3 == 0]
C = [c for c in range(20) if c in A and c in B]

# Print out the result
print('A: ', A)
print('B: ', B)
print('C: ', C)

# Create the lists
A = [a for a in range(5) if a % 2 == 0]
B = [b for b in range(5) if b % 3 == 0]
C = [a + b for a in A for b in B]

# Print out the result
print('A: ', A)
print('B: ', B)
print('C: ', C)

verbs = ["work", "eat", "sleep", "repeat"]
verbs_with_ing = [verb + "ing" for verb in verbs]
print(verbs_with_ing)

verbs = ["work", "eat", "sleep", "repeat"]
verb_converter = lambda verb: verb + "ing"
verbs_with_ing = [verb_converter(verb) for verb in verbs]
print(verbs_with_ing)

#set comprehension

# Construct a list of integers which are not prime (which are the product of two integers)
no_primes = {a * multiplier for multiplier in range(2, 100) for a in range(2, 100)}
# Since 1 is not a prime number we have to add it to this list
no_primes.add(1)
# Now construct a list of primes out of this list
primes = {p for p in range(1, 100) if p not in no_primes}
# Show the result
print(no_primes)
print(primes)

#dict comprehension
# Create a set comprehension for all x in 0...9 for the function f(x)=x^2
f = {x: x**2 for x in range(10)}

# Display the result
print(f)

pass