import flet as ft
from livros import cadastrarLivro, verLivros, deletarLivro, atualizarLivro
from usuarios import cadastrarUsuario, verUsuarios, deletarUsuario, atualizarUsuario
from emprestimos import cadastrarEmprestimo, deletarEmprestimo

def main(page: ft.Page):
    page.title = "Sistema de Gerenciamento de Biblioteca"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Ajustar o tamanho da janela principal
    page.window_width = 300
    page.window_height = 600
    
    def update_main_content(content):
        page.controls.clear()
        page.controls.append(content)
        page.update()

    def create_main_buttons():
        buttons = [
            ft.ElevatedButton(text="Cadastrar Livro", on_click=lambda e: show_cadastrar_livro()),
            ft.ElevatedButton(text="Cadastrar Usuário", on_click=lambda e: show_cadastrar_usuario()),
            ft.ElevatedButton(text="Consultar Livros", on_click=lambda e: show_consultar_livros()),
            ft.ElevatedButton(text="Consultar Usuários", on_click=lambda e: show_consultar_usuarios()),
            ft.ElevatedButton(text="Emprestar Livro", on_click=lambda e: show_emprestar_livro()),
            ft.ElevatedButton(text="Deletar Livro", on_click=lambda e: show_deletar_livro()),
            ft.ElevatedButton(text="Deletar Usuário", on_click=lambda e: show_deletar_usuario()),
            ft.ElevatedButton(text="Atualizar Livro", on_click=lambda e: show_atualizar_livro()),
            ft.ElevatedButton(text="Atualizar Usuário", on_click=lambda e: show_atualizar_usuario())
        ]
        page.controls.clear()
        page.controls.append(ft.Column(controls=buttons, spacing=10, alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def show_message(title, message):
        page.dialog = ft.AlertDialog(
            title=ft.Text(title),
            content=ft.Text(message),
            actions=[
                ft.ElevatedButton(text="OK", on_click=lambda e: page.dialog.close())
            ]
        )
        page.dialog.open = True
        page.update()

    def show_cadastrar_livro():
        def salvar_livro(e):
            id = cadastrarLivro(nome.value, autor.value, preco.value, categoria.value)
            if id:
                show_message("Sucesso", f"Livro cadastrado com sucesso com id: {id}")
            else:
                show_message("Erro", "Não foi possível cadastrar o livro.")
        
        nome = ft.TextField(label="Nome", width=250)
        autor = ft.TextField(label="Autor", width=250)
        preco = ft.TextField(label="Preço", width=250)
        categoria = ft.TextField(label="Categoria", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Cadastrar Livro", size=20, weight=ft.FontWeight.BOLD),
                    nome,
                    autor,
                    preco,
                    categoria,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Salvar", on_click=salvar_livro),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    def show_cadastrar_usuario():
        def salvar_usuario(e):
            id = cadastrarUsuario(nome.value, idade.value, autor_preferido.value, matricula.value, curso.value)
            if id:
                show_message("Sucesso", f"Usuário cadastrado com sucesso com id: {id}")
            else:
                show_message("Erro", "Não foi possível cadastrar o usuário.")
        
        nome = ft.TextField(label="Nome", width=250)
        idade = ft.TextField(label="Idade", width=250)
        autor_preferido = ft.TextField(label="Autor Preferido", width=250)
        matricula = ft.TextField(label="Matrícula", width=250)
        curso = ft.TextField(label="Curso", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Cadastrar Usuário", size=20, weight=ft.FontWeight.BOLD),
                    nome,
                    idade,
                    autor_preferido,
                    matricula,
                    curso,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Salvar", on_click=salvar_usuario),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    def show_consultar_livros():
        livros = verLivros()
        if not livros:
            page.controls.clear()
            page.controls.append(
                ft.Column(
                    controls=[
                        ft.Text("Nenhum livro encontrado."),
                        ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                    ],
                    spacing=10
                )
            )
            page.update()
            return

        controls = [ft.Text("Consultar Livros", size=20, weight=ft.FontWeight.BOLD)]
        for livro in livros:
            controls.extend([
                ft.Text(f"Nome: {livro.get('nome', 'N/A')}"),
                ft.Text(f"Autor: {livro.get('autor', 'N/A')}"),
                ft.Text(f"Preço: {livro.get('preço', 'N/A')}"),
                ft.Text(f"Categoria: {livro.get('categoria', 'N/A')}"),
                ft.Text("-------------------------")
            ])

        controls.append(ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons()))
        page.controls.clear()
        page.controls.append(ft.Column(controls=controls, spacing=10))
        page.update()

    def show_consultar_usuarios():
        usuarios = verUsuarios()
        controls = [ft.Text("Consultar Usuários", size=20, weight=ft.FontWeight.BOLD)]
        for usuario in usuarios:
            controls.extend([
                ft.Text(f"Nome: {usuario.get('nome', 'N/A')}"),
                ft.Text(f"Idade: {usuario.get('idade', 'N/A')}"),
                ft.Text(f"Matrícula: {usuario.get('matricula', 'N/A')}"),
                ft.Text(f"Autor Preferido: {usuario.get('autorPreferido', 'N/A')}"),
                ft.Text(f"Curso: {usuario.get('curso', 'N/A')}"),
                ft.Text("-------------------------")
            ])
        
        controls.append(ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons()))
        page.controls.clear()
        page.controls.append(ft.Column(controls=controls, spacing=10))
        page.update()

    def show_emprestar_livro():
        def emprestar(e):
            id = cadastrarEmprestimo(matricula.value, nome_livro.value)
            if id:
                show_message("Sucesso", "Empréstimo realizado com sucesso.")
            else:
                show_message("Erro", "Não foi possível realizar o empréstimo.")
        
        matricula = ft.TextField(label="Matrícula", width=250)
        nome_livro = ft.TextField(label="Nome do Livro", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Emprestar Livro", size=20, weight=ft.FontWeight.BOLD),
                    matricula,
                    nome_livro,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Emprestar", on_click=emprestar),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    def show_deletar_livro():
        def deletar(e):
            deleted = deletarLivro(nome_livro.value)
            if deleted:
                show_message("Sucesso", "Livro deletado com sucesso.")
            else:
                show_message("Erro", "Não foi possível deletar o livro.")
        
        nome_livro = ft.TextField(label="Nome do Livro", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Deletar Livro", size=20, weight=ft.FontWeight.BOLD),
                    nome_livro,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Deletar", on_click=deletar),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    def show_deletar_usuario():
        def deletar(e):
            deleted = deletarUsuario(matricula.value)
            if deleted:
                show_message("Sucesso", "Usuário deletado com sucesso.")
            else:
                show_message("Erro", "Não foi possível deletar o usuário.")
        
        matricula = ft.TextField(label="Matrícula", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Deletar Usuário", size=20, weight=ft.FontWeight.BOLD),
                    matricula,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Deletar", on_click=deletar),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    def show_atualizar_livro():
        def atualizar(e):
            updated = atualizarLivro(nome.value, autor.value, preco.value, categoria.value)
            if updated:
                show_message("Sucesso", "Livro atualizado com sucesso.")
            else:
                show_message("Erro", "Não foi possível atualizar o livro.")
        
        nome = ft.TextField(label="Nome do Livro", width=250)
        autor = ft.TextField(label="Autor", width=250)
        preco = ft.TextField(label="Preço", width=250)
        categoria = ft.TextField(label="Categoria", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Atualizar Livro", size=20, weight=ft.FontWeight.BOLD),
                    nome,
                    autor,
                    preco,
                    categoria,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Atualizar", on_click=atualizar),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    def show_atualizar_usuario():
        def atualizar(e):
            updated = atualizarUsuario(nome.value, idade.value, autor_preferido.value, matricula.value, curso.value)
            if updated:
                show_message("Sucesso", "Usuário atualizado com sucesso.")
            else:
                show_message("Erro", "Não foi possível atualizar o usuário.")
        
        nome = ft.TextField(label="Nome", width=250)
        idade = ft.TextField(label="Idade", width=250)
        autor_preferido = ft.TextField(label="Autor Preferido", width=250)
        matricula = ft.TextField(label="Matrícula", width=250)
        curso = ft.TextField(label="Curso", width=250)
        
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Atualizar Usuário", size=20, weight=ft.FontWeight.BOLD),
                    nome,
                    idade,
                    autor_preferido,
                    matricula,
                    curso,
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Atualizar", on_click=atualizar),
                            ft.ElevatedButton(text="Voltar", on_click=lambda e: create_main_buttons())
                        ]
                    )
                ],
                spacing=10
            )
        )
        page.update()

    create_main_buttons()

ft.app(target=main)
