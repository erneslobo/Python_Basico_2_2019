# Crear un codigo que calcule las soluciones de la ecuacion cuadratica
# ax^2 + bx + c = 0

import math

a = float(input('Ingresar el valor de a\n'))
b = float(input('Ingresar el valor de b\n'))
c = float(input('Ingresar el valor de c\n'))


#x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
#x2 = (-b - math.sqrt(b**2-4*a*c))/2*a

#print('El valor de ax^2 + bx + c = 0 es')
#print('x1 =', x1)
#print('x2 =', x2)

discriminante = b ** 2 - 4*a*c

if discriminante < 0 :
    raiz = math.sqrt(-discriminante) * complex(0,1)
else:
    raiz = math.sqrt(-discriminante)

x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)

print('El valor de ax^2 + bx + c = 0 es')
print('x1 =', x1)
print('x2 =', x2)
