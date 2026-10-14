'''
    Objetivo:

-Calcular el promedio general de la lista tiempos.

-Crear una nueva lista llamada rapidos que guarde únicamente los tiempos que estuvieron por debajo del promedio.

-Mostrar en pantalla la nueva lista con los tiempos filtrados.'''

tiempos = [30, 85, 310, 45, 210, 95, 129]

rapidos =[]

def promedio(tiempos):
    return sum(tiempos)/len(tiempos)

print(f"Aqui tenemos los tiempos de los corredores: {tiempos}")
print(f"El promedio de los tiempos es: {promedio(tiempos)}")

promedio_general = promedio(tiempos)

for tiempo in tiempos:
    if tiempo < promedio_general:
        rapidos.append(tiempo)

print(f"Los tiempos mas rapidos con respecto {promedio_general} son los: {rapidos}")
