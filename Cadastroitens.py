menu = int(input("selecione a opção:\n[1]cadastrar produtos\n[2]buscar produtos\n[3]encerrar"))
if menu == 1:
    x=1
    produtos = []
    while (x == 1):
        nome = input("nome:")
        quantidade = input("quantos?")
        prod = [nome,quantidade]
        produtos.append(prod)
    x = input("continuar cadastrando tecle 1, fi")
print("quantidade de prdutos", len(produtos))
for n in produtos:
    nome = n[0]
    quantidade = n[1]
    print("o produto é", nome,"tem a quantidade:", quantidade)

