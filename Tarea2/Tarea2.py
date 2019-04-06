#Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.

mis_valores = [5, 6, 10, 13, 3, 4]
Promedio = sum(mis_valores)/len(mis_valores)
print ('El Promedio de la lista es',Promedio)

#Considere si se tiene una lista que contiene las alturas de grupos de personas


todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

#Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas

index = todos.index(max(todos))
grupo = max(todos)
print('El grupo q contiene la mayor de todas la alturas es group #',(index+1), 'la altura mayor es', max(grupo))