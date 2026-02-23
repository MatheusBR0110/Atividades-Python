print("ACERTE A SENHA!!!")

lista_senha = [75983, 28508, 49607, 29587, 01107]
alvo = '01107'
rodada = 1

while True:
    entrada = int(input('Digite uma senha: '))
    if entrada == alvo:
        print(f"Senha Aceita: {alvo}")
        break
    else:
        print("Senha Incorreta")