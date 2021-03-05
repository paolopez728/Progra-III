#Escribir un programa en Python que pregunte al usuario por el número de
#horas estudiadas para el curso de programación III y el tiempo promedio 2
#usado por día. Después debe mostrar por pantalla la sumatoria de horas para
#que el docente evalúe en base a su conocimiento.

HorasEstudiadas=(int(input("Número de horas estudiadas para programacion III: ")))
HorasPromedio=(int(input("Numero de horas promedio por dia para programacion III: ")))

HorasTotal = HorasEstudiadas + HorasPromedio

print("Total de horas usadas por por el estudiantes para programacion III: ", HorasTotal)