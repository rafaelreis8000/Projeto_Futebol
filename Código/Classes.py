class Pessoa:
    def __init__(self, nome, nascimento, sexo):
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo

class Clube:
    def __init__(self, nome):
        self.nome = nome
        self.elenco = Elenco

class Elenco:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = Jogador

class Jogador(Pessoa):
    def __init__(self, nome, nascimento, sexo, altura, peso, lateralidade):
        super().__init__(nome, nascimento, sexo)
        self.altura = altura
        self.peso = peso
        self.lateralidade = lateralidade
