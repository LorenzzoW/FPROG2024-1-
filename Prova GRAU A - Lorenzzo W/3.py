############################################################################################

               #PROVA GRAU A EXERCÍCIO 3: 


#ingredientes (ESTOQUE)
estoque = {
    'Pó de Fênix': 100,
    'Essência Celestial': 50,
    'Raiz de Dragão': 45,
    'Orvalho Lunar': 30,
    'Flores secas': 200,
    'Elixir amargo': 20,
    'Lágrimas de unicórnio': 15
}

#Lisyinha com as poções e seus ingredientes necessários para fabricação
pocoes = {
    'Poção de Cura': {'Pó de Fênix': 30, 'Essência Celestial': 20, 'Flores secas': 2},
    'Poção Força da Floresta': {'Orvalho Lunar': 20, 'Raiz de Dragão': 30},
    'Poção Sabedoria da Riqueza': {'Essência Celestial': 30, 'Pó de Fênix': 50},
    'Poção Sorte no Amor': {'Orvalho Lunar': 10, 'Flores secas': 50},
    'Poção Malvada': {'Elixir amargo': 10, 'Raiz de Dragão': 15}
}

#consulta o estoque atual de ingredientes
def consultar_estoque():
    print("\nIngredientes disponíveis:")
    for ingrediente, quantidade in estoque.items():
        print(f"{ingrediente}: {quantidade} g/ml")

#preparar uma poção
def preparar_pocao():
    print("\nPoções disponíveis:")
    #Mostra as poções disponíveis praescolha
    for pocao in ['Poção de Cura', 'Poção Força da Floresta', 'Poção Sabedoria da Riqueza', 'Poção Sorte no Amor', 'Poção Malvada']:
        print(pocao)
    
    nome_poção = input("\nDigite o nome da poção que deseja preparar: ")
    
    if nome_poção not in pocoes:
        print("Nome de poção inválido.")
        return
    
    ingredientes_necessarios = pocoes[nome_poção]
    print(f"\nIngredientes da {nome_poção}:")
    for ingrediente, quantidade in ingredientes_necessarios.items():
        print(f"{ingrediente}: {quantidade} g/ml")

    ingredientes_faltando = []

    # OsIngredientes suficientes em estoque
    for ingrediente, quantidade_necessaria in ingredientes_necessarios.items():
        if estoque.get(ingrediente, 0) < quantidade_necessaria:
            ingredientes_faltando.append(ingrediente)

    if ingredientes_faltando:
        print(f"\nFaltam ingredientes para preparar a {nome_poção}: {', '.join(ingredientes_faltando)}")
    else:
        #atualiza o estoque após preparar uma poção 0w0
        for ingrediente, quantidade_necessaria in ingredientes_necessarios.items():
            estoque[ingrediente] -= quantidade_necessaria
        print("\nPoção criada com sucesso!")

#Loop para o programa
while True:
    print("\nMenu:")
    print("1 - Preparar uma poção")
    print("2 - Consultar igredientes disponíveis")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        preparar_pocao()
    elif opcao == '2':
        consultar_estoque()
    elif opcao == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente!!!!")

##########################################################################################