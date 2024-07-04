import csv

# Leitura do arquivo CSV
with open('Gatos.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    matriz = list(reader)

# Função para salvar as alterações no arquivo CSV (opção 6 no menu)
def salvar(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for linha in matriz:
            writer.writerow(linha)

# Função para exibir o menu
def exibir_menu():
    print("\n----- MENU -----")
    print("1. Cadastrar felino")
    print("2. Alterar status de felino")
    print("3. Consultar informações sobre felino")
    print("4. Apresentar estatísticas gerais")
    print("5. Filtragem de dados")
    print("6. Salvar e sair")
    print("----------------")

# Função para cadastrar um novo felino
def cadastrar_felino():
    global matriz
    novo_gato = []
    for coluna in matriz[0]:
        valor = input(f"Informe {coluna}: ")
        novo_gato.append(valor)
    matriz.append(novo_gato)
    print("Felino cadastrado com sucesso!")

# Função para alterar o status de um felino
def alterar_status_felino():
    global matriz
    if len(matriz) <= 1:
        print("Não há felinos cadastrados.")
        return

    print("Selecione o felino para alterar o status:")
    for i, gato in enumerate(matriz[1:], start=1):
        print(f"{i}. {gato[0]}")  # Assumindo que a primeira coluna é o nome

    try:
        escolha = int(input("Escolha o número do felino: ")) - 1
        if escolha < 0 or escolha >= len(matriz) - 1:
            print("Escolha inválida.")
            return

        print("Status atual do felino:")
        for j, valor in enumerate(matriz[escolha + 1]):
            print(f"{matriz[0][j]}: {valor}")

        while True:
            opcao = input("Digite o número da informação que deseja alterar (ou 's' para sair): ")
            if opcao.lower() == 's':
                break
            elif opcao.isdigit() and 1 <= int(opcao) <= len(matriz[0]):
                coluna = int(opcao) - 1
                novo_valor = input(f"Novo valor para {matriz[0][coluna]}: ")
                matriz[escolha + 1][coluna] = novo_valor
            else:
                print("Opção inválida. Tente novamente.")
        
        print("Status do felino atualizado com sucesso!")

    except ValueError:
        print("Opção inválida.")

# Função para consultar informações de um felino
def consultar_informacoes():
    global matriz
    if len(matriz) <= 1:
        print("Não há felinos cadastrados.")
        return

    print("Selecione o felino para consultar informações:")
    for i, gato in enumerate(matriz[1:], start=1):
        print(f"{i}. {gato[0]}")  # Assumindque a primeira coluna é o nome

    try:
        escolha = int(input("Escolha o número do felino: ")) - 1
        if escolha < 0 or escolha >= len(matriz) - 1:
            print("Escolha inválida.")
            return
        
        print("\nInformações do felino selecionado:")
        for j, valor in enumerate(matriz[escolha + 1]):
            print(f"{matriz[0][j]}: {valor}")

    except ValueError:
        print("Opção inválida.")

# Função para exibir estatísticas gerais....
def exibir_estatisticas():
    global matriz
    if len(matriz) <= 1:
        print("Não há felinos cadastrados para calcular estatísticas.")
        return

    total_gatos = len(matriz) - 1
    machos = len([gato for gato in matriz[1:] if gato[1].upper() == 'M'])
    femeas = total_gatos - machos

    adotados = len([gato for gato in matriz[1:] if gato[9].upper() == 'SIM'])
    nao_adotados = total_gatos - adotados

    negativos_FIV_FELV = len([gato for gato in matriz[1:] if gato[6].upper() == 'NÃO' and gato[7].upper() == 'NÃO'])
    apenas_FIV_positivos = len([gato for gato in matriz[1:] if gato[6].upper() == 'SIM' and gato[7].upper() == 'NÃO'])
    apenas_FELV_positivos = len([gato for gato in matriz[1:] if gato[6].upper() == 'NÃO' and gato[7].upper() == 'SIM'])
    ambos_positivos = len([gato for gato in matriz[1:] if gato[6].upper() == 'SIM' and gato[7].upper() == 'SIM'])

    print("\n----- ESTATÍSTICAS GERAIS -----")
    print(f"Porcentagem de machos: {machos / total_gatos * 100:.2f}%")
    print(f"Porcentagem de fêmeas: {femeas / total_gatos * 100:.2f}%")
    print(f"Porcentagem de adotados: {adotados / total_gatos * 100:.2f}%")
    print(f"Porcentagem de não adotados: {nao_adotados / total_gatos * 100:.2f}%")
    print(f"Porcentagem de felinos sem FIV+ e FELV+: {negativos_FIV_FELV / total_gatos * 100:.2f}%")
    print(f"Porcentagem de felinos apenas FIV+: {apenas_FIV_positivos / total_gatos * 100:.2f}%")
    print(f"Porcentagem de felinos apenas FELV+: {apenas_FELV_positivos / total_gatos * 100:.2f}%")
    print(f"Porcentagem de felinos com FIV+ e FELV+: {ambos_positivos / total_gatos * 100:.2f}%")

# Função para realizar filtragem de dados;
def realizar_filtragem():
    global matriz
    if len(matriz) <= 1:
        print("Não há felinos cadastrados para realizar filtragem.")
        return

    print("\n----- FILTRAGEM DE DADOS -----")
    print("1. Consultar gatos resgatados por período")
    print("2. Consultar gatos adotados por período")

    opcao = input("Escolha uma opção de filtragem: ")

    if opcao == '1':
        ano_inicio = int(input("Digite o ano de início: "))
        ano_fim = int(input("Digite o ano de fim: "))

        gatos_resgatados = [gato for gato in matriz[1:] if int(gato[8].split('/')[2]) >= ano_inicio and int(gato[8].split('/')[2]) <= ano_fim]
        if gatos_resgatados:
            print("\nGatos resgatados no período:")
            for gato in gatos_resgatados:
                print(gato[0])
        else:
            print("Nenhum gato resgatado no período especificado.")

    elif opcao == '2':
        ano_inicio = int(input("Digite o ano de início: "))
        ano_fim = int(input("Digite o ano de fim: "))

        gatos_adotados = [gato for gato in matriz[1:] if gato[9].upper() == 'SIM' and int(gato[10].split('/')[2]) >= ano_inicio and int(gato[10].split('/')[2]) <= ano_fim]
        if gatos_adotados:
            print("\nGatos adotados no período:")
            for gato in gatos_adotados:
                print(gato[0])
        else:
            print("Nenhum gato adotado no período especificado.")

    else:
        print("Opção inválida.")

# Função principal do programa:
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_felino()
        elif opcao == "2":
            alterar_status_felino()
        elif opcao == "3":
            consultar_informacoes()
        elif opcao == "4":
            exibir_estatisticas()
        elif opcao == "5":
            realizar_filtragem()
        elif opcao == "6":
            salvar('Gatos.csv', matriz)
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa >o<
if __name__ == "__main__":
    main()