import flet as ft

def Times(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('Times', size=40),
                ft.ElevatedButton("Cadastrar time", on_click=lambda _: page.go('/cadastrar_time')),
                ft.ElevatedButton(text="Voltar", on_click=lambda e: page.go('/')),
            ]
        )
    )