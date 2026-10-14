'''Recorrer la lista y agregar a cada diccionario una nueva clave "promedio" 
con el promedio de sus notas (puedes calcularlo usando sum(...) / len(...)).
Al final, si hacemos print(estudiantes[0]), debería verse algo como:
{"nombre": "Sofía", "notas": [6.0, 7.0, 5.5], "promedio": 6.17}'''


estudiantes = [
    {"nombre": "Sofía", "notas": [6.0, 7.0, 5.5]},
    {"nombre": "Mateo", "notas": [4.0, 3.5, 5.0]},
    {"nombre": "Valentina", "notas": [6.5, 6.0, 7.0]}
]

def promedio(notas):
    return sum(notas) / len(notas)

for estudiante in estudiantes:
    estudiante["promedio"] = promedio(estudiante["notas"])
    print(estudiante)

print(estudiantes[0])