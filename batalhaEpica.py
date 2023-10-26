import random

print("-" * 10 + " FASE FINAL " + "-" * 10)


def azureSerpent(vida, ataque, defesa, quantidade_magia, poções, flechas, defesa_usada, magia_usada):
    vida = random.randint(40, 60)
    ataque = random.randint(10, 20)
    defesa = random.randint(10, 15)
    quantidade_magia = random.randint(8, 10)
    poções = 2
    flechas = 2
    defesa_usada = 0
    magia_usada = 0
    return vida, ataque, defesa, quantidade_magia, poções, flechas, defesa_usada, magia_usada


def Javagnar(vida, ataque, defesa, quantidade_magia):
    vida = random.randint(50, 70)
    ataque = random.randint(5, 10)
    defesa = random.randint(10, 20)
    quantidade_magia = random.randint(10, 15)
    return vida, ataque, defesa, quantidade_magia


def batalha(vida_azure, ataque_azure, defesa_azure, quantidade_magia_azure, poções_azure, flechas_azure,
            defesa_usada_azure, magia_usada_azure,
            vida_javagnar, ataque_javagnar, defesa_javagnar, quantidade_magia_javagnar):
    global trocar
    trocar = 0

    def atributos():
        print("-" * 10 + "SEUS ATRIBUTOS" + "-" * 10)
        print(f"Vida: {vida_azure:.1f}")
        print(f"Ataque: {ataque_azure}")
        print(f"Defesa: {defesa_azure}")
        print(f"Quantidade de magia: {quantidade_magia_azure}")
        print(f"Poções: {poções_azure}")
        print(f"Arco e Flecha dourado: {flechas_azure}")
        print(f"Defesa usada: {defesa_usada_azure}")
        print(f"Magia usada: {magia_usada_azure}")
        print("-" * 10 + "ATRIBUTOS DA JAVAGNAR" + "-" * 10)
        print(f"Vida: {vida_javagnar:.1f}")
        print(f"Ataque: {ataque_javagnar}")
        print(f"Defesa: {defesa_javagnar}")
        print(f"Quantidade de magia: {quantidade_magia_javagnar}")

    print("Você encontrou a Javagnar! Prepare-se para a batalha!")
    atributos()
    print("-" * 10 + "BATALHA" + "-" * 10)
    while trocar == 0 and vida_azure > 0:
        print("Escolha uma das opções para atacar: ")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Usar magia")
        print("4 - Usar poção")
        print("5 - Usar arco e flecha dourado")
        print("6 - Rever atributos de você e do Javagnar\n")
        escolha_usuario = input("Digite sua escolha: ")
        escolha_inimigo = random.randint(1, 4)
        tentativas = 2
        if escolha_usuario == "1":
            vida_javagnar -= ataque_azure - (ataque_azure * (defesa_javagnar * 2.5 / 100))
            trocar = 1
            print("-" * 10 + "OPÇÃO ESCOLHIDA: ATACAR" + "-" * 10)
            if vida_javagnar > 0:
                print(f"\nVocê atacou! Vida restante do boss: {vida_javagnar:.1f}")
            else:
                print(f"\nVocê atacou! Vida restante do boss: 0\n")
        elif escolha_usuario == "2":
            if tentativas > 0:
                defesa_azure += 5
                tentativas -= 1
                defesa_usada_azure += 1
                trocar = 1
                print("-" * 10 + "OPÇÃO ESCOLHIDA: DEFENDER" + "-" * 10)
                print(f"\nVocê defendeu! Sua defesa aumentou para {defesa_azure}!")
                print(f"Você possui {tentativas} tentativas restantes!")
            else:
                print("Você não pode mais defender nesta batalha!")
                trocar = 1
        elif escolha_usuario == "3":
            if quantidade_magia_azure > 0:
                vida_javagnar -= random.randint(5, 10)
                quantidade_magia_azure -= 1
                magia_usada_azure += 1
                trocar = 1
                print("-" * 10 + "OPÇÃO ESCOLHIDA: USAR MAGIA" + "-" * 10)
                if vida_javagnar > 0:
                    print(f"\nVocê usou magia! Vida restante do boss: {vida_javagnar:.1f}")
                else:
                    print(f"\nVocê usou magia! Vida restante do boss: 0")
                print(f"Você possui {quantidade_magia_azure} magias restantes!")
            else:
                print("Você não possui magias restantes!")
                trocar = 1
        elif escolha_usuario == "4":
            if poções_azure > 0:
                vida_azure += 10
                ataque_azure += 5
                poções_azure -= 1
                trocar = 1
                print("-" * 10 + "OPÇÃO ESCOLHIDA: USAR POÇÃO" + "-" * 10)
                print(
                    f"\nVocê usou uma poção! Sua vida aumentou para {vida_azure:.1f} e seu ataque aumentou para {ataque_azure}!")
                print(f"Você possui {poções_azure} poções restantes!")
            else:
                print("Você não possui poções restantes!")
                trocar = 1
        elif escolha_usuario == "5":
            if flechas_azure > 0:
                vida_javagnar -= 10
                flechas_azure -= 1
                trocar = 1
                print("-" * 10 + "OPÇÃO ESCOLHIDA: USAR ARCO E FLECHA DOURADO" + "-" * 10)
                if vida_javagnar > 0:
                    print(f"\nVocê usou o arco e flecha dourado! Vida restante do boss: {vida_javagnar:.1f}")
                else:
                    print(f"\nVocê usou o arco e flecha dourado! Vida restante do boss: 0\n")
                print(f"Você possui {flechas_azure} arcos e flechas dourados restantes!")
            else:
                print("Você não possui arcos e flechas dourados restantes!")
                trocar = 1
        elif escolha_usuario == "6":
            print("-" * 10 + "OPÇÃO ESCOLHIDA: VER ATRIBUTOS" + "-" * 10)
            atributos()
            trocar = 0
        else:
            print("Opção inválida!")
            trocar = 0

        while trocar == 1 and vida_javagnar > 0:
            if escolha_inimigo == 1:
                vida_azure -= ataque_javagnar - (ataque_javagnar * (defesa_azure * 2.5 / 100))
                trocar = 0
                print("\n" + "-" * 10 + "OPÇÃO ESCOLHIDA DO JAVAGNAR: ATACAR" + "-" * 10)
                if vida_azure > 0:
                    print(f"\nO JavaGnar atacou! Sua vida restante: {vida_azure:.1f}\n")
                else:
                    print(f"\nO JavaGnar atacou! Sua vida restante: 0\n")
            elif escolha_inimigo == 2:
                defesa_javagnar += 2
                trocar = 0
                print("\n" + "-" * 10 + "OPÇÃO ESCOLHIDA DO JAVAGNAR: DEFENDER" + "-" * 10)
                print(f"\nO JavaGnar defendeu! A defesa dele aumentou para {defesa_javagnar}!\n")
            elif escolha_inimigo == 3:
                if quantidade_magia_javagnar > 0:  
                    vida_azure -= random.randint(10, 15)
                    quantidade_magia_javagnar -= 1
                    trocar = 0
                    print("\n" + "-" * 10 + "OPÇÃO ESCOLHIDA DO JAVAGNAR: USAR MAGIA" + "-" * 10)
                    if vida_azure > 0:
                        print(f"\nO JavaGnar usou magia! Sua vida restante: {vida_azure:.1f}\n")
                    else:
                        print(f"\nO JavaGnar usou magia! Sua vida restante: 0\n")
                else:
                    trocar = 0
                    print("\n" + "-" * 10 + "OPÇÃO ESCOLHIDA DO JAVAGNAR: USAR MAGIA" + "-" * 10)
                    print(f"\nO JavaGnar não possui magias restantes!\n")
            elif escolha_inimigo == 4:
                vida_javagnar += 5
                ataque_javagnar += 2
                trocar = 0
                print("\n" + "-" * 10 + "OPÇÃO ESCOLHIDA DO JAVAGNAR: CURAR" + "-" * 10)
                print(
                    f"\nO JavaGnar usou uma poção! A vida dele aumentou para {vida_javagnar:.1f} e o ataque dele aumentou para {ataque_javagnar}!\n")
        if vida_azure <= 0:
            print("Você perdeu! Deseja recomeçar o jogo?")
            print("1 - Sim")
            print("2 - Não")
            escolha = input("Digite sua escolha: ")
            if escolha == "1":
                return batalha(vida_azure=random.randint(30, 50), ataque_azure=random.randint(10, 15),
                               defesa_azure=random.randint(10, 15), quantidade_magia_azure=random.randint(8, 10),
                               poções_azure=2, flechas_azure=2, defesa_usada_azure=0, magia_usada_azure=0,
                               vida_javagnar=random.randint(50, 70), ataque_javagnar=random.randint(5, 10),
                               defesa_javagnar=random.randint(10, 20), quantidade_magia_javagnar=random.randint(10, 15))
            else:
                print("Jogo finalizado!")
                break
        elif vida_javagnar <= 0:
            print("-" * 10 + "PARABÉNS! VOCÊ VENCEU!" + "-" * 10)
            print("1 - Sim")
            print("2 - Não")
            escolha = input("Digite sua escolha: ")
            if escolha == "1":
                return batalha(vida_azure=random.randint(30, 50), ataque_azure=random.randint(10, 15),
                               defesa_azure=random.randint(10, 15), quantidade_magia_azure=random.randint(8, 10),
                               poções_azure=2, flechas_azure=2, defesa_usada_azure=0, magia_usada_azure=0,
                               vida_javagnar=random.randint(50, 70), ataque_javagnar=random.randint(5, 10),
                               defesa_javagnar=random.randint(10, 20), quantidade_magia_javagnar=random.randint(10, 15))
            else:
                print("Jogo finalizado!")
                break


vida_azure, ataque_azure, defesa_azure, quantidade_magia_azure, poções_azure, flechas_azure, defesa_usada_azure, magia_usada_azure \
    = azureSerpent(vida=0, ataque=0, defesa=0, quantidade_magia=0, poções=0, flechas=0, defesa_usada=0, magia_usada=0)

vida_javagnar, ataque_javagnar, defesa_javagnar, quantidade_magia_javagnar = Javagnar(vida=0, ataque=0, defesa=0,
                                                                                      quantidade_magia=0)

batalha(vida_azure, ataque_azure, defesa_azure, quantidade_magia_azure, poções_azure, flechas_azure, defesa_usada_azure,
        magia_usada_azure, vida_javagnar, ataque_javagnar, defesa_javagnar, quantidade_magia_javagnar)
