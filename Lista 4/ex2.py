import random

#Sorteia um número aleatório entre 1 e 10
numero_sorteado = random.randint(1, 10)
tentativas = 3

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número sorteado entre 1 e 10.")

while tentativas > 0:
    # Lê a tentativa do usuário
    tentativa = int(input(f"Você tem {tentativas} tentativas. Digite um número: "))
    
    # Verifica se a tentativa está correta
    if tentativa == numero_sorteado:
        print("Parabéns! Você acertou!")
        break
    elif tentativa < numero_sorteado:
        print("O número a adivinhar é maior.")
    else:
        print("O número a adivinhar é menor.")

    #Decrementa o número de tentativas
    tentativas -= 1

    #Se o usuário usou todas as tentativas e não acertou
if tentativas == 0:
    print(f"Você perdeu! O número sorteado era {numero_sorteado}.")