# Crear un archivo llamado tarea_1.py
# Escribir un código en Python que imprima en pantalla lo siguiente:
# * 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14
#
# usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos.

import math

var1 = math.pi
var2 = '******'

print("%.1s" % var2,"%.7f" % var1,"%.2s" % var2,"%.6f" % var1,"%.3s" % var2,"%.5f" % var1,"%.4s" % var2,"%.4f" % var1,"%.5s" % var2,"%.3f" % var1,var2,"%.2f" % var1)
