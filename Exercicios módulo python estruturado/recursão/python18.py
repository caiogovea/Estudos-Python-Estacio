def maior_recursivo(lista):
    if len(lista) == 1:
        return lista[0]
    
    maior_do_resto = maior_recursivo(lista[1:])
    
    if lista[0] > maior_do_resto:
        return lista[0]
    else:
        return maior_do_resto
numeros = [15, 7, 42, 9, 3]

print("Maior número da lista:", maior_recursivo(numeros))  
