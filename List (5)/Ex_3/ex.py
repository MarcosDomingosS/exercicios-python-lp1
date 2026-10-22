def exibirMenu():
    resultado = False
    while not resultado:
        opcao = int(input("Selecione a opção:\n"
                           "1 - Cadastrar produto\n"
                           "2 - Calcular valor do estoque\n"
                           "3 - Buscar produto\n"
                           "4 - Listar produtos\n"
                           "5 - Sair\n" ))
        if opcao >= 1 and opcao <= 5:
            resultado = True
        else:
            print("Opção inválida!")
 
    return opcao
 
def cadastrarProduto(produtos, nome, preco, quantidade):
    produtos.append([nome, preco, quantidade])
 
def calcularValorEstoque(produtos):
    soma = 0
    for produto in produtos:
        soma += produto[1] * produto[2]
    return soma
 
def buscarProduto(produtos, nome):
    for produto in produtos:
        if produto[0].lower() == nome.lower():
            return produto
    return None
 
def listarProdutos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"Nome: {produto[0]} | Preço: R$ {produto[1]:.2f} | Quantidade: {produto[2]}")
 
produtos = []
 
while True:
    opcao = exibirMenu()
 
    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
 
        cadastrarProduto(produtos, nome, preco, quantidade)
        print("Produto cadastrado com sucesso!")
 
    elif opcao == 2:
        valor = calcularValorEstoque(produtos)
        print(f"Valor total do estoque: R$ {valor:.2f}")
 
    elif opcao == 3:
        nome = input("Digite o nome do produto que deseja buscar: ")
        produto = buscarProduto(produtos, nome)
 
        if produto is not None:
            print(f"Nome: {produto[0]} | Preço: R$ {produto[1]:.2f} | Quantidade: {produto[2]}")
        else:
            print("Produto não encontrado.")
 
    elif opcao == 4:
        listarProdutos(produtos)
 
    elif opcao == 5:
        print("Saindo do programa...")
        break
 