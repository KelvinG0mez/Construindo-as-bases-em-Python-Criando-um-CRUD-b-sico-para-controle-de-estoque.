print("==== E S T O Q U E ====")

estoque = []

while (True):

    print("""
    Escolha uma opção:      
    [1] ADICIONAR 
    [2] REMOVER
    [3] VIZUALIZAR
    [4] SAIR 
                        """)

    escolha = int(input("Digite uma das opções: "))

    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
        print("ESCOLHA INVALIDA...")
        continue

    else:

        if escolha == 1:
            print("ADICIONAR ITEM:")
            add_item = str(input("Digite o item que vc deseja ADICIONAR no ESTOQUE:"))
            estoque.append(add_item)
            print(f'{estoque}')
            print("ITEM ADCIONADO...")

        if escolha == 2:
            print("REMOVER ITEM:")
            remove_item = str(input("Digite o item que você deseja REMOVER do ESTOQUE:"))
            estoque.remove(remove_item)
            print(f'{estoque}')
            print("ITEM REMOVIDO...")

        if escolha == 3:
            print("VIZUALIZAR:")
            print(estoque)

        if escolha == 4:
            print("FINALIZANDO PROGRAMA...")
            break
