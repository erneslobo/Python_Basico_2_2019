from clinica import *
from clinicaArchivos import *

la_clinica = Clinica('MiClinica')
la_clinica.update(leerArchivo())

while True:
    print ('Bienvenidos a la Clinica\n\n')
    print ('Selecciona una de las siguiente opciones:\n\n')
    print ('1-Ingreso de un paciente nuevo')
    print ('2-Borrado de un paciente')
    print ('3-Agregar más enfermedades en un paciente en particular')
    print ('4-Agregar más medicamentos en un paciente en particular')
    print ('5-Generar reporte de las enfermedades tratadas en la clínica')
    print ('6-Generar reporte de los medicamentos entregados en la clínica')
    print ('7-Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.')
    print ('8-Salir del sistema\n')
    opcionMenu = int(input('Ingrese el numero de la opcion: '))

    if opcionMenu == 1:
        identificacion = input('Ingrese el numero de identificación:')
        nombre = input('Ingrese el nombre:')
        apellido = input('Ingrese el apellido:')
        telefono = int(input('Ingrese el telefono:'))
        direccion = input('Ingrese el dirección:')
        Enfermedad = input('Ingrese enfermedad:')
        listaEnfermedades=[]
        listaEnfermedades.append(Enfermedad)
        while True:
            opcionMenu1 = int(input('Si desea agregar otra enfermedad presione 1, de lo contrario presione 0: '))
            if opcionMenu1 == 1:
                Enfermedad = input('Ingrese enfermedad:')
                listaEnfermedades.append(Enfermedad)
            else:
                break
        Medicamento = input('Ingrese medicamento:')
        listaMedicamentos = []
        listaMedicamentos.append(Medicamento)
        while True:
            opcionMenu2 = int(input('Si desea agregar otro medicamento presione 1, de lo contrario presione 0: '))
            if opcionMenu2 == 1:
                Medicamento = input('Ingrese medicamento:')
                listaMedicamentos.append(Medicamento)
            else:
                break
        paciente = {'identificación':identificacion,'Nombre':nombre,'Apellido':apellido,'teléfono':telefono,
                    'dirección':direccion,'lista_de_enfermedades_tratadas' : listaEnfermedades,
                    'lista_de_medicamentos_que_toma': listaMedicamentos}
        la_clinica.agregar_paciente(**paciente)
        escribirArchivo(la_clinica)
    elif opcionMenu == 2:
        identificacion = input('Ingrese el numero de identificación:')
        la_clinica.borrar_paciente(identificacion)
        escribirArchivo(la_clinica)
    elif opcionMenu == 3:
        identificacion = input('Ingrese el numero de identificación:')
        enfermedad = input('Ingrese la enfermedad:')
        la_clinica.agregar_enfermedades(identificacion=identificacion, nueva_enfermedad=enfermedad)
        escribirArchivo(la_clinica)
    elif opcionMenu == 4:
        identificacion = input('Ingrese el numero de identificación:')
        medicamento = input('Ingrese medicamento:')
        la_clinica.agregar_medicinas(identificacion=identificacion, nuevo_medicamento=medicamento)
        escribirArchivo(la_clinica)
    elif opcionMenu == 5:
        reporte_enfermedades_tratadas = la_clinica.enfermedades_tratadas()
        print(reporte_enfermedades_tratadas)
    elif opcionMenu == 6:
        reporte_medicamentos_recetados = la_clinica.medicamentos_recetados()
        print(reporte_medicamentos_recetados)
    elif opcionMenu == 7:
        identificacion1 = input('Ingrese el numero de identificación paciente 1:')
        identificacion2 = input('Ingrese el numero de identificación paciente 2:')
        la_clinica.comparar_pacientes(identificacion1, identificacion2)
    else:
        break
pass