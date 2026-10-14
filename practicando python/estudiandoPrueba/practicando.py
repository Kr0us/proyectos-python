productos = [
    {"nombre": "Cuaderno", "precio": 1500, "stock": 4},
    {"nombre": "Lápiz", "precio": 300, "stock": 0},
    {"nombre": "Goma", "precio": 200, "stock": 7}
]

#Objetivo: Mostrar en pantalla únicamente los nombres de los productos que tienen unidades disponibles (es decir, donde stock > 0).

for producto in productos:
    if producto["stock"] > 0:
        print(f"El producto: {producto["nombre"]}\n"
               "Esta disponible\n")