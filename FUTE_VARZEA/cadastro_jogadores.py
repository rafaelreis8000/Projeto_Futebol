import sqlite3
import flet as ft

def cadastrar_jogador(page: ft.Page, main_menu_callback):
    # Função para submeter o jogador
    def submit_jogador(e):
        nome_jogador = input_nome.value
        posicao = input_posicao.value
        time_id = int(input_time_id.value)

        if nome_jogador and posicao and time_id:
            conn = sqlite3.connect("futebol.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO jogadores (nome, posicao, time_id) VALUES (?, ?, ?)",
                           (nome_jogador, posicao, time_id))
            conn.commit()
            conn.close()
            page.snack_bar = ft.SnackBar(ft.Text(f"Jogador '{nome_jogador}' cadastrado com sucesso!"))
            page.snack_bar.open = True
            limpar_campos()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
        page.update()

    # Função para limpar os campos
    def limpar_campos():
        input_nome.value = ""
        input_posicao.value = ""
        input_time_id.value = ""
        page.update()

    # Função para voltar ao menu principal
    def voltar_menu(e):
        main_menu_callback()  # Chama a função que recria o menu principal

    # Campos de entrada e botões
    input_nome = ft.TextField(label="Nome do Jogador")
    input_posicao = ft.TextField(label="Posição")
    input_time_id = ft.TextField(label="ID do Time")

    submit_button = ft.ElevatedButton("Cadastrar Jogador", on_click=submit_jogador)
    voltar_button = ft.ElevatedButton("Voltar", on_click=voltar_menu, bgcolor=ft.colors.GREY_300)

    # Adiciona os campos e botões à página
    page.add(input_nome, input_posicao, input_time_id, submit_button, voltar_button)
    page.update()
