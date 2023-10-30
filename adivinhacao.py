import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

# numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade deseja?")
print("(1) - Fácil")
print("(2) - Médio")
print("(3) - Difícil")

nivel = int(input("Digite o nível escolhido: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# while (rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
            if (rodada == total_de_tentativas):
                print ("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
            if (rodada == total_de_tentativas):
                print ("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    # rodada = rodada + 1

print("Fim do jogo")