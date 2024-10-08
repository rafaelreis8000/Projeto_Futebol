import flet as ft
from app.home import Home
from app.times import Times
from app.integrantes import Integrantes
from app.pages.cadastrar_pessoa import cadastrar_pessoa
from app.pages.cadastrar_time import cadastrar_time

def register_routes(page: ft.Page):
    def route_change(route):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[Home(page)]))
        
        elif page.route == "/times":
            page.views.append(ft.View(route="/times", controls=[Times(page)]))
        
        elif page.route == "/integrantes":
            page.views.append(ft.View(route="/integrantes", controls=[Integrantes(page)]))
        
        elif page.route == "/cadastrar_pessoa":
            page.views.append(ft.View(route="/cadastrar_pessoa", controls=[cadastrar_pessoa(page)]))

        elif page.route == "/cadastrar_time":
            page.views.append(ft.View(route="/cadastrar_time", controls=[cadastrar_time(page)]))
        
        page.update()

    # Associa a função de mudança de rota à página
    page.on_route_change = route_change
