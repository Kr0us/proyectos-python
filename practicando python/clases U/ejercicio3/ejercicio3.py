#Desarrollar un ejercicio en python, utilizando un menu y utilizar funciones
#opcion1 Sumar N numeros y mostrar resultado
#opcion2 Restar 2 numeros y mostrar resultado
#opcion3 Multipicar N numeros y Mostrar resultado
#opcion4 dividir 2 numeros y mostrar resultados
#opcion5 calcular el promedio de n notas


def sumar():
    n = int(input("Ingrese la cantidad de numeros a sumar:"))
    suma = 0
    for i in range(1, n + 1):
        numero = float(input(f"ingrese el {i} numero: "))
        suma += numero

    print(f"Su resultado es {suma}")

def restar():
    n1 = int(input("Ingrese el primer numero que quiere restar:"))
    n2 = int(input("Ingrese el segundo numero que quiere restar:"))

    resta = n1 - n2

    print(f"El resultado de la resta es {resta}")
    

def multiplicar():
    n = int(input("Ingrese la cantidad de numeros a multiplicar:"))
    mult = 1
    for i in range(1, n + 1):
        numero = float(input(f"ingrese el {i} numero: "))
        mult = mult * numero

    print(f"el resultado de la opercion es: {mult}")

def dividir():
    n1 = int(input("Ingrese el primer numero a dividir"))
    n2 = int(input(" Ingrese el segundo numero a dividir"))

    if n2 == 0:
        print("No se puede dividir por 0")

    else:
        div = n1/n2
        print(f"El resultado de {n1}/{n2} = {div}")

    

def promedio():
    cantidad_numeros = int(input("Cuantos numeros queremos sacar de promedio?: "))
    total = 0
    for x in range(1, cantidad_numeros + 1):
        numero = float(input(f"Ingrese su numero {x}: "))
        total = total + numero

    prom = total/cantidad_numeros

    print(f"El promedio es de {prom}")


while True:
    print("Menu principal")
    print("1. Sumar: ")
    print("2. Restar: ")
    print("3. Multiplicar: ")
    print("4. Dividir: ")
    print("5. Promedio ")
    print("0. Salir")

    eleccion = int(input("Ingrese su opcion: "))

    if eleccion == 1:
        sumar()

    elif eleccion == 2:
        restar()

    elif eleccion == 3:
        multiplicar()
    elif eleccion == 4:
        dividir()

    elif eleccion == 5:
        promedio()

    elif eleccion == 0:
        print("Ha finalizado el programa")
        break

    else:
        print("Opcion no valida vuelva intentar")
        continue
        