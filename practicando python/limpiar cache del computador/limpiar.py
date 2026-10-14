import os
import shutil
from pathlib import Path

def eliminar_contenido(carpeta: Path) -> tuple[int, int]:
	"""Elimina el contenido de una carpeta sin eliminar la carpeta raíz."""
	eliminados = 0
	errores = 0

	if not carpeta.exists():
		return eliminados, errores

	for elemento in carpeta.iterdir():
		try:
			if elemento.is_dir() and not elemento.is_symlink():
				shutil.rmtree(elemento)
			else:
				elemento.unlink()
			eliminados += 1
		except (PermissionError, OSError) as error:
			errores += 1
			print(f"No se pudo eliminar {elemento}: {error}")

	return eliminados, errores


def carpetas_cache() -> list[Path]:
	"""Devuelve carpetas temporales y cachés comunes de Windows."""
	local_app_data = os.environ.get("LOCALAPPDATA")
	rutas = [Path(os.environ.get("TEMP", ""))]

	if local_app_data:
		base = Path(local_app_data)
		rutas.extend(
			[
				base / "Temp",
				base / "Microsoft" / "Windows" / "INetCache",
				base / "Microsoft" / "Windows" / "WebCache",
			]
		)

	# Evita procesar rutas vacías o repetidas.
	return list(dict.fromkeys(ruta for ruta in rutas if str(ruta)))


def main() -> None:
	print("Este programa eliminará archivos temporales y cachés comunes de Windows.")
	print("Algunos archivos en uso o protegidos no podrán eliminarse.\n")

	if input("¿Deseas continuar? [s/N]: ").strip().lower() not in ("s", "si", "sí"):
		print("Operación cancelada.")
		return

	total_eliminados = 0
	total_errores = 0

	for carpeta in carpetas_cache():
		eliminados, errores = eliminar_contenido(carpeta)
		total_eliminados += eliminados
		total_errores += errores
		print(f"Procesada: {carpeta}")

	print(f"\nElementos eliminados: {total_eliminados}")
	print(f"Elementos no eliminados: {total_errores}")
	print("Limpieza finalizada.")


if __name__ == "__main__":
	main()
