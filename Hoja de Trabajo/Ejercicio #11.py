#Una empresa de tecnologías vende memorias RAM a US$20.00 cada una. La
#memoria usada tiene un descuento del 60%. Escribir un programa que
#comience leyendo el número de Memorias RAM vendidas que no son nuevas.
#Después el programa debe mostrar el precio habitual de una memoria RAM
#nueva, el descuento que se le hace por no ser nueva y el coste final total.

Ram=int(input("Memorias Ram adquiridas: "))
calculo=((60*20)/100)
descuento=Ram*calculo
compra=Ram*20

print("Precio de la Ram nueva es de US$",20,"por unidad" )
print("Precio de la Ram usada es de US$", calculo, "por unidad")
print("Memorias Ram usadas y compradas", Ram, "unidades con un precio de US$",descuento)