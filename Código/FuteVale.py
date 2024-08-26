import flet as ft

def main(page: ft.Page):                    #define uma página/ tela principal
    page.title = 'FuteVale'

    page.window_width = 500
    page.bgcolor = '#214E34'                #configura o tamanho e as cores da tela

    txt_titulo = ft.Text('Nome do Time: ')
    NomeTime = ft.TextField(label='Digite o nome do time: ')
    
    btn_incluir = ft.ElevatedButton('Cadastrar')


    page.add(                               #adiciona os elementos do sistema na tela
            txt_titulo,
            NomeTime,
            btn_incluir
        )

ft.app(target=main)