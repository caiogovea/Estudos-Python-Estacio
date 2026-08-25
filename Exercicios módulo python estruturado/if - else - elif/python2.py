print("Qual sua idade?: ")
idade = int(input())

if idade > 0 and idade < 12:
    print("Criança")

elif idade > 12 and idade < 18:
    print("Adolescente")

elif idade > 18 and idade < 60:
    print("Adulto")

else:
    print("Idoso")