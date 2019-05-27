import json

def escribirArchivo(diccionario):
    with open('clinica.txt', 'w') as f:
        json.dump(diccionario, f)

def leerArchivo():
    with open('clinica.txt', 'r') as f:
        return json.load(f)

leerArchivo()

pass