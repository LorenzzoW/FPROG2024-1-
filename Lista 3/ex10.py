import random

#Número de faces do dado
faces_dado = int(input("Digite o número de faces do dado (4, 6, 8, 10, 12 ou 16): "))

#verificando se o número de faces é valído
if faces_dado not in  [4, 6, 8, 10, 12, 16]:
     print("Número de faces inválido. Por favor, escolha entre 4, 6, 8, 10, 12 ou 16.")

else:
     #Realiza o sorteio do dado
     resultado = random.randint(1, faces_dado)

     # Imprime o resultado do sorteio
     print(f"O dado de {faces_dado} faces foi sorteado e o resultado é: {resultado}") 