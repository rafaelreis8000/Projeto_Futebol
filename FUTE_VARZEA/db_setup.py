import sqlite3
import logging
import os

def criar_banco_dados(nome_banco="futebol.db"):
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()

        # Cria a tabela de times
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS times (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cor_principal TEXT,
                cor_secundaria TEXT,
                escudo TEXT
            )
        ''')

        # Cria a tabela de jogadores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jogadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                posicao TEXT,
                time_id INTEGER,
                FOREIGN KEY (time_id) REFERENCES times(id)
            )
        ''')

        # Confirma as alterações no banco de dados
        conn.commit()
        logging.info("Banco de dados criado com sucesso!")

    # Captura e registra qualquer erro que possa ocorrer durante a criação do banco de dados
    except sqlite3.Error as error:
        logging.error(f"Erro ao criar o banco de dados {nome_banco}: {error}")

    # Fecha a conexão com o banco de dados, mesmo que ocorra um erro
    finally:
        if conn:
            conn.close()

def banco_existe(nome_banco="futebol.db"):
    """
    Verifica se o arquivo do banco de dados já existe no sistema de arquivos
        bool: Retorna True se o arquivo existir, False caso contrário.
    """
    return os.path.exists(nome_banco)

def main():
    if not banco_existe():
        criar_banco_dados()
    else:
        print("O banco de dados já existe.")

if __name__ == "__main__":
    main()