numeros = [10, 25, 3, 48, 17, 90, 2]

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")