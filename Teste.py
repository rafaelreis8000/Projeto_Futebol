import flet as ft

def main(page: ft.Page):
    titulo = ft.Text(value = "FuteVale Manager", size = 30)
    page.title = "FuteVale Manager"
    page.window_width = 500
    page.controls.append(titulo) #append adiciona

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Insira um nome por favor"
            page.update()
        if not entrada_nome.value:
            entrada_senha.error_text = "insira uma senha por favor"
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")
            
            page.clean()
            page.add(ft.Text(f"Olá, {nome}\nSeja bem-vindo!"))
            pass

    entrada_nome = ft.TextField(label = "Insira seu nome")
    entrada_senha = ft.TextField(label = "Insira sua senha")

    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("LOGIN", on_click= login)
    )

    pass


ft.app(target= main)
