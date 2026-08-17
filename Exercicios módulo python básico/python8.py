## Simulador de caixa de supermercado

arroz = 10.00
feijao = 8.50
macarrao = 5.25

print("Quantos pacotes de arroz você deseja?: ")
qtArroz = int(input())

print("Quantos pacotes de feijão você deseja?: ")
qtFeijao = int(input())

print("Quantos pacotes de macarrão você deseja?: ")
qtMacarrao = int(input())

valor = (qtArroz * arroz) + (qtFeijao + feijao) + (qtMacarrao + macarrao)
print(f"Total da compra: {valor}")