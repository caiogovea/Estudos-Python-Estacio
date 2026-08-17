## Cálculo de salário

print("Digite o seu salário: ")
salario = float(input())
print("Digite o percentual de aumento: ")
aumento = float(input())

novoSalario = (salario * aumento) / 100 + salario

print(f"Seu novo salário é: {novoSalario}")