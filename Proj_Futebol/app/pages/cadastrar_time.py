import sqlite3
import flet as ft
import re

def cadastrar_time(page: ft.Page):
    page.clean()

    # Função para validar URLs
    def validar_url(url):
        url_pattern = re.compile(r'^(https?://)?(www\.)?([a-zA-Z0-9_-]+(\.[a-zA-Z]{2,})+)(/[^ ]*)?$')
        return url_pattern.match(url) is not None

    # Função para submeter os dados do time
    def dados_time(e):
        nome_time = input_nome.value
        cor_principal_time = input_cor_principal.value
        cor_secundaria_time = input_cor_secundaria.value
        escudo_time = input_escudo.value  # URL do escudo
        abreviacao_time = input_abreviacao.value

        if all([nome_time, cor_principal_time, cor_secundaria_time, escudo_time, abreviacao_time]):
            # Validação da URL do escudo
            if not validar_url(escudo_time):
                page.snack_bar = ft.SnackBar(ft.Text("A URL do escudo não é válida!"), open=True)
                page.update()
                return
            
            try:
                with sqlite3.connect("futebol.db") as conn:
                    # Verifica se o time já existe
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM times WHERE nome = ? OR abreviacao = ?", (nome_time, abreviacao_time))
                    existe = cursor.fetchone()[0] > 0
                    
                    if existe:
                        page.snack_bar = ft.SnackBar(ft.Text("Time ou abreviação já cadastrado!"), open=True)
                    else:
                        # Insere o novo time
                        conn.execute(
                            "INSERT INTO times (nome, cor_principal, cor_secundaria, escudo, abreviacao) VALUES (?, ?, ?, ?, ?)",
                            (nome_time, cor_principal_time, cor_secundaria_time, escudo_time, abreviacao_time)
                        )
                        page.snack_bar = ft.SnackBar(ft.Text(f"Time '{nome_time}' cadastrado com sucesso!"), open=True)
                        # Limpa os campos
                        for field in [input_nome, input_cor_principal, input_cor_secundaria, input_escudo, input_abreviacao]:
                            field.value = ""
                            image_preview.visible = False  # Oculta a prévia após o cadastro
            except sqlite3.Error as error:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao cadastrar o time: {error}"), open=True)

        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"), open=True)

        page.update()

    # Função para validar a abreviação (3 caracteres)
    def validar_abreviacao(e):
        if len(input_abreviacao.value) > 3:
            input_abreviacao.value = input_abreviacao.value[:3]  # Limita a 3 caracteres
            page.snack_bar = ft.SnackBar(ft.Text("A abreviação deve ter no máximo 3 caracteres."), open=True)
            page.update()

    # Função para atualizar a prévia da imagem
    def atualizar_previa(e):
        if validar_url(input_escudo.value):
            image_preview.src = input_escudo.value
            image_preview.visible = True
        else:
            image_preview.visible = False
        page.update()

    # Campos de entrada
    input_nome = ft.TextField(label="Nome do Time")
    input_cor_principal = ft.TextField(label="Cor Principal")
    input_cor_secundaria = ft.TextField(label="Cor Secundária")
    input_escudo = ft.TextField(label="URL do Escudo", on_change=atualizar_previa)  # Campo para a URL do escudo
    input_abreviacao = ft.TextField(label="Abreviação (3 letras)", on_change=validar_abreviacao)  # Campo com validação
    image_preview = ft.Image(visible=False, width=100, height=100) # Componente para exibir a prévia da imagem

    # Botões de ação
    cadastro_button = ft.ElevatedButton("Cadastrar", on_click=dados_time)
    voltar_button = ft.ElevatedButton("Voltar", on_click=lambda e: page.go('/'), bgcolor=ft.colors.GREY_300)

    # Monta o layout da página
    return ft.Column(controls=[
        input_nome,
        input_cor_principal,
        input_cor_secundaria,
        input_escudo,
        image_preview,
        input_abreviacao,
        cadastro_button,
        voltar_button
    ])
