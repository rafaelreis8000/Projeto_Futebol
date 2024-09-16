import flet as ft

def criar_campeonato(page: ft.Page):
    def submit_campeonato(e):
        nome_campeonato = input_nome.value

        if nome_campeonato:
            # Logica para criar o campeonato
            page.snack_bar = ft.SnackBar(ft.Text(f"Campeonato '{nome_campeonato}' criado com sucesso!"))
            page.snack_bar.open = True
            limpar_campos()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha o nome do campeonato!"))
            page.snack_bar.open = True
        page.update()

    def limpar_campos():
        input_nome.value = ""
        page.update()

    input_nome = ft.TextField(label="Nome do Campeonato")
    submit_button = ft.ElevatedButton("Criar", on_click=submit_campeonato)

    page.add(input_nome, submit_button)
    page.update()
