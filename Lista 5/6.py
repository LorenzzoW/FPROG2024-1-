import random

# Função para simular a abertura de uma caixa
def abrir_caixa():
    # Probabilidades de obtenção de cada tipo de item
    prob_comum = 0.8
    prob_raro = 0.19
    prob_lendario = 0.01
    
    # Realiza o sorteio para determinar o tipo de item
    sorteio = random.random()
    if sorteio < prob_comum:
        print("Você coletou 1 item comum!")
        return "comum"
    elif sorteio < prob_comum + prob_raro:
        print("Você coletou 1 item raro!")
        return "raro"
    else:
        print("Você coletou 1 item lendário!")
        return "lendário"

# Função para consultar os itens coletados
def consultar_itens(inventario):
    print("Itens coletados:")
    print("Itens comuns:", inventario["comum"])
    print("Itens raros:", inventario["raro"])
    print("Itens lendários:", inventario["lendario"])

# Função principal do programa
def main():
    inventario = {"comum": 0, "raro": 0, "lendario": 0}
    
    while True:
        print("\n1 - Abrir uma caixa")
        print("2 - Consultar itens")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            tipo_item = abrir_caixa()
            inventario[tipo_item] += 1
        elif escolha == "2":
            consultar_itens(inventario)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")

if __name__ == "__main__":
    main()
