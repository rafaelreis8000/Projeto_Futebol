import sqlite3
import os

def criar_banco_dados(nome_banco="futebol.db"):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    # Criação da tabela times
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS times (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cor_principal TEXT,
            cor_secundaria TEXT,
            escudo TEXT,
            abreviacao TEXT
        )
    ''')

    # Criação da tabela de pessoas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            cargo TEXT NOT NULL  -- 'jogador', 'torcedor', 'tecnico', 'ajudante'
        );
    ''')

    # Criação da tabela de jogadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pessoa_id INTEGER NOT NULL,  -- Referência à tabela pessoas
            altura REAL,
            peso REAL,
            posicao TEXT,
            time TEXT NOT NULL,
            FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
            ON DELETE CASCADE  -- Se a pessoa for excluída, os jogadores também serão
        );
    ''')

    # Criação da tabela de torcedores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS torcedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pessoa_id INTEGER NOT NULL,  -- Referência à tabela pessoas
            time_favorito TEXT NOT NULL,
            FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
            ON DELETE CASCADE  -- Se a pessoa for excluída, os torcedores também serão
         );
    ''')
    
    # Criação da tabela de técnicos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tecnicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pessoa_id INTEGER NOT NULL,  -- Referência à tabela pessoas
            experiencia INTEGER,  -- Anos de experiência
            time_atual TEXT NOT NULL,
            FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
            ON DELETE CASCADE  -- Se a pessoa for excluída, os técnicos também serão
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ajudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pessoa_id INTEGER NOT NULL,  -- Referência à tabela pessoas
            time_atual TEXT NOT NULL,
            funcao TEXT NOT NULL,  -- O que o ajudante faz
            FOREIGN KEY (pessoa_id) REFERENCES pessoas(id)
            ON DELETE CASCADE -- Se a pessoa for excluída, os ajudantes também serão
        );
    ''')

    conn.commit()
    conn.close()

def inicializar_banco():
    if not os.path.exists("futebol.db"):
        criar_banco_dados()
        print("Banco de dados criado com sucesso!")
    else:
        print("O banco de dados já existe.")
