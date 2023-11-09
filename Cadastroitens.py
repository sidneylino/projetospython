#algoritmo para cadastramento de produtos
#criado por Sidney Lino

opcao = int(input("selecione a opção:\n[1]cadastrar produtos\n[2]buscar produtos\n[3]encerrar"))
catalogo = []
while opcao == 1:
    nome = input("nome:")
    quantidade = input("quantos?")
    produto = [nome,quantidade]
    catalogo.append(produto)
    opcao = int(input("[1] Cadastrar novo produto \n[2]buscar produtos\n [3]Encerrar"))
    if opcao == 2:
        print("quantidade de produtos:", len(catalogo))
        for n in catalogo:
            nome = n[0]
            quantidade = n[1]
            print("produto:", nome, "quantidade:", quantidade)
    elif opcao == 3:
        print("programa encerrado")
    else:
        opcao = int(input("Opção invalida, digite novamente:"))








