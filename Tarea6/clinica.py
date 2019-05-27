# lambda funcion para aplanar la lista de listas
flatten = lambda l: [item for sublist in l for item in sublist]

def returnNotMatches(a, b):
    a = set(a)
    b = set(b)
    return [list(b - a), list(a - b)]

def intersection(a, b):
    a = set(a)
    b = set(b)
    return list(b & a)

class Clinica(dict):
    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_paciente(self,identificación,
                        Nombre, Apellido,
                        teléfono, dirección,
                        lista_de_enfermedades_tratadas,
                        lista_de_medicamentos_que_toma):
        self.update({
            identificación :{
            'Nombre':Nombre,
            'Apellido':Apellido,
            'teléfono':teléfono,
            'dirección':dirección,
            'lista_de_enfermedades_tratadas':lista_de_enfermedades_tratadas,
            'lista_de_medicamentos_que_toma':lista_de_medicamentos_que_toma}
        })

        print('Paciente agregado',repr(self[identificación]))

    def borrar_paciente(self, identificacion):
        print('Borrando Paciente', repr(self[identificacion]))
        if identificacion in self:
            del self[identificacion]

    def agregar_medicinas(self,identificacion, nuevo_medicamento):
        self[identificacion]['lista_de_medicamentos_que_toma'].append(nuevo_medicamento)

    def agregar_enfermedades(self,identificacion, nueva_enfermedad):
        self[identificacion]['lista_de_enfermedades_tratadas'].append(nueva_enfermedad)

    def enfermedades_tratadas(self):
        return flatten([self[paciente_id]['lista_de_enfermedades_tratadas'] for paciente_id in self.keys()])

    def medicamentos_recetados(self):
        return flatten([self[paciente_id]['lista_de_medicamentos_que_toma'] for paciente_id in self.keys()])

    def comparar_pacientes(self, paciente1_id, paciente2_id):
        #Creando funcion reporte. notese que el formato es similar
        def reporte(Mensaje, funcion_a_ejecutar, detalle):
            print(Mensaje,
                  'Paciente:' ,paciente1_id,
                  'Paciente:', paciente2_id,
                  funcion_a_ejecutar(
                      self[paciente1_id][detalle],
                      self[paciente2_id][detalle])
                  )
        reporte('Medicamentos en común', intersection, 'lista_de_medicamentos_que_toma')
        reporte('Medicamentos diferentes', returnNotMatches, 'lista_de_medicamentos_que_toma')
        reporte('Enfermedades en común', intersection, 'lista_de_enfermedades_tratadas')
        reporte('Enfermedades diferentes', returnNotMatches, 'lista_de_enfermedades_tratadas')

