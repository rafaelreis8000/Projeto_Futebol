import flet as ft
from cadastro_times import cadastrar_time
from cadastro_jogadores import cadastrar_jogador
from gerenciar_campeonato import criar_campeonato
# Importe outros arquivos conforme necessário

def main(page: ft.Page):

    # Função que recria o menu principal
    def main_menu():
        page.clean()  # Limpa a tela
        page.add(
            ft.Text("Menu Principal"),
            ft.ElevatedButton("Cadastrar Time", on_click=navegar_para_cadastro_time),
            ft.ElevatedButton("Cadastrar Jogador", on_click=navegar_para_cadastro_jogador),
            ft.ElevatedButton("Gerenciar Campeonato", on_click=gerenciar_campeonato)
            # Adicione mais botões conforme necessário
        )
        page.update()

    # Função para navegar para o cadastro de times
    def navegar_para_cadastro_time(e):
        page.clean()  # Limpa a tela
        cadastrar_time(page, main_menu)  # Passa a função main_menu como callback

    # Função para navegar para o cadastro de jogadores
    def navegar_para_cadastro_jogador(e):
        page.clean()  # Limpa a tela
        cadastrar_jogador(page, main_menu)  # Passa a função main_menu como callback

    # Função para navegar para o gerenciamento do campeonato
    def gerenciar_campeonato(e):
        page.clean() # Limpa a tela
        cadastrar_jogador(page, main_menu) # Passa a função main_menu como callback

    # Inicializa o menu principal
    main_menu()

# Executa o aplicativo
ft.app(target=main)
