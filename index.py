from livros import cadastrarLivro, verLivros, deletarLivro, atualizarLivro
from usuarios import cadastrarUsuario, verUsuarios, deletarUsuario, atualizarUsuario
from emprestimos import cadastrarEmprestimo, deletarEmprestimo
from prettytable import PrettyTable

resposta = ""
tabela = PrettyTable(["Opção", "Ação"]) 
tabela.add_rows([
    ["1", "Cadastrar um novo livro"],
    ["2", "Cadastrar um novo usuário"],
    ["3", "Consultar todos os usuários"],
    ["4", "Consultar todos os livros"],
    ["5", "Emprestar livro"],
    ["6", "Deletar empréstimo"],
    ["7", "Deletar livro"],
    ["8", "Deletar usuário"],
    ["9", "Atualizar usuário"],
    ["10", "Atualizar Livro"],
    ["0", "Sair do programa"]
])
i = 0

while True:
    if i > 0:
        a = input("Quer continuar o programa? (s) ").lower()
        if a != "s":
            break
    print(tabela)
    resposta = int(input("Digite o número da opção: "))
    while resposta not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0] or resposta == "":
        print(tabela)
        resposta = int(input("Digite o número da opção: "))

    if resposta == 1:
        id = cadastrarLivro()
        if id:
            print(f"Livro cadastrado com sucesso com id: {id}")
        continue
    elif resposta == 2:
        id = cadastrarUsuario()
        if id:
            print(f"Usuário cadastrado com sucesso com id: {id}")
        continue
    elif resposta == 3:
        usuarios = verUsuarios()

        for usuario in usuarios:
            print("------------------------")
            print(f"nome: {usuario['nome']}")
            print(f"idade: {usuario['idade']}")
            print(f"matricula: {usuario['matricula']}")
            print(f"curso: {usuario['curso']}")
            print(f"nome do autor preferido: {usuario['autorPreferido']}")
        continue
    elif resposta == 4:
        livros = verLivros()
        for livro in livros:
            print("------------------------")
            print(f"nome: {livro['name']}")
            print(f"autor: {livro['author']}")
            print(f"preço: {livro['price']}")
        continue
    elif resposta == 5:
        id = cadastrarEmprestimo()
        if id:
            print("Empréstimo feito com sucesso.")
        continue
    elif resposta == 6:
        deleted = deletarEmprestimo()
        if deleted:
            print("Emprestimo deletado com sucesso.")
        else:
            print("Erro ao deletar empréstimo.")
        continue
    elif resposta == 7:
        deleted = deletarLivro()
        if deleted:
            print("Livro deletado com sucesso.")
        else:
            print("Erro ao deletar livro.")
    elif resposta == 8:
        deleted = deletarUsuario()
        if deleted:
            print("Usuário deletado com sucesso.")
        else:
            print("Erro ao deletar usuário.")
    elif resposta == 9:
        if atualizarUsuario() == 0:
            print("Usuário atualizado com sucesso")
    elif resposta == 10:
        if atualizarLivro() == 0:
            print("Livro atualizado com sucesso")
    else:
        break
    i += 1
        