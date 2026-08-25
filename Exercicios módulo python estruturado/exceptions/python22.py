try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")

except ValueError:
    print("Erro: Você deve digitar apenas números.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero.")