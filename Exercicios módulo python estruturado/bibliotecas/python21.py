import random

nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"
]

vencedor = random.choice(nomes)

print("SORTEIO DE NOMES")
print(f"Participantes: {nomes}")
print(f"\n O vencedor(a) sorteado(a) foi: {vencedor}!")