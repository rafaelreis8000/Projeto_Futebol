import flet as ft

def Integrantes(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('Integrante', size=40),
                ft.ElevatedButton("Cadastrar Pessoa", on_click=lambda _: page.go('/cadastrar_pessoa')),
                # ft.ElevatedButton("Cadastrar Torcedor"),
                ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go('/')),
            ]
        )
    )