print("ACERTE O NOME  SECRETO!!!")

lista_nomes = ['Matheus', 'Laura', 'André', 'Ricardo', 'Letícia']
alvo = 'Matheus'

for alvo in lista_nomes:
    entrada = input("Digite um nome: ")
    if entrada == alvo:
        print(f"Acertou o nome secreto: {alvo}")
        break
    else:
        print("Errou! Tente Novamente")