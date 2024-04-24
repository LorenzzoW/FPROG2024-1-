# Solicita o número de alunos
num_alunos = int(input("Quantos alunos deseja calcular a média? "))

# Variável para armazenar a média geral
media_geral = 0

for aluno in range(1, num_alunos + 1):
    print(f"\nAluno {aluno}:")
    
    # Lê as notas do grau A e grau B
    grauA = float(input("Digite a nota do grau A: "))
    grauB = float(input("Digite a nota do grau B: "))
    
    # Calcula a média
    media = (grauA + grauB) / 2
    
    if media >= 7.0:
        print("APROVADO")
    else:
        # Lê a nota do grau C
        grauC = float(input("Digite a nota do grau C: "))
        
        # Solicita qual nota (A ou B) deve ser substituída
        substituir = input("Substituir a nota do grau A ou B? ").upper()
        
        if substituir == 'A':
            grauA = grauC
        elif substituir == 'B':
            grauB = grauC
        
        # Recalcula a média
        media = (grauA + grauB) / 2
        
        if media >= 7.0:
            print("APROVADO")
        else:
            print("REPROVADO")
    
    # Atualiza a média geral
    media_geral += media

# Calcula e imprime a média geral dos alunos
media_geral /= num_alunos
print(f"\nMédia geral dos alunos: {media_geral:.2f}")
