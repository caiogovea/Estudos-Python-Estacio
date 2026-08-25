def calcular_media(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media

def situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

m = calcular_media(8.0, 6.5, 7.5)
status = situacao(m)

print(f"Média: {m:.1f}")
print(f"Situação: {status}")