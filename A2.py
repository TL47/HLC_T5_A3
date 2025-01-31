def eliminar_duplicados(lista_palabras):
    return list(set(lista_palabras))

lista = ["hola", "mundo", "hola", "python", "mundo"]
lista_sin_duplicados = eliminar_duplicados(lista)
print(lista_sin_duplicados)