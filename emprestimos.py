from db import get_database
from usuarios import buscarUsuario
from livros import verLivroPorNome

client = get_database()

db = client["top"]
lend = db.emprestimos

def cadastrarEmprestimo():
    matricula = input("Digite sua matricula: ")
    nome = input("Digite o nome do livro que quer emprestar: ")

    if not buscarUsuario(matricula):
        print("Essa matrícula não existe")
        return
    if not verLivroPorNome(nome):
        print("Esse livro não existe")
        return
    
    if nome in verEmprestimo(nome):
        print("Esse livro já foi emprestado.")
        return

    data = {
        "matricula": matricula,
        "nome_do_livro": nome,
    }

    insertedLend = lend.insert_one(data)
    return insertedLend.inserted_id

def verLivros():
    return lend.find()

def verEmprestimo(nome):
    emprestimos = []
    for emprestimo in lend.find():
        emprestimos.append(emprestimo["nome_do_livro"])
    return emprestimos

def deletarEmprestimo():
    nome = input("nome do livro que quer deletar o empréstimo: ")
    emprestimosAntes = verEmprestimo(nome)
    lend.delete_one({ "nome_do_livro": nome })
    emprestimos = verEmprestimo(nome)
    if nome not in emprestimos and nome in emprestimosAntes:
        return True
    else:
        return False
    