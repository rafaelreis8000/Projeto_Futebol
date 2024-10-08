import flet as ft

def Home(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('Página Inicial', size=40),
                ft.ElevatedButton("Times", on_click=lambda _: page.go('/times')),
                ft.ElevatedButton("Integrantes", on_click=lambda _: page.go('/integrantes')),
            ]
        )
    )