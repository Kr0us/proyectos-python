#creamos una tupla

encabezado = ("Nombre", "Edad", "Carrera")

estudiantes = (
    ("Ana", 21, "Ciberseguridad"),
    ("Pedro", 22, "Teatro"),
    ("Silvia", 25, "Salud"),
    ("Juan", 20, "Informatica")
)

#print(encabezado)

#print (estudiantes[1][2]) 
print("\nNombres:")
for nombre in estudiantes:
    print(nombre[0])

print("\nEdad:")
for edad in estudiantes:
    print(edad[1])

print("\nCarrera:")
for carrera in estudiantes:
    print(carrera[2])