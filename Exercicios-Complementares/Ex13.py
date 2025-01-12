print("""
    --------- Menu ---------
    [ 1 ] -> Inserir Produto:
    [ 2 ] -> Remover Produto:
    [ 3 ] -> Sair
    --------- Menu ----------
""")

escolha_convertido_para_int = 0
indice_para_remover_item_convertido = 0 # Indice convertido para int
manter_item = ''
indice_para_remover_item = 0 # Variável definida para escolha do usuário

escolha_valida = None
indice_valido_para_remover_item = None 

lista_de_produtos = ["Maçã", "Uva", "Luvas", "Vassoura", "Carne"]
while True:
    escolha = input("Informe sua escolha: ")
    
    if len(escolha) > 1:
        print("Informe apenas um valor!!")
        print('\n')
        continue
    
    try:
        escolha_convertido_para_int = int(escolha)
        escolha_valida = True
    except:
        escolha_valida = None

    if escolha_valida is None:
        print("Informe um valor válido!")
        print('\n')
        continue

    if escolha_convertido_para_int == 1:
        novo_produto = input("Informe o nome do produto: ").capitalize()

        if novo_produto.isnumeric():
            print("Informe um produto válido!")
            print('\n')
            continue

        if novo_produto in lista_de_produtos:
            print("A lista de produtos já contém este item!")
            manter_item = input("Você quer inserir o item mesmo assim (s/n)? ").lower()

            if manter_item.startswith('s'):
                lista_de_produtos.append(novo_produto)
            else:
                continue

        else:
            lista_de_produtos.append(novo_produto)

    elif escolha_convertido_para_int == 2:
        print("Itens da lista atual!")
        for itens in lista_de_produtos:
            print(itens, end=' ')
        print('\n')

        print("O primeiro item da lista começa em 0!")
        indice_para_remover_item = input("Qual o indice do produto a ser removido? ")

        try:
            indice_para_remover_item_convertido = int(indice_para_remover_item)
            indice_valido_para_remover_item = True
        except:
            indice_valido_para_remover_item = None
        
        # Removendo o item pedido pelo usuário!
        lista_de_produtos.pop(indice_para_remover_item_convertido)
        print("Lista atual")
        for itens in lista_de_produtos:
            print(itens, end=' ')
        print('\n')
    
    elif escolha_convertido_para_int == 3:
        print("Você saiu do programa!")
        print("Lista atual")
        for itens in lista_de_produtos:
            print(itens, end=' ')
        print('\n')
        print("Obrigado por utilizar o programa!!")
        break
    
    else:
        print("Opção inválida!")
        break