def contar_vocales_consonantes(texto):
    vocales = 'aeiouAEIOU'
    contar = {'vocales': 0, 'consonantes': 0}
    
    for char in texto:
        if char.isalpha():
            if char in vocales:
                contar['vocales'] += 1
            else:
                contar['consonantes'] += 1
                
    return contar

texto = "Hola Mundo"
resultado = contar_vocales_consonantes(texto)
print(resultado)