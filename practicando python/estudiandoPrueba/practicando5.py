'''Objetivo: Queremos mostrar el nombre de cada estudiante 
y su nota más alta (puedes apoyarte en la función max(...) de Python).'''

estudiantes = [
    {"nombre": "Sofía", "notas": [6.0, 7.0, 5.5]},
    {"nombre": "Mateo", "notas": [4.0, 3.5, 5.0]},
    {"nombre": "Valentina", "notas": [6.5, 6.0, 7.0]}
]

for estudiante in estudiantes:
    print(f"El nombre del estudiantes es: {estudiante['nombre']} y su nota mas alta es un {max(estudiante['notas'])}")