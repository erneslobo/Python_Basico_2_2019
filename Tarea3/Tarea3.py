
import operator

# Para definir la agenda del hospital
agenda_hospital = []

persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')

# agregamos una persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)

# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)

# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)

# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]

# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)

print(agenda_hospital)

# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)

# Pregunta 1 Cuantos pacientes llegaron en total?

print('Llegaron', len(agenda_hospital),'pacientes')

# Pregunta 2 Cuantas personas llegaron por dolor?

cuenta = 0

for x in agenda_hospital:
    if x[5]=='dolor':
        cuenta +=1

print(cuenta, 'pacientes llegaron por dolor')

#Pregunta 3 Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven

agenda_hospital.sort(key= operator.itemgetter(3), reverse=True)
print(agenda_hospital)

#Pregunta 4 Cuantos pacientes son mayores de edad? cuantos menores?

mayores = 0
menores = 0

for x in agenda_hospital:
    if x[3] >= 18:
        mayores += 1
    else:
        menores += 1

print(mayores,'personas mayores en la lista')
print(menores,'personas menores en la lista')

#Preguna 5 Suponga que se atienden con orden de prioridad por gravedad de consulta,
#empezando por los que tienen dolor y luego por edad (mas viejo al joven),
# empezando por el adulto mayor. Ordene la lista empenzando por los que tienen mayor prioridad.

agenda_hospital.sort(key=operator.itemgetter(5,3), reverse=True)

print(agenda_hospital)

#Pregunta 6 Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.

for x in reversed(agenda_hospital):
    if x[5] == 'dolor':
        agenda_hospital.remove(x)
print(agenda_hospital)

agenda_hospital.sort(key=operator.itemgetter(3))
print(agenda_hospital)

