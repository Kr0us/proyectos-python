#utilizando ciclo y lista
#Crear una lista llamada 'alumnos'
#cargar 10 alumnos a la lista, utilizando ciclo
#mostrar los daros de la lista

def mostrarLista():
    print(alumnos)
    

alumnos = []

print("Bienvenido al programar para tener una lista de estudiantes")

while True:

    print("1. Agregar un alumno")
    print("2. Eliminar algun Alumno")
    print("3. Consulta de lista")
    print("4. Salir del programa")

    opcion = int(input("Cual es su eleccion?: "))

    if opcion == 1:

        cantidad = int(input("Cuantos estudiantes quiere ingresar?: "))

        for i in range(cantidad):
            nombre = input(f"Ingrese el Nombre del alumno {i+1}: ")
            alumnos.append(nombre)
            print(f"Asi va quedando su lista {alumnos}")

    elif opcion == 2:
        mostrarLista()
        print("Que alumno desea eliminar?")
        print(f"En este momento hay {len(alumnos)} alumnos")
        eliminar = input("Ingrese el nombre del estudiante el cual quiere eliminar: ")

        if eliminar in alumnos:
            alumnos.remove(eliminar)
            print(f"{eliminar} fue eliminado corresctamente")
        else:
            print(f"{eliminar} no se a encontrado en su lista")

    elif opcion == 3:
        print(f"Su lista de alumnos es: ")
        mostrarLista()

    elif opcion == 4:    
        print("ADIOS")
        break
                
    else:
        print("vuelvalo a intentar")
        continue