'''Objetivo: Queremos obtener una nueva lista llamada seleccionados que 
contenga solo los nombres de quienes estudian "Informática". 
Al final, debería quedar así: ["Sofía", "Valentina"].'''

alumnos = [
    {"nombre": "Sofía", "carrera": "Informática"},
    {"nombre": "Mateo", "carrera": "Diseño"},
    {"nombre": "Valentina", "carrera": "Informática"}
]

seleccionados = []

for alumno in alumnos:
    if alumno["carrera"] == "Informática":
        seleccionados.append(alumno["nombre"])
        print(f"Se a agregado a la lista de seleccionados: {alumno["nombre"]}")

for alumnoSeleccionado in seleccionados:
    print(f"Esta en la lista de seleccionado: {alumnoSeleccionado}")