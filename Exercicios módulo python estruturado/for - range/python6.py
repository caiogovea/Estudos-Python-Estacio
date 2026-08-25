soma = 0

primeiro_str = input("Digite o número 1 de 10: ")
primeiro = float(primeiro_str)

maior = primeiro
menor = primeiro
soma += primeiro

for i in range(2, 11):
  numero_str = input(f"Digite o número {i} de 10: ")
  numero = float(numero_str)

  soma += numero

  if numero > maior:
    maior = numero

  if numero < menor:
    menor = numero

media = soma / 10

print("\n--- Resultados ---")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma total: {soma}")
print(f"Média: {media}")