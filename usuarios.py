from db import get_database

client = get_database()

db = client["top"]
users = db.usuarios

def cadastrarUsuario():
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    autorPreferido = input("Digite o autor preferido: ")
    matricula = input("Digite a matricula do usuário: ")
    curso = input("Digite o curso do usuário: ")

    if (not nome or not idade or not autorPreferido or not matricula or not curso):
        print("Digite as informações corretamente")
        return
    elif (int(idade) < 0 or int(idade) > 100):
        print("Digite a idade corretamente")
        return
    elif (len(matricula) < 8):
        print("Digite a matricula corretamente")
        return

    data = {
        "nome": nome,
        "idade": idade,
        "autorPreferido": autorPreferido,
        "matricula": matricula,
        "curso": curso
    }

    insertedUser = users.insert_one(data)
    return insertedUser.inserted_id

def verUsuarios():
    return users.find()

def buscarUsuario(matricula):
    return users.find_one({"matricula": matricula})

def verUsuario(matricula):
    usuarios = []
    for usuario in users.find():
        usuarios.append(usuario["matricula"])
    return usuarios

def deletarUsuario():
    matricula = input("matricula do usuário que quer deletar: ")
    usuariosAntes = verUsuario(matricula)
    users.delete_one({ "matricula": matricula })
    usuarios = verUsuario(matricula)
    if matricula not in usuarios and matricula in usuariosAntes:
        return True
    else:
        return False

def atualizarUsuario():
    opcoes = ("nome", "idade", "autorPreferido", "curso")
    matricula = input("Digite a matricula que quer atualizar: ")
    if matricula not in verUsuario(matricula):
        print("Esse usuário não existe.")
        return 1
    opcao = int(input("0 - nome\n1 - idade\n2 - Autor preferido\n3 - curso\nDigite: "))
    if opcao not in [0,1,2,3]:
        return
    info = input(f"Digite o/a novo {opcoes[opcao]}: ")
    
    users.update_one({"matricula": matricula}, {
        "$set": { str(opcoes[opcao]): info}
    })
    return 0