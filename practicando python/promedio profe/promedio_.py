print ("hola Mundo")
suma=0
for i in range(1,11):
    nota=float(input(f"ingrese nota {i}: "))
    suma=suma+nota
promedio=suma/10
print (f"El promedio final del alumno es:  {promedio:.1f}")
if promedio >=4:
    print("estado: Alumno Aprobado")
else:
    print("estado: Alumno Reprobado")