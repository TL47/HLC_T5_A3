def eliminar_pares():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in numeros:
        if i % 2 == 0:
            numeros.remove(i)
    return numeros
resultado = eliminar_pares()
print(resultado)