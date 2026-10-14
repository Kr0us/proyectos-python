# Proyectos Python

Ejercicios y pequeños proyectos de aprendizaje de Python de Kr0us.
Este repositorio guarda el progreso; algunos ejercicios están en desarrollo.

## Organización

- `practicando python/`: proyectos y ejercicios anteriores, incluidos los de `8deoctubre/`.
- `tuplas/`: ejercicios de tuplas.
- `diccionarios/`: ejercicios de diccionarios.
- `listas/`: ejercicios de listas.
- `hello.py` y `proyecto.py`: ejercicios iniciales.

## Ejecutar un ejercicio

Desde la carpeta del repositorio, con Python 3.12 o posterior:

```bash
python3 "practicando python/8deoctubre/tupla.py"
```

Revisa cada programa antes de ejecutarlo. El proyecto `limpiar cache del computador`
elimina archivos y está pensado para Windows: no lo ejecutes en WSL/Linux.

## Guardar y subir avances desde WSL

```bash
cd /home/kr0us/proyectos_python
git status
git add .
git diff --cached
git commit -m "Describe aquí los cambios realizados"
git push
```

Antes de confirmar los cambios, revisa que no incluyan contraseñas ni datos personales.
Los archivos temporales, entornos virtuales y el horario académico no se publican.
