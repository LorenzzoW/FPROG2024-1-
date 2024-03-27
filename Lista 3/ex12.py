#Idade do nadador
idade = int(input("Digite a idade do nadador: "))

#Inicializa a categoria como vazia
categoria = ""

if idade >= 5:
 if idade <=7:
    categoria = "Infantil A"

if idade >= 8:
  if idade <=10:
     categoria = "Infantil B"

if idade >= 11:
  if idade <=13: 
     categoria = "Juvenil A"

if idade >= 14:
   if idade <= 17:
      categoria = "Juvenil B"

if idade > 18:
    categoria = "Sênior"

#Imprime a categoria do nadador
if categoria:
  print("Categoria do nadador:", categoria)

else:
  print("Idade fora das categorias disponíveis.")