suma = 0 

for i in range(1, 11):

    nota = float(input(f"Cual es su nota {i}: "))

    suma = suma + nota

promedio = suma/10

if promedio >= 4:
    print(f"Usted a aprobado con un promedio {promedio}")

else:
    print(f"Usted a reprobado con un promedio {promedio}")
