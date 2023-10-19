def forjarEspada(nome, nivel, xp, quantidade_magia):
    validacao = lambda nivel, quantidade_magia: nivel >= 20 and quantidade_magia >= 250
    while True:
        treinamento = input(f"{nome}, você deseja treinar para aumentar seus atributos? (S/N): ")
        if treinamento == "S":
            xp_requerido = nivel * 15
            xp += 10
            quantidade_magia += 2
            print("*" * 40)
            print(f"Xp atual: {xp}")
            print(f"Xp necessário para o próximo nível: {xp_requerido}")
            print(f"Magia atual: {quantidade_magia}")
            print("*" * 40)
            if xp >= xp_requerido:
                quantidade_magia += 10
                nivel += 1
                print(f"{nome}, você subiu de nível! Nível atual: {nivel}\n")
        else:
            break
        if validacao(nivel, quantidade_magia):
            print(f"{nome}, você pode passar para a próxima fase!\n")
            return False


forjarEspada(nome=(input("Digite seu nome: ")), nivel=1, xp=0, quantidade_magia=0)

