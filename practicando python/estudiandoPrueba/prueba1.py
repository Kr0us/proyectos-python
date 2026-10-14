def agregar_libro(biblioteca, titulo, autor, anio):
    """Agrega un libro a la biblioteca"""
    libro = {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "disponible": True
    }
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado correctamente.")


def buscar_libro_por_titulo(biblioteca, titulo):
    """Busca libros por título (puede haber varios con mismo título)"""
    resultados = []
    for libro in biblioteca:
        if titulo.lower() in libro["titulo"].lower():
            resultados.append(libro)
    return resultados


def prestar_libro(biblioteca, titulo):
    """Marca un libro como prestado si está disponible"""
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            if libro["disponible"]:
                libro["disponible"] = False
                print(f"Libro '{titulo}' prestado correctamente.")
                return True
            else:
                print(f"El libro '{titulo}' no está disponible.")
                return False

    print(f"No se encontró el libro '{titulo}'.")
    return False


def mostrar_libros_disponibles(biblioteca):
    """Muestra todos los libros disponibles"""
    disponibles = [libro for libro in biblioteca if libro["disponible"]]
    if not disponibles:
        print("No hay libros disponibles en este momento.")
        return

    print("\n=== LIBROS DISPONIBLES ===")
    for libro in disponibles:
        print(f"'{libro['titulo']}' - {libro['autor']} ({libro['anio']})")


# Programa principal
def main():
    biblioteca = []

    # Agregar algunos libros iniciales
    agregar_libro(biblioteca, "Cien años de soledad", "Gabriel García Márquez", 1967)
    agregar_libro(biblioteca, "Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    agregar_libro(biblioteca, "1984", "George Orwell", 1949)

    # Ejemplos de uso
    print("\nBuscando libros con 'soledad':")
    resultados = buscar_libro_por_titulo(biblioteca, "soledad")
    for libro in resultados:
        print(f"- {libro['titulo']}")

    print("\nIntentando prestar '1984':")
    prestar_libro(biblioteca, "1984")

    print("\nLibros disponibles después del préstamo:")
    mostrar_libros_disponibles(biblioteca)


if __name__ == "__main__":
    main()