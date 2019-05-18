# Misc classes
class misc:
    def __repr__(self):
        # return the clase name
        return self.__class__.__name__

    def __str__(self):
        # return the clase name
        return self.__class__.__name__

class Animal(misc):
    def __init__(self, especie):
        self.especie = especie

    def reproducirse(self):
        print(f'El {self} está reproduciendose')

    def comer(self):
        print(f'El {self} está comiendo')

    def crecer(self):
        print(f'El {self} está creciendo')

    def nacer(self):
        print(f'El {self} está naciendo')

    def morir(self):
        print(f'El {self} está muriendo')


class Mono(Animal):
    def __init__(self):
        super().__init__(especie='Mono')
        self.cola = True

    def jugar(self):
        print(f'El {self.especie} está jugando')

    def mueve_la_cola(self):
        print(f'El {self.especie} mueve la cola')

class Humano(Mono):
    def __init__(self):
        self.especie = 'Humano'
        self.cola = False

    def mueve_la_cola(self):
        if not self.cola:
            print(f'El {self.especie} no tiene cola')
        else:
            print(f'El {self.especie} tiene cola')

class Abuelo(Humano):
    def __init__(self):
        self.esTrabajador = True

class Padre(Abuelo):
    def __init__(self):
        self.estudios = 'Contador'

class Hijo(Padre):
    def __init__(self):
        self.profesion = 'Analista de negocios'