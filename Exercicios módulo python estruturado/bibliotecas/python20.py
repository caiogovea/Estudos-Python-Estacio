import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("JOGO DA ADIVINHAÇÃO")
print("Tente adivinhar o número entre 1 e 100!\n")

while True:
    palpite_str = input("Digite seu palpite: ")
    
    if not palpite_str.isdigit():
        print("[X] Por favor, digite apenas números inteiros válidos.")
        continue
        
    palpite = int(palpite_str)
    tentativas += 1
    
    if palpite > numero_secreto:
        print("Muito alto! Tente um número menor.\n")
    elif palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.\n")
    else:
        print(f"\n🎉 Acertou! O número era {numero_secreto}.")
        print(f"Você precisou de {tentativas} tentativas.")
        break