print("Qual valor da compra?: ")

compra = float(input())

if compra < 100:
    print(f"O valor da compra é de R$ {compra:.2f}")

elif compra >= 100 and compra < 300:
    desconto = compra * 0.10
    total = compra - desconto
    print(f"O valor da compra é de R$ {compra:.2f} e o valor com desconto é de R$ {total:.2f}")

elif compra >= 300:
    desconto = compra * 0.15
    total = compra - desconto
    print(f"O valor da compra é de R$ {compra:.2f} e o valor com desconto é de R$ {total:.2f}")
