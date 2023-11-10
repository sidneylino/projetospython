#algoritmo para cadastramento de produtos
#criado por Sidney Lino
encerrar = 1
catalogo = []
while encerrar == 1:
    print("-"*42)
    opcao = int(input("selecione a opção:\n[1]cadastrar produtos\n[2]buscar produtos\n[3]encerrar\n"+"-"*42))
    if opcao == 1:
        nome = input("nome:")
        quantidade = input("quantos?")
        produto = [nome,quantidade]
        catalogo.append(produto)
    elif opcao == 2:
        print("quantidade de produtos:", len(catalogo))
        for n in catalogo:
            nome = n[0]
            quantidade = n[1]
            print("produto:", nome, "quantidade:", quantidade)

    elif opcao == 3:
        encerrar = 2
    else:
        opcao = int(input("Opção invalida, digite novamente:"))








