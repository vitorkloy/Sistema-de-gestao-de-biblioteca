from db import get_database

client = get_database()

db = client["top"]
books = db.livros

def cadastrarLivro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    valor = input("Digite o valor do livro: ")
    categoria = input("Digite o nome da categoria: ")

    if (not nome or not autor or not valor or not categoria):
        print("Preencha os dados corretamente.")
        return
    elif (float(valor) < 0):
        print("Preencha o valor corretamente.")
        return
    if (verLivroPorNome(nome)):
        if (nome == verLivroPorNome(nome)["nome"]):
            print("Esse livro já existe.")
            return

    data = {
        "nome": nome,
        "autor": autor,
        "preco": valor,
        "categoria": categoria
    }

    insertedBook = books.insert_one(data)
    return insertedBook.inserted_id

def verLivros():
    return books.find()

def verLivroPorNome(nome):
    return books.find_one({"nome": nome})

def verLivro(nome):
    livros = []
    for livro in books.find():
        livros.append(livro["nome"])
    return livros

def deletarLivro():
    nome = input("nome do livro que quer deletar: ")
    livrosAntes = verLivro(nome)
    books.delete_one({ "nome": nome })
    livros = verLivro(nome)
    if nome not in livros and nome in livrosAntes:
        return True
    else:
        return False
    
def atualizarLivro():
    opcoes = ("nome", "autor", "preço", "categoria")
    nome = input("Digite o nome do livro que quer atualizar: ")
    if nome not in verLivro(nome):
        print("Esse livro não existe.")
        return 1
    opcao = int(input("0 - nome\n1 - autor\n2 - preço\n3 - categoria\nDigite: "))
    if opcao not in [0,1,2,3]:
        return
    info = input(f"Digite o/a novo {opcoes[opcao]}: ")
    
    books.update_one({"nome": nome}, {
        "$set": { str(opcoes[opcao]): info}
    })
    return 0