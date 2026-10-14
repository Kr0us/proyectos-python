import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()

    print(
      "---------------------------------------------------"
    "\n|Bienvenido al juego de adivinar el numero        |" 
    "\n|Donde tendras que ingresar un numero por terminal|" 
    "\n|Y te dire si es mayor, menor o si es correcto    |"
    "\n --------------------------------------------------"
    "\n      Selecciona 1 para jugar, 0 para salir")

    eleccion = int(input(""))
    
    if eleccion == 1:
        hasta_numero = int(input("Hasta que numero quieres adivinar?: "))
        numero_azar = random.randint(1, hasta_numero)

        while True:
            numero = int(input(f"\nIngresa un numero del 1-{hasta_numero}: "))
            
            if numero == numero_azar:
                print(f"Le haz acertado al numero!!!\nEl numero era {numero_azar}")

                for i in range(5,0,-1):
                    print(f"El programa se reiniciara en {i} segundos")
                    time.sleep(1)
                break

            elif numero > numero_azar:
                print("El numero es mas bajo")
        
            elif numero < numero_azar:
                print("El numero es mas alto")
    else:
        for i in range(5,0,-1):
            print(f"El programa se apagara en {i} segundos")
            time.sleep(1)
        break
        
    










    


    