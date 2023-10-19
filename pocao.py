print("-" * 10 + " FASE 2 " + "-" * 10)


def criarPocao(quantidade_ervas, quantidade_agua, nivel_alquimia, xp):
    receita = {
        "ervas": 10,
        "agua": 50,
    }
    validacao = lambda nivel_alquimia: nivel_alquimia >= 5
    while True:
        treinamento = input(f"Você deseja treinar para aumentar seu nível de alquimia? (S/N): ")
        if treinamento == "S":
            xp_requerido = nivel_alquimia * 15
            xp += 10
            print("*" * 40)
            print(f"Xp atual: {xp}")
            print(f"Xp necessário para o próximo nível: {xp_requerido}")
            print("*" * 40)
            if xp >= xp_requerido:
                nivel_alquimia += 1
                print(f"Você subiu de nível! Nível atual: {nivel_alquimia}\n")
                print("*" * 40)
        else:
            break
        while validacao(nivel_alquimia):
            if validacao(nivel_alquimia):
                quantidade_ervas = int(input("Digite a quantidade de ervas que você possui: "))
                quantidade_agua = int(input("Digite a quantidade de água que você possui: "))
                if quantidade_ervas >= receita["ervas"] and quantidade_agua >= receita["agua"]:
                    print("*" * 40)
                    print("Você criou uma poção! Pode passar para a próxima fase!")
                    return False
                else:
                    print("Você não possui os ingredientes necessários para criar a poção!")
                    print(f"Quantidade de ervas restantes: {receita['ervas'] - quantidade_ervas}")
                    print(f"Quantidade de água restante: {receita['agua'] - quantidade_agua}")


criarPocao(quantidade_ervas=0, quantidade_agua=0, nivel_alquimia=1, xp=0)
