#Una peuqeña tienda necesita resgistrar informacion de sus productos. Para ello
# se utilizara estuctura basada en tuplas
#cada producto debe contener: COdigo, Nombre, Precio y Stock
#El programa debe utilizar tupla para almacenar los ancabezados y otra tupla para
#almacenar el registro de los productos
#1. Crea encabezado
#2. Crea Tupla prouctos
#3. Mostrar los encabezados
#4. Recorrer los productos
#5. Modificar el programa para mostrar los productos que tengan un stock menor o igual a 10
#6. para cada producto calcular el valor_inventario=precio[2]*stock[3]
#7. Mostrar todos los valores de inventario
#8. Calcular y mostrar el valor total del inventario

encabezado = ("Codigo", "Nombre", "Precio", "Stock")

productos = (
    (111, "Computadora", 3000, 3),
    (222, "Tablet", 1000, 5),
    (333, "Celular", 2000, 8),
    (444, "SSD", 80, 11)
)

while True:
    
    print("\nEliga su opcion: ")
    print("1. Mostrar las categorias.")
    print("2. Recorrer los productos")
    print("3. Mostrar productos que tengan stock menor o igual a 10.")
    print("4. Mostrar valor total del inventario de los prodcutos")
    print("5. Mostar los valor del inventario")
    print("0. SALIR")

    opcion = int(input("\nELija su opcion:"))

    if opcion == 1:
        print(f"{encabezado}")

    elif opcion == 2:
        print(f"{encabezado[0]:<8} {encabezado[1]:<12} {encabezado[2]:<10} {encabezado[3]:<6}")
        print("-" * 45)
        for producto in productos:
            print(f"{producto[0]:<8} {producto[1]:<12} ${producto[2]:<10} {producto[3]:<6}")

    elif opcion == 3:
        print(f"{encabezado[0]:<8} {encabezado[1]:<12} {encabezado[2]:<10} {encabezado[3]:<6}")
        print("-" * 45)
        for producto in productos:
            if producto[3] <= 10:
                print(f"{producto[0]:<8} {producto[1]:<12} ${producto[2]:<10} {producto[3]:<6}")

    elif opcion == 4:
        total_producto = 0
        print(f"{encabezado[1]:<12} {encabezado[2]:<10} {encabezado[3]:<6}")
        print("-" * 45)
        for producto in productos:
            valor_producto = producto[2] * producto[3]
            total_producto = total_producto + valor_producto
            print(f"{producto[1]:<12} {producto[2]:<10} {producto[3]:<6}")
        print(f"El valor de los productos es: {total_producto}")

    elif opcion == 5:
        valor_total = 0
        for producto in productos:
            valor = producto[2] * producto[3]
            valor_total = valor_total + valor
        print(f"El valor total del inventario completo es: {valor_total}")

    elif opcion == 0:
        break

    else:
        print("Valor no valido vuelvalo hacer.")
