#Programa de sistema de gerenciamento de estoque

#Definindo a classe Pai que no caso é o Produto que vai armazenar as informações de produto até o momento vazias.
class Produtocl():
    codigo = 0
    nome = ""
    preco = 0.0
    quantidade = 0

#Definindo a classe principal que vai realizar as demais funções, herdando os atributos de Produtocl.
class Principal(Produtocl):

    #Função responsável por inserir as informações na classe Produto.
    def inserir(self):
        produto.codigo = int(input("Insira o código do produto: "))
        produto.nome = str(input("Insira o nome do produto: "))
        produto.preco = float(input("Insira o preço do produto: "))
        produto.quantidade = int(input("Insira a quantidade do produto: "))
        print("\nProduto: ", produto.nome, " inserido com sucesso! \n\n")
        main.menu()

    #Função responsável por analisar se existe um produto, exibe também a quantidade em estoque e preço.
    def result_consulta(self):
        consulta = input("Insira o nome do produto: ")
        if consulta in produto.nome:
            print("\n ### O produto ", produto.nome, " possui ", produto.quantidade, " em estoque e seu preço é: ", produto.preco, " reais \n")
            main.menu()

        else:
            print("\n ### Não existe produto com nome de: ", consulta, ".\n\n")
            main.menu()

    # Função que tem o propósito de menu, através dela será feita a operação principal do programa 
    # e será chamada ao fim de cada operação para não encerrar o programa de maneira ineficiente.
    def menu(self):
        print("MENU PRINCIPAL ")
        print("Insira o número correspondente a ação: ")
        print("1 - Inserir um produto ")
        print("2 - Consultar um produto ")
        print("3 - Fechar ")

        resposta = input("Opção: ")

        # Analisa a resposta do menu.
        if resposta == "1":
            main.inserir()
        
        if resposta == "2":
            main.result_consulta()

        elif resposta == "3":
            print("Programa encerrado! ")

        # Aqui é uma parte especial do menu que ocorre caso o valor digitado seja inválido, fazendo assim
        # o usuário voltar ao menu principal para tentar novamente, isenta o fechamento do programa em caso de erro.
        else:
            print("\n ### Dígito incorreto, por favor insira um valor válido \n")
            main.menu()


#Chamada de classes e funções.
produto = Produtocl()
main = Principal()
main.menu()