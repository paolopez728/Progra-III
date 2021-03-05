#Escribir un programa en Python que pregunte al usuario un monto a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión.

inversion=float(input("Ingrese el monto a invertir: "))
año=float(input("Ingrese los años a invertir: "))

if inversion<10000:
    porcentaje=1
    calculo=((inversion*porcentaje)/100)
    ganancia=calculo*año

    print("el interes por año es de: ", calculo)
    print("La inversion de Q", inversion, "sus ganancias serian Q", ganancia, "durante", año, "años" )

if inversion>10000:
    porcentajeB=2.5
    calculoB=((inversion*porcentajeB)/100)
    gananciaB=calculoB*año

    print("el interes por año es de: ", calculoB)
    print("La inversion de Q", inversion, "sus ganancias serian Q", gananciaB, "durante", año, "años" )