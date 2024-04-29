########################## MINI JOGO DA VIDA ##########################

import random

def criar_jogador():
    return {
        'posicao': 0,    #Começa na posição 0!
        'filhos': 0,     #Inicia sem filhos!
        'casado': False, #Inicia solteiro!
        'loteria': False,#Inicia sem ganhar na loteria!
        'famoso': False, #Inicia não famoso!
        'vivo': True     #Começa vivo!
    }

def jogar_dado(jogador):
    resultado = random.randint(1, 6)  #Simula o lançamento do dado
    print(f"Dado lançado! Resultado: {resultado}")
    return resultado

def desafio_matematico(jogador):
    print("Desafio Matemático!")
    resultado = jogar_dado(jogador)  #Simula a rolagem do dado
    if resultado == 1:
        print("1. Mostrar na tela os números primos até 100")
        print("Resolução:")
        #Função para mostrar os números primos até 100
        for num in range(2, 101):
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                print(num, end=" ")
        print("\n")
    elif resultado == 2:
        print("2. Fazer o somatório dos números de 1 até 10")
        print("Resolução:")
        print(sum(range(1, 11)))
    elif resultado == 3:
        print("3. Imprimir a série de Fibonacci até o décimo elemento")
        print("Resolução:")
        a, b = 0, 1
        for _ in range(10):
            print(a, end=" ")
            a, b = b, a + b
        print("\n")
    elif resultado == 4:
        print("4. Calcular a área de um círculo com raio 2.5")
        print("Resolução:")
        raio = 2.5
        area = 3.14 * raio ** 2
        print(area)
    elif resultado == 5:
        print("5. Imprimir o fatorial de 5")
        print("Resolução:")
        fatorial = 1
        for i in range(1, 6):
            fatorial *= i
        print(fatorial)
    elif resultado == 6:
        print("6. Imprimir os 5 primeiros números divisíveis por 2 e por 5")
        print("Resolução:")
        num = 10
        count = 0
        while count < 5:
            if num % 2 == 0 and num % 5 == 0:
                print(num, end=" ")
                count += 1
            num += 1
        print("\n")

def formatura(jogador):
    print("Formatura!")
    cursos = {
        1: "Direito",
        2: "Medicina",
        3: "Jogos Digitais",
        4: "Segurança da Informação", 
        5: "Análise e Desenvolvimento de Sistemas",
        #(Adicionar mais cursos conforme necessário!)
    }
    resultado = jogar_dado(jogador)  #Simula a rolagem do dado
    curso_sorteado = cursos.get(resultado, "Curso não especificado...")
    print(f"Parabéns! Você se formou em {curso_sorteado}!")

def ter_filho(jogador):
    print("Teve um filho!")
    resultado = jogar_dado(jogador)  #Simula a rolagem do dado
    if resultado != 5:
        jogador['filhos'] += 1
        print("Parabéns! Você teve um filho.")
    else:
        print("Parabéns! Você teve gêmeos.")

def casamento(jogador):
    print("Casamento!")
    jogador['casado'] = True
    print("Parabéns! Você se casou!")

def ganhar_na_loteria(jogador):       
    print("Ganhou na loteria!")
    resultado = jogar_dado(jogador)  #Simula a rolagem do dado
    premios = {
        1: "Ganha R$ 2,50 no bolão",  
        2: "Ganha R$ 5.000,00",
        3: "Ganha R$ 50.000,00",
        4: "Ganha R$ 500.00,00",     
        5: "Ganha R$ 5.000.000,00",
        6: "Ganha R$ 100.000.00,00"
    }
    premio_sorteado = premios.get(resultado, "Prêmio não especificado")
    print(f"Parabéns! {premio_sorteado}")

def ficar_famoso(jogador):
    print("Ficou famoso!")
    jogador['famoso'] = True
    print("Parabéns! Você ficou famoso!")

def novo_amor(jogador):
    print("Novo amor!")
    if not jogador['casado']:        
        jogador['casado'] = True
        print("Parabéns! Você encontrou um novo amor.")
    else:
        print("Você já está casado!")

def maquina_do_tempo(jogador):
    print("Máquina do tempo!")
    print("Vish... Você voltou para o início do jogo...")
    jogador['posicao'] = 0

def mostrar_conquistas(jogador):
    print("===== Conquistas do Jogador =====")
    print(f"Posição final: {jogador['posicao']}")
    print(f"Filhos: {jogador['filhos']}")
    print(f"Casado: {jogador['casado']}")
    print(f"Ganhou na loteria: {jogador['loteria']}")
    print(f"Famoso: {jogador['famoso']}")
    print("=================================")

def mini_jogo_da_vida():
    #Criar os jogadores:
    jogador1 = criar_jogador()
    jogador2 = criar_jogador()        
    
    #Loop principal do jogo
    while True:
        #JOGADOR 1:
        input(f"Jogador 1 (posição {jogador1['posicao']}): Pressione Enter para jogar...")
        if jogador1['vivo']:
            jogador1['posicao'] += jogar_dado(jogador1)  #Avança na posição...
            verificar_posicao(jogador1)
            if jogador1['posicao'] >= 21:
                print("Jogador 1 alcançou a casa final! Fim do jogo!")
                mostrar_conquistas(jogador1)
                break
        
        #JOGADOR 2:
        input(f"Jogador 2 (posição {jogador2['posicao']}): Pressione Enter para jogar...")
        if jogador2['vivo']:
            jogador2['posicao'] += jogar_dado(jogador2)  #Avança na posição...
            verificar_posicao(jogador2)
            if jogador2['posicao'] >= 21:
                print("Jogador 2 alcançou a casa final! Fim do jogo!")
                mostrar_conquistas(jogador2)
                break

def verificar_posicao(jogador):      
    posicao = jogador['posicao']
    if posicao == 1:
        print("Rolou o dado.")
    elif posicao == 2:
        print("Casa da caveira. Você morreu! F, Game over!")
        jogador['vivo'] = False      
    elif posicao == 3:
        print("Rolou o dado novamente.")
    elif posicao == 4:
        desafio_matematico(jogador)
    elif posicao == 5:
        formatura(jogador)
    elif posicao == 6:
        ter_filho(jogador)
    elif posicao == 7:
        casamento(jogador)
    elif posicao == 8:
        print("Casa da caveira. Você morreu! F, Game over!")
        jogador['vivo'] = False
    elif posicao == 9:
        ter_filho(jogador)
    elif posicao == 10:
        desafio_matematico(jogador)
    elif posicao == 11:
        print("Divórcio!")
    elif posicao == 12:
        ter_filho(jogador)
    elif posicao == 13:
        ganhar_na_loteria(jogador)    
    elif posicao == 14:
        ficar_famoso(jogador)
    elif posicao == 15:
        novo_amor(jogador)
    elif posicao == 16:
        print("Rolou o dado.")
    elif posicao == 17:
        print("Casa da caveira. Você morreu! F, Game over!")
        jogador['vivo'] = False
    elif posicao == 18:
        desafio_matematico(jogador)
    elif posicao == 19:
        maquina_do_tempo(jogador)    
    elif posicao == 20:
        print("Fim, teve uma vida longa e próspera!")

#EXECUTAR O JOGO:
mini_jogo_da_vida()

########################## MINI JOGO DA VIDA ##########################