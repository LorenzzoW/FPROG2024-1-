import random 

#Lista para armazenar valores sorteados...
valores_sorteados = []

#Sorteia 5 valores entre 0 e 100 e adiciona à lista 
for _ in range(5):
    valores_sorteados.append(random.randint(0, 100))

#Imprime os valores sorteados
print(f"Valores sorteados: {valores_sorteados}")

#Calcula e imprime o menor valor
menor_valor = min(valores_sorteados)
print(f"Menor valor sorteado: {menor_valor}")

#Calcula e imprime o maior valor
maior_valor = max(valores_sorteados)
print(f"Maior valor sorteado: {maior_valor}")

#Calcula e imprime a média dos valores
media = sum(valores_sorteados) / len(valores_sorteados)
print(f"Média dos valores sorteado: {media:.2f}")