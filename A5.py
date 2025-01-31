def contar_frecuencia_palabras(frase):
    palabras = frase.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

frase = input("Introduce una frase en minúsculas: ")
frecuencia_palabras = contar_frecuencia_palabras(frase)
print(frecuencia_palabras)