number = int(input("Escoge el numero del cual quisieras saber la tabla de multiplicar: "))

numeroMultiplicador = int(input("Por cuantos te gustaria saber la tabla de este numero?: "))

def multiplicador():
    for x in range(0,numeroMultiplicador+1):

        print(f"{number} x {x} = {number * x} ")



multiplicador()

    

