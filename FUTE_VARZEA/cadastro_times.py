import sqlite3
import flet as ft

def cadastrar_time(page: ft.Page, main_menu_callback):

    # Limpa a tela
    page.clean()

    # Função para submeter o time
    def submit_time(e):
        nome_time = input_nome.value
        cor_principal_time = input_cor_principal.value
        cor_secundaria_time = input_cor_secundaria.value
        escudo_time = input_escudo.value  # URL ou caminho do escudo

        if nome_time and cor_principal_time and cor_secundaria_time and escudo_time:
            conn = sqlite3.connect("futebol.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO times (nome, cor_principal, cor_secundaria, escudo) VALUES (?, ?, ?, ?)",
                           (nome_time, cor_principal_time, cor_secundaria_time, escudo_time))
            conn.commit()
            conn.close()
            page.snack_bar = ft.SnackBar(ft.Text(f"Time '{nome_time}' cadastrado com sucesso!"))
            page.snack_bar.open = True
            limpar_campos()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
        page.update()

    # Função para limpar os campos
    def limpar_campos():
        input_nome.value = ""
        input_cor_principal.value = ""
        input_cor_secundaria.value = ""
        input_escudo.value = ""
        page.update()

    # Função para voltar ao menu principal
    def voltar_menu(e):
        main_menu_callback()  # Chama a função que recria a tela principal

    # Layout do cadastro
    input_nome = ft.TextField(label="Nome do Time")
    input_cor_principal = ft.TextField(label="Cor Principal")
    input_cor_secundaria = ft.TextField(label="Cor Secundária")
    input_escudo = ft.TextField(label="URL do Escudo")

    # Botões de ação
    submit_button = ft.ElevatedButton("Cadastrar", on_click=submit_time)
    voltar_button = ft.ElevatedButton("Voltar", on_click=voltar_menu, bgcolor=ft.colors.GREY_300)

    # Adiciona os campos e botões à página
    page.add(input_nome, input_cor_principal, input_cor_secundaria, input_escudo, submit_button, voltar_button)
    page.update()
