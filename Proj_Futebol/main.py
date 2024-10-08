import flet as ft
from app.routes import register_routes  # Importa a função que registra as rotas
from app.banco_dados import inicializar_banco #Importa a função que inicia o banco

def main(page: ft.Page):
    # Chama a função que registra todas as rotas
    register_routes(page)
    inicializar_banco()
    
    page.go("/")  # Redireciona para a página inicial
    page.update()

if __name__ == "__main__":
    ft.app(target=main)