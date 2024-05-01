def media_unisinos(grau_a, grau_b):
    
    media_final = (grau_a + grau_b) / 2
    return media_final


nota_grau_a = float(input("nota do Grau A: "))
nota_grau_b = float(input("nota do Grau B: "))

media = media_unisinos(nota_grau_a, nota_grau_b)

print(f"A média final do aluno é: {media}")


