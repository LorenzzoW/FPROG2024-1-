# Solicita as notas dos graus A e B ao usuário
nota_grau_a = float(input("Digite a nota do Grau A: "))
nota_grau_b = float(input("Digite a nota do Grau B: "))

# Calcula a média inicial
media_inicial = (nota_grau_a + nota_grau_b) / 2

# Define a porcentagem mínima de aprovação (60%)
porcentagem_aprovacao = 60

# Calcula a média mínima necessária para aprovação
media_minima_aprovacao = porcentagem_aprovacao / 100 * 10  # Considerando que são dois graus

# Verifica se o aluno passou ou ficou em recuperação
if media_inicial >= media_minima_aprovacao:
    print("Média final:", media_inicial)
    print("Aluno aprovado!")
else:
    print("Média final:", media_inicial)
    print("Aluno em recuperação (Grau C).")
    
    # Pergunta ao aluno se deseja substituir a nota do Grau A ou B
    substituir_grau = input("Deseja substituir a nota do Grau A ou B? (Digite 'a' ou 'b'): ")
    
    # Verifica a escolha do aluno e solicita a nova nota do Grau C
    if substituir_grau == 'a':
        nota_grau_a = float(input("Digite a nova nota do Grau A: "))
        nota_b = nota_grau_b  # Mantém a nota original do Grau B
    else:
        nota_a = nota_grau_a  # Mantém a nota original do Grau A
        nota_grau_b = float(input("Digite a nova nota do Grau B: "))
    
    # Recalcula a média final com a nota substituída
    media_final = (nota_a + nota_b) / 2
    
    # Verifica se o aluno passou ou reprovou após a substituição da nota
    if media_final >= media_minima_aprovacao:
        print("Média final após substituição:", media_final)
        print("Aluno aprovado!")
    else:
        print("Média final após substituição:", media_final)
        print("Aluno reprovado.")
