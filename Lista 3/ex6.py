import random

#Pergunta ao usuário se ele aposta em PAR ou ÍMPAR
aposta = input("Você aposta em PAR ou ÍMPAR? ").upper()

#Verifica se a aposta é válida
if aposta != "PAR" and aposta != "ÍMPAR":
    print("Opção inválida. Por favor, escolha entre PAR ou ÍMPAR.")
else:
    # Solicita ao usuário que digite um número de 0 a 5
    numero_usuario = int(input("Digite um número de 0 a 5: "))
    
    # Gera um número aleatório de 0 a 5
    numero_aleatorio = random.randint(0, 5)
    
    # Calcula a soma
    soma = numero_usuario + numero_aleatorio
    
    # Verifica se a soma é par ou ímpar
    resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"
    
    # Verifica se o usuário venceu
    if (aposta == "PAR" and resultado == "PAR") or (aposta == "ÍMPAR" and resultado == "ÍMPAR"):
        print(f"Você venceu! A soma dos números é {soma} ({resultado}).")
    else:
        print(f"Você perdeu! A soma dos números é {soma} ({resultado}). O programa venceu, hehe.")
