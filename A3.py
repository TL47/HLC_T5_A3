def crear_diccionario_cuadrados():
    diccionario = {i: i**2 for i in range(1, 6)}
    return diccionario

resultado = crear_diccionario_cuadrados()
print(resultado)