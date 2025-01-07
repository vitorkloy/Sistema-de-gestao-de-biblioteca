import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from livros import cadastrarLivro, verLivros, deletarLivro, atualizarLivro
from usuarios import cadastrarUsuario, verUsuarios, deletarUsuario, atualizarUsuario
from emprestimos import cadastrarEmprestimo, deletarEmprestimo

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Biblioteca")
        # Define o tamanho da janela
        self.root.geometry("400x600")
        
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        self.create_main_buttons()

    def create_main_buttons(self):
        self.clear_frame()
        
        buttons = {
            "Cadastrar Livro": self.cadastrar_livro,
            "Cadastrar Usuário": self.cadastrar_usuario,
            "Consultar Livros": self.consultar_livros,
            "Consultar Usuários": self.consultar_usuarios,
            "Emprestar Livro": self.emprestar_livro,
            "Deletar Livro": self.deletar_livro,
            "Deletar Usuário": self.deletar_usuario,
            "Atualizar Livro": self.atualizar_livro,
            "Atualizar Usuário": self.atualizar_usuario
        }
        
        for idx, (texto, comando) in enumerate(buttons.items()):
            btn = ttk.Button(self.frame_principal, text=texto, command=comando, width=25)
            btn.grid(row=idx, column=0, padx=10, pady=10, sticky=tk.W)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    
    def clear_frame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def cadastrar_livro(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Cadastrar Livro").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Nome").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        nome = tk.Entry(self.frame_principal, width=40)  # Ajuste a largura
        nome.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Autor").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        autor = tk.Entry(self.frame_principal, width=40)
        autor.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Preço").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        preco = tk.Entry(self.frame_principal, width=40)
        preco.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Categoria").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        categoria = tk.Entry(self.frame_principal, width=40)
        categoria.grid(row=4, column=1, padx=5, pady=5)
        
        def salvar_livro():
            id = cadastrarLivro(nome.get(), autor.get(), preco.get(), categoria.get())
            if id:
                self.show_message("Sucesso", f"Livro cadastrado com sucesso com id: {id}")
            else:
                self.show_message("Erro", "Não foi possível cadastrar o livro.")
        
        tk.Button(self.frame_principal, text="Salvar", command=salvar_livro).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=6, column=0, columnspan=2, pady=10)

    def cadastrar_usuario(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Cadastrar Usuário").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Nome").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        nome = tk.Entry(self.frame_principal, width=40)
        nome.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Idade").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        idade = tk.Entry(self.frame_principal, width=40)
        idade.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Autor Preferido").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        autor_preferido = tk.Entry(self.frame_principal, width=40)
        autor_preferido.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Matrícula").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        matricula = tk.Entry(self.frame_principal, width=40)
        matricula.grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Curso").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        curso = tk.Entry(self.frame_principal, width=40)
        curso.grid(row=5, column=1, padx=5, pady=5)
        
        def salvar_usuario():
            id = cadastrarUsuario(nome.get(), idade.get(), autor_preferido.get(), matricula.get(), curso.get())
            if id:
                self.show_message("Sucesso", f"Usuário cadastrado com sucesso com id: {id}")
            else:
                self.show_message("Erro", "Não foi possível cadastrar o usuário.")
        
        tk.Button(self.frame_principal, text="Salvar", command=salvar_usuario).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=7, column=0, columnspan=2, pady=10)
    
    def consultar_livros(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Consultar Livros").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        # Recupera a lista de livros
        livros = verLivros()
        
        if not livros:
            tk.Label(self.frame_principal, text="Nenhum livro encontrado.").grid(row=1, column=0, columnspan=2, pady=10)
            tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=2, column=0, columnspan=2, pady=10)
            return

        # Exibe os livros
        for idx, livro in enumerate(livros):
            row = idx * 6 + 1
            tk.Label(self.frame_principal, text=f"Nome: {livro.get('nome', 'N/A')}").grid(row=row, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Autor: {livro.get('autor', 'N/A')}").grid(row=row + 1, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Preço: {livro.get('preço', 'N/A')}").grid(row=row + 2, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Categoria: {livro.get('categoria', 'N/A')}").grid(row=row + 3, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text="-------------------------").grid(row=row + 4, column=0, columnspan=2, pady=5)
        
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=row + 5, column=0, columnspan=2, pady=10)

    def consultar_usuarios(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Consultar Usuários").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        usuarios = verUsuarios()
        for idx, usuario in enumerate(usuarios):
            row = idx + 1
            tk.Label(self.frame_principal, text=f"Nome: {usuario.get('nome', 'N/A')}").grid(row=row, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Idade: {usuario.get('idade', 'N/A')}").grid(row=row + 1, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Matrícula: {usuario.get('matricula', 'N/A')}").grid(row=row + 2, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Autor Preferido: {usuario.get('autorPreferido', 'N/A')}").grid(row=row + 3, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text=f"Curso: {usuario.get('curso', 'N/A')}").grid(row=row + 4, column=0, columnspan=2, pady=5, sticky=tk.W)
            tk.Label(self.frame_principal, text="-------------------------").grid(row=row + 5, column=0, columnspan=2, pady=5)
        
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=row + 6, column=0, columnspan=2, pady=10)
    
    def emprestar_livro(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Emprestar Livro").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Matrícula").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        matricula = tk.Entry(self.frame_principal, width=40)
        matricula.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Nome do Livro").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        nome_livro = tk.Entry(self.frame_principal, width=40)
        nome_livro.grid(row=2, column=1, padx=5, pady=5)
        
        def emprestar():
            id = cadastrarEmprestimo(matricula.get(), nome_livro.get())
            if id:
                self.show_message("Sucesso", "Empréstimo realizado com sucesso.")
            else:
                self.show_message("Erro", "Não foi possível realizar o empréstimo.")
        
        tk.Button(self.frame_principal, text="Emprestar", command=emprestar).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=4, column=0, columnspan=2, pady=10)
    
    def deletar_livro(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Deletar Livro").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Nome do Livro").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        nome_livro = tk.Entry(self.frame_principal, width=40)
        nome_livro.grid(row=1, column=1, padx=5, pady=5)
        
        def deletar():
            deleted = deletarLivro(nome_livro.get())
            if deleted:
                self.show_message("Sucesso", "Livro deletado com sucesso.")
            else:
                self.show_message("Erro", "Não foi possível deletar o livro.")
        
        tk.Button(self.frame_principal, text="Deletar", command=deletar).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=3, column=0, columnspan=2, pady=10)
    
    def deletar_usuario(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Deletar Usuário").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Matrícula").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        matricula = tk.Entry(self.frame_principal, width=40)
        matricula.grid(row=1, column=1, padx=5, pady=5)
        
        def deletar():
            deleted = deletarUsuario(matricula.get())
            if deleted:
                self.show_message("Sucesso", "Usuário deletado com sucesso.")
            else:
                self.show_message("Erro", "Não foi possível deletar o usuário.")
        
        tk.Button(self.frame_principal, text="Deletar", command=deletar).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=3, column=0, columnspan=2, pady=10)
    
    def atualizar_livro(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Atualizar Livro").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Nome do Livro").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        nome_livro = tk.Entry(self.frame_principal, width=40)
        nome_livro.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Campo a ser Atualizado").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        campo = ttk.Combobox(self.frame_principal, values=["nome", "autor", "preço", "categoria"], width=37)
        campo.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Novo Valor").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        novo_valor = tk.Entry(self.frame_principal, width=40)
        novo_valor.grid(row=3, column=1, padx=5, pady=5)
        
        def atualizar():
            if atualizarLivro(nome_livro.get(), campo.get(), novo_valor.get()) == 0:
                self.show_message("Sucesso", "Livro atualizado com sucesso.")
            else:
                self.show_message("Erro", "Não foi possível atualizar o livro.")
        
        tk.Button(self.frame_principal, text="Atualizar", command=atualizar).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=5, column=0, columnspan=2, pady=10)
    
    def atualizar_usuario(self):
        self.clear_frame()
        
        tk.Label(self.frame_principal, text="Atualizar Usuário").grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        tk.Label(self.frame_principal, text="Matrícula").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        matricula = tk.Entry(self.frame_principal, width=40)
        matricula.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Campo a ser Atualizado").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        campo = ttk.Combobox(self.frame_principal, values=["nome", "idade", "autorPreferido", "curso"], width=37)
        campo.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_principal, text="Novo Valor").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        novo_valor = tk.Entry(self.frame_principal, width=40)
        novo_valor.grid(row=3, column=1, padx=5, pady=5)
        
        def atualizar():
            if atualizarUsuario(matricula.get(), campo.get(), novo_valor.get()) == 0:
                self.show_message("Sucesso", "Usuário atualizado com sucesso.")
            else:
                self.show_message("Erro", "Não foi possível atualizar o usuário.")
        
        tk.Button(self.frame_principal, text="Atualizar", command=atualizar).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.frame_principal, text="Voltar", command=self.create_main_buttons).grid(row=5, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
