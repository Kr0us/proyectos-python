producto = {
    "nombre": "Teclado",
    "precio": 25.0
}

#print(producto["descuento"])
print(producto.get("descuento", 0))

del producto["precio"]

print(producto.values())

