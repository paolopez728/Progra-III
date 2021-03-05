#Una ferretería tiene mucho éxito en dos de sus productos: barrenos y sierras
#eléctricas. Suele hacer venta por correo y la empresa de logística les cobra
#por peso de cada paquete así que deben calcular el peso de los barrenos y
#sierras que saldrán en cada paquete a demanda. Cada barreno pesa 112 kg y 
#cada sierra 75 kg. Escribir un programa que lea el número de barrenos y
#sierras vendidos en el último pedido y calcule el peso total del paquete que
#será enviado

opcion1=input("¿compró un barreno? (s/n): ")
if opcion1=="s":
    barreno=int(input("¿Cuantas a adquirido?: "))
else:
    barreno=0

opcion2=input("¿compro una sierra? (s/n): ")
if opcion2=="s":
    sierra=int(input("¿Cuantas a adquirido?: "))
else:
    sierra=0

PesoBarreno=barreno*112
PesoSierra=sierra*75
Total=PesoBarreno+PesoSierra

print("La cantidad de barrenos es de: ", barreno, "con un peso total de: ", PesoBarreno, "Kilogramos")
print("La cantidad de sierras es de: ", sierra, "con un peso total de: ", PesoSierra, "Kilogramos")
print("El total del paquete es de: ", Total)