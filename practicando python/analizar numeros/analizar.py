import random

numeros = [random.randint(1,10) for _ in range(6)]


print(f"la lista es: {numeros}")

print(f"el numero mas alto es: {max(numeros)}")
print(f"el numero mas bajo es: {min(numeros)}")
print(f"La suma de los 6 numeros es: {sum(numeros)}")


