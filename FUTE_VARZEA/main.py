import flet as ft
from cadastro_times import cadastrar_time
from cadastro_jogadores import cadastrar_jogador
from gerenciar_campeonato import criar_campeonato

def main(page: ft.Page):
    page.title = "Gestão de Futebol - Menu Principal"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def voltar_ao_menu(e):
        # Remove a tela atual e volta para a tela principal
        page.views.pop()
        page.update()

    def navegar_para_cadastro_time(e):
        page.views.append(ft.View(
            "/cadastrar_time",
            [
                ft.AppBar(
                    title=ft.Text("Cadastrar Time"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    leading=ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=voltar_ao_menu
                    )
                ),
                cadastrar_time(page)  # Função que cria o layout de cadastro de time
            ]
        ))
        page.update()

    def navegar_para_cadastro_jogador(e):
        page.views.append(ft.View(
            "/cadastrar_jogador",
            [
                ft.AppBar(
                    title=ft.Text("Cadastrar Jogador"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    leading=ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=voltar_ao_menu
                    )
                ),
                cadastrar_jogador(page)  # Função que cria o layout de cadastro de jogador
            ]
        ))
        page.update()

    def navegar_para_campeonato(e):
        page.views.append(ft.View(
            "/criar_campeonato",
            [
                ft.AppBar(
                    title=ft.Text("Criar Campeonato"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    leading=ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=voltar_ao_menu
                    )
                ),
                criar_campeonato(page)  # Função que cria o layout para criar um campeonato
            ]
        ))
        page.update()

    # Layout do menu principal
    page.add(ft.Text("Bem-vindo ao sistema de Gestão de Futebol!", size=20, weight=ft.FontWeight.BOLD))
    
    cadastrar_button = ft.ElevatedButton("Cadastrar Time", on_click=navegar_para_cadastro_time)
    cadastrar_jogador_button = ft.ElevatedButton("Cadastrar Jogador", on_click=navegar_para_cadastro_jogador)
    criar_campeonato_button = ft.ElevatedButton("Criar Campeonato", on_click=navegar_para_campeonato)

    # Adiciona os botões ao layout
    page.add(cadastrar_button, cadastrar_jogador_button, criar_campeonato_button)

    # Inicializa a página principal
    page.go("/")

# Inicializa a aplicação
ft.app(target=main)
