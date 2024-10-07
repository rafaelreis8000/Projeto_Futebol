import sqlite3
import logging

# ... (restante do código que você já tem)

def listar_times():
    """Lista todos os times cadastrados no banco de dados."""
    try:
        conn = sqlite3.connect('futebol.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM times")
        times = cursor.fetchall()

        for time in times:
            print(f"ID: {time[0]}, Nome: {time[1]}, Cor principal: {time[2]}, Cor secundária: {time[3]}, Escudo: {time[4]}")

        conn.close()
    except sqlite3.Error as error:
        logging.error(f"Erro ao listar os times: {error}")

def listar_jogadores():
    """Lista todos os jogadores cadastrados no banco de dados."""
    try:
        conn = sqlite3.connect('futebol.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM jogadores")
        jogadores = cursor.fetchall()

        for jogador in jogadores:
            print(f"ID: {jogador[0]}, Nome: {jogador[1]}, Posição: {jogador[2]}, Time: {jogador[3]}")

        conn.close()
    except sqlite3.Error as error:
        logging.error(f"Erro ao listar os jogadores: {error}")

# Chamar as funções para listar os times e jogadores
listar_times()
listar_jogadores()