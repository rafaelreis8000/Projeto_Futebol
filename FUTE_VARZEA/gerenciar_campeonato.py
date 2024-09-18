import sqlite3
import random
import flet as ft

def criar_campeonato(page: ft.Page, main_menu_callback):
    def sortear_times(e):
        # Conecta ao banco de dados
        conn = sqlite3.connect("futebol.db")
        cursor = conn.cursor()

        # Seleciona todos os times cadastrados
        cursor.execute("SELECT id, nome FROM times")
        times = cursor.fetchall()

        # Verifica se há pelo menos 4 times
        if len(times) < 4:
            page.snack_bar = ft.SnackBar(ft.Text("É necessário no mínimo 4 times para criar um campeonato."))
            page.snack_bar.open = True
            page.update()
            return

        # Sorteia os times participantes
        num_times = min(8, len(times))  # Define um máximo de 8 times para o campeonato
        times_sorteados = random.sample(times, num_times)

        # Cria os jogos do campeonato (todos contra todos)
        jogos = []
        for i in range(len(times_sorteados)):
            for j in range(i + 1, len(times_sorteados)):
                time1 = times_sorteados[i]
                time2 = times_sorteados[j]
                jogos.append((time1[0], time2[0]))  # Armazena o ID dos times para os jogos

        # Armazena os jogos no banco de dados
        cursor.execute("DELETE FROM jogos")  # Remove jogos antigos
        for jogo in jogos:
            cursor.execute("INSERT INTO jogos (time1_id, time2_id, resultado) VALUES (?, ?, ?)", (jogo[0], jogo[1], ""))
        conn.commit()
        conn.close()

        page.snack_bar = ft.SnackBar(ft.Text(f"Campeonato criado com {num_times} times!"))
        page.snack_bar.open = True
        page.update()

    def voltar_menu(e):
        main_menu_callback()

    # Layout da página
    sortear_button = ft.ElevatedButton("Sortear Times e Criar Campeonato", on_click=sortear_times)
    voltar_button = ft.ElevatedButton("Voltar", on_click=voltar_menu, bgcolor=ft.colors.GREY_300)

    page.add(sortear_button, voltar_button)
    page.update()

