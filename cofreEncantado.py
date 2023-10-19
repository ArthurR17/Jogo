import random

print("-" * 10 + " FASE 3 " + "-" * 10)
print("Você encontrou um cofre mágico! Para abri-lo, você deve acertar o número secreto!")
numero = random.randint(1, 100)


def abrirCofre(numero, numero_usuario):
    tentativas = 10
    while True:
        numero_usuario = int(input("Digite um número de 1 a 100: "))
        print(f"Você tem {tentativas} tentativas restantes!")
        if numero_usuario == numero:
            print("Parabéns! Você acertou o número secreto!")
            return False
        elif numero_usuario < numero:
            tentativas -= 1
            print("O número secreto é menor que o número digitado!")
        elif numero_usuario > numero:
            tentativas -= 1
            print("O número secreto é maior que o número digitado!")


abrirCofre(numero, numero_usuario=0)
