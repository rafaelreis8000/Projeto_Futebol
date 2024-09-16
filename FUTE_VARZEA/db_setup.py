import sqlite3

def criar_banco_dados():
    conn = sqlite3.connect("futebol.db")
    cursor = conn.cursor()

    # Criando a tabela times
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS times (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cor_principal TEXT,
            cor_secundaria TEXT,
            escudo TEXT
        )
    ''')

    # Criando a tabela jogadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            posicao TEXT,
            time_id INTEGER,
            FOREIGN KEY (time_id) REFERENCES times(id)
        )
    ''')

    # Criação de mais tabelas (campeonatos, comissões, etc.) aqui

    conn.commit()
    conn.close()

# Rodar este arquivo para criar o banco de dados
if __name__ == "__main__":
    criar_banco_dados()
