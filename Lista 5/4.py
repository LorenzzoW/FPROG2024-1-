import random

def sorteio(inicio, fim):
    
    num_sorteado = random.randint(inicio, fim)
    return num_sorteado


# Exemplo de uso
inicio_intervalo = int(input("Digite o valor inicial do intervalo: "))
fim_intervalo = int(input("Digite o valor final do intervalo: "))

num_sorteado = sorteio(inicio_intervalo, fim_intervalo)
print(f"O número sorteado é: {num_sorteado}")
