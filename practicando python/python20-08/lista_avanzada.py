#crear 2 listas para cargar datos, los que desee el usuario
#Crear las listas necesarias para resultados
#Operaciones: 
# Sumar 2 listas
# Restar 2 listas
# Multiplicar 2 listas
# Dividir 2 listas

#Validar los datos de entrada a cada lista
#Guardar los resultados en una nueva lista y mostrarlos

def sumar_lista():
    print(lista1 + lista2)

def restar_lista():
    print(lista1 - lista2)

def multiplicar_lista():
    print(lista1 * lista2)

def dividir_lista():
   print(lista1 / lista2)

def validar_info():
    print(lista1)
    print(lista2)

def validarInfoLista1():
    print(lista1)

def validarInfoLista2():
    print(lista2)

lista1 = ["Cristian", 3]
lista2 = ["Sebastian", 5]

while True:
    print("Bienvenido al programa de las listas donde guardaremos lo que usted coloque borrar o agregar. ")
    print("1. Agregar valor a la lista")
    print("2. Mostrar lista")
    print("3. Quitar un valor en la lista")
    print("4. Sumar listas")
    print("5. Restar listas")
    print("6. Multiplicar listas")
    print("7. Dividir listas")
    print("8. Salir del programa")

    opcion = int(input("Que opcion le gustaria escoger: "))

    if opcion == 1:
        print("En cual de las listas le gustaria agregar algo Lista 1 o Lista 2")

        elegir_lista = int(input("Seleccione:\n" \
                             "1) Para Lista 1\n" \
                             "2) Para Lista 2\n"
                             "Eleccion: "))

        if elegir_lista == 1:
            validarInfoLista1()
            cantidad_agregar = int(input("Cuantas cosas va agregar a la Lista1?\n" \
                                         "Cantidad: "))
            for i in range(cantidad_agregar):
                nombre = input(f"Ingrese el Nombre del alumno {i+1}: ")
                lista1.append(nombre)
                print(f"Asi va quedando su lista {lista1}")

        elif elegir_lista == 2:
            validarInfoLista2()
            cantidad_agregar = int(input("Cuantas cosas va agregar a la Lista2?\n" \
                                         "Cantidad: "))
            for i in range(cantidad_agregar):
                nombre = input(f"Ingrese el Nombre del alumno {i+1}: ")
                lista1.append(nombre)
                print(f"Asi va quedando su lista {lista2}")

    elif opcion == 2:
        validar_info()

    elif opcion == 3:
        validar_info()
        print("Quitar valor de la lista")
        elegir_lista = int(input("Seleccione la lista de la cual quiere eliminar:\n" \
                                     "1) Para Lista 1\n" \
                                     "2) Para Lista 2\n"
                                     "Eleccion: "))

        if elegir_lista == 1:
            print("Que cosa desea eliminar?")
            print(f"En este momento hay {len(lista1)} casillas ocupadas")

            eliminar = input("Ingrese el nombre el cual quiere eliminar: ")

            if eliminar in lista1:
                lista1.remove(eliminar)
                print(f"{eliminar} fue eliminado corresctamente")
            else:
                print(f"{eliminar} no se a encontrado en su lista")

        elif elegir_lista == 2:
            print("Que cosa desea eliminar?")
            print(f"En este momento hay {len(lista2)} casillas ocupadas")

            eliminar = input("Ingrese el nombre el cual quiere eliminar: ")

            if eliminar in lista2:
                lista2.remove(eliminar)
                print(f"{eliminar} fue eliminado corresctamente")
            else:
                print(f"{eliminar} no se a encontrado en su lista")

    elif opcion == 4:
        sumar_lista()
        validar_info()

    elif opcion == 5:
        restar_lista()
        validar_info()

    elif opcion == 8:
        print("Saliendo del programa...")
    else:
        break
        