print("-" * 10 + " FASE 5 " + "-" * 10)

def treinoArqueiro(nivel, xp, quantidade_flechas):
    nivel = int(input("Digite seu nível: "))
    quantidade_flechas = int(input("Digite a quantidade de flechas que você possui: "))
    validacao = lambda nivel, quantidade_flechas: nivel >= 10 and quantidade_flechas >= 100
    if validacao(nivel, quantidade_flechas):
        while True:
            treinamento = input("Você deseja treinar para aumentar seus atributos? (S/N): ")
            if treinamento != "N":
                xp_requerido = nivel * 15
                xp += 10
                print("*" * 40)
                print(f"Xp atual: {xp}")
                print(f"Xp necessário para o próximo nível: {xp_requerido}")
                print("*" * 40)
                if xp >= xp_requerido:
                    nivel += 1
                    print(f"Você subiu de nível! Nível atual: {nivel}\n")
            else:
                print("Você pode passar para a próxima fase!\n")
                return False


treinoArqueiro(nivel=0, xp=0, quantidade_flechas=0)

