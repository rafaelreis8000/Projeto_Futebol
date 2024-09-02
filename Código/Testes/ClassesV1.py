class Pessoa:
    def __init__(self, nome, nascimento, sexo):
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo

class Clube:
    def __init__(self, nome):
        self.nome = nome
        self.elenco = Elenco()  # Inicializando um objeto do tipo Elenco

class Elenco:
    def __init__(self):
        self.jogadores = [] # Lista para armazenar objetos do tipo Jogador
        self.comissao = []  # Lista para armazenar objetos do tipo Comissao

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

class Jogador(Pessoa):
    def __init__(self, nome, nascimento, sexo, altura, peso, posicao, lateralidade):
        super().__init__(nome, nascimento, sexo)
        self.altura = altura
        self.peso = peso
        self.posicao = posicao
        self.lateralidade = lateralidade

class Comissao(Pessoa):
    def __init__(self, nome, nascimento, sexo, cargo):
        super().__init__(nome, nascimento, sexo)
        self.cargo = cargo
