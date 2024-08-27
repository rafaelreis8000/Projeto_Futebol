import re
import flet as ft

def main(page: ft.Page):

    # Define o nome da aba, tamanho da tela e cor de fundo
    page.title = "FuteVale - Manager"
    page.window_width = 500
    page.bgcolor = '#214E34'

    # Cria uma lista vazia
    lista_clubes = []

    # Checa se o nome do clube é válido
    def validar_nome(nome):
        # Expressão que verifica a validade do nome
        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"
        if not nome:
            return "O nome do clube não pode ser nulo."
        if not re.match(pattern, nome):
            return "O nome do clube não pode conter números ou caracteres especiais."
        return None

    # Função para adicionar itens à lista
    def adicionar_item(e):
        nome_clube = user_input.value.strip()
        mensagem_erro = validar_nome(nome_clube)

        if mensagem_erro:
            # Exibe a mensagem de erro
            txt_erro.value = mensagem_erro
            page.update()
        else:
            # Exibe o botão de confirmação se a validação for bem-sucedida
            txt_erro.value = ""
            btn_confirmar.visible = True
            page.update()

    # Função para confirmar a adição do clube à lista
    def confirmar_adicao(e):
        nome_clube = user_input.value.strip()
        novo_item = ft.Text(value=nome_clube)
        lista_clubes.append(novo_item)
        lista_column.controls.append(novo_item)
        user_input.value = ""
        btn_confirmar.visible = False
        page.update()

    # Entrada de texto pelo usuário
    user_input = ft.TextField(hint_text="Nome do Clube")

    # Botão para adicionar (validação)
    btn_add = ft.ElevatedButton(text="Adicionar", on_click=adicionar_item)

    # Componente de texto para exibir mensagens de erro
    txt_erro = ft.Text(value="", color="red")

    # Botão de confirmação para adicionar o clube à lista
    btn_confirmar = ft.ElevatedButton(
        text="Confirmar",
        on_click=confirmar_adicao,
        visible=False,  # Inicialmente invisível
        bgcolor="green"
    )

    # Lista (Column) onde os itens serão exibidos
    lista_column = ft.Column()

    # Adicionando os componentes na página
    page.add(user_input, btn_add, txt_erro, btn_confirmar, lista_column)

# Inicializando a aplicação
ft.app(target=main)
