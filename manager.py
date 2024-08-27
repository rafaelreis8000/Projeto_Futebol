import re
import flet as ft

def main(page: ft.Page):

    #define o nome da aba, tamanho da tela e cor
    page.title = "FuteVale - Manager"
    page.window_width = 500
    page.bgcolor = '#214E34'

    # Cria uma lista vazia
    lista_clubes = []
    
    # Adiciona itens à lista
    def adicionar_item(e):
        novo_item = ft.Text(value=user_input.value)
        lista_clubes.append(novo_item)
        lista_column.controls.append(novo_item)
        user_input.value = ""
        page.update()

    # Entrada de texto pelo usuário
    user_input = ft.TextField(hint_text="Nome do Clube")

    # Botão de adicionar
    btn_add = ft.ElevatedButton(text="Adicionar", on_click=adicionar_item)

    # Lista (Column) onde os itens serão exibidos
    lista_column = ft.Column()

    # Adicionando os componentes na página
    page.add(user_input, btn_add, lista_column)

# Inicializando a aplicação
ft.app(target=main)