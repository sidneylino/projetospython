opcao = int(input("selecione a opção:\n[1]cadastrar produtos\n[2]buscar produtos\n[3]encerrar"))
if opcao == 1:
    x=1
    catalogo = []
    while x == 1:
        nome = input("nome:")
        quantidade = input("quantos?")
        produto = [nome,quantidade]
        catalogo.append(produto)
        x = int(input("[1] Cadastrar novo produto \n[2]buscar produtos\n [3]Encerrar"))

print("quantidade de produtos:", len(produtos))
for n in produtos:
    nome = n[0]
    quantidade = n[1]
    print("o produto é", nome,"tem a quantidade:", quantidade)

