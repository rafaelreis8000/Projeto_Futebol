criar venv
    python -m venv venv
    venv/Scripts/activate

instalar dependências do projeto
    pip install -r requirements.txt

#######################
ESTRUTURA DA APLICAÇÃO
#######################
Proj_Futebol/
│
├── main.py                # Arquivo principal para rodar o aplicativo
├── app/
│   ├── __init__.py         # Arquivo vazio para tornar 'app' um pacote Python
│   ├── banco_dados.py      # Novo arquivo para o código do banco de dados
│   ├── home.py
│   ├── integrantes.py
│   ├── times.py
│   └── pages/
│       ├── cadastrar_jogador.py
│       └── cadastrar_torcedor.py
