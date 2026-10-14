
def parImpar(num):

    if num % 2 == 0:
        print(f"tu numero es par")

    else:
        print(f"tu numero es impar")

while True:

    entrada = input("Ingresa tu numero o 'q' para salir: ")

    entrada = entrada.lower()

    if entrada == "q":
        break

    try:
        numero = int(entrada)

    except ValueError:
        print("Eso no es un numero. Intenta otra vez.")
        continue

    parImpar(numero)



    
    