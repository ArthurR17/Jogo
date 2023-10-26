import random

print("-" * 10 + " FASE 4 " + "-" * 10)


def resolverEnigma(valida_resposta):
    palavra = random.choice(["Espada", "Escudo", "Armadura", "Elmo", "Cajado", "Poção", "Flecha", "Adaga", "Machado", "Arco"]).lower().strip()
    digitadas = []
    acertos = []
    erros = 0
    while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else "_"
        print(senha)
        if senha == palavra:
            print("Você acertou! Pode passar para a próxima fase!")
            break
        resposta_usuario = input("\nDigite uma letra: ").lower().strip()
        if resposta_usuario in digitadas:
            print("Você já tentou esta letra!")
            continue
        digitadas.append(resposta_usuario)
        if resposta_usuario in palavra:
            acertos.append(resposta_usuario)
        else:
            erros += 1
            print("Você errou!")
        print("X==:==\nX  :  ")
        print("X  O  " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " \|  "
        elif erros >= 4:
            linha2 = " \|/ "
        print("X%s" % linha2)
        linha3 = ""
        if erros == 5:
            linha3 += " /   "
        elif erros >= 6:
            linha3 += " / \ "
        print("X%s" % linha3)
        print("X\n===========")
        if erros == 6:
            print("Enforcado!")
            break
        if valida_resposta(resposta_usuario):
            print("Você validou a resposta do enigma!")
            return False


def valida_resposta(resposta_usuario):
    return resposta_usuario == "resposta_correta"


resolverEnigma(valida_resposta)
