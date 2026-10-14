def contadorVocales(texto):

    contador = 0
    vocales = "aeiouAEIOU"

    for letra in texto:

        if letra in vocales:
            contador = contador + 1

    return contador
    
