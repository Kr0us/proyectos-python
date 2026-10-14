#Diseñar un programa que permita ingresar la compra de 5 clientes
#Cada cliente debe comprar 4 productos
#Calcular la compra de 4 productos
#Si la compra supera los $10.000 tiene un descuento de 8% sino solo de 3%
#Mostrar descuento de cada compra
#Mostrar valor fianl a pagar

clientes = int(input("Cuantos clientes son?: "))

for cliente in range(1, clientes + 1):
    suma_compra = 0
    print(f"Ciente N°{cliente}")

    productos = int(input("Cuantos productos va a llevar?: "))

    for x in range(1,productos + 1):
        valor_compra = int(input(f"Ingresar valor de la compra {x}: "))
        suma_compra = suma_compra + valor_compra

    if suma_compra >= 10000:
        print("Obtienes un cupon del 8% de descuento")
        print(f"Tu compra queda en: ${suma_compra*0.92} antes de ${suma_compra}")

    else:
        print("Obtienes un cupon de compra del 3%")
        print(f"Tu compra queda en: ${suma_compra*0.97} antes de ${suma_compra}")


