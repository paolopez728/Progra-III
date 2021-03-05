#Escribir un programa en Python que pida al usuario dos números flotantes y
#muestre por pantalla la <a> entre <b> da un cociente <c> y un resto <d>
#donde <a> y <b> son los números introducidos por el usuario, y <c> y <d>
#son el cociente y el resto de la división entera respectivamente.

import math

numero1=float(input("Ingrese el Primer numero flotante: "))
numero2=float(input("Ingrese el segundo numero flotante: "))

resto=numero1%numero2
cociente=numero1/numero2

RedondeoResto=round(resto,2)
RedondeoCociente=round(cociente,2)

print("El resto de la division es: ", RedondeoResto)
print("El cociente de la division es de: ", RedondeoCociente)