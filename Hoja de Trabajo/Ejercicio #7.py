#Escribir un programa en Python que pida al usuario su peso (en libras) y
#estatura (en metros), calcule el índice de masa corporal y lo almacene en una
#variable, y muestre por consola la frase Tu índice de masa corporal es <imc>
#donde <imc> es el índice de masa corporal calculado redondeado con dos
#decimales.

import math

libras=(int(input("Introduzca su peso en libras: ")))
altura=(float(input("introduzca su altura en metros: ")))

constante=2.2046

kg=libras/constante

imc=kg/(altura*altura)
redondeado=round(imc, 2)

print("Tu indice de Masa Corporal es de: ", redondeado)