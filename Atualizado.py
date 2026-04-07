import os
import time

estoque = {}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

limpar_tela()

def exibir_menu():

        print("Escolha uma opção:")      
        print("[1] ADICIONAR") 
        print("[2] REMOVER")
        print("[3] VIZUALIZAR")
        print("[4] SAIR\n") 
        return input("Digite uma das opções: ")

def adicionar_item():
    print("="*30)
    print("ADICIONAR ITEM:\n")

    add_item_chave = str(input("ADICIONAR no ESTOQUE:"))

    try:
        add_item_valor = int(input(f"Valor UNIDADE {add_item_chave}: R$"))
        quantidade = int(input("QUANTIDADE: "))
        estoque[add_item_chave] = {"valor": add_item_valor, "quantidade": quantidade}

        print("ITEM ADCIONADO.\n")
        time.sleep(2)
        limpar_tela()

    except ValueError:
         print("\n[!] ERRO: O valor deve ser um numero inteiro!")
         time.sleep(2)
         limpar_tela()

def remover_item():

    print("="*30)
    print("REMOVER ITEM:\n")

    remove_item = str(input("REMOVER do ESTOQUE:"))

    if remove_item in estoque:
            
            del estoque[remove_item]
            print("ITEM REMOVIDO...\n")
            time.sleep(2)
            limpar_tela()
    else: 
                print("Erro: Este item nao está no estoque.")
                time.sleep(2)
                limpar_tela()

def visualizar_estoque():

    print("="*30)
    print("VIZUALIZAR ESTOQUE:\n")

    if not estoque:
        print("O estoque está vazio!")
    else:
        for nome, dados in estoque.items(): 

            valor = dados["valor"]
            quantidade = dados["quantidade"]

            print(f"Produto: {nome} | Valor: R${valor:.2f} | Estoque: {quantidade}uni")
    
    print("\n" + "="*30)
    input("Pressione Enter para continuar...") 
    limpar_tela()

print("==== E S T O Q U E ====\n")

while (True):

    escolha = exibir_menu()
        
    match escolha:

        case "1":
            adicionar_item()

        case "2":
           remover_item()

        case "3":            
            visualizar_estoque()
                
        case "4":
            print("FINALIZANDO PROGRAMA...")
            break
        
        case _:
            print("ERRO: Opção inválida! Escolha entre 1 e 4")
            time.sleep(2)
            limpar_tela()
