class Pessoa:
    def __init__(self, nome, sobrenome, idade, nascimento, sexo, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.nascimento = nascimento
        self.sexo = sexo
        self.cargo = cargo

class Jogador(Pessoa):
    def __init__(self, nome, sobrenome, idade, nascimento, sexo, altura, peso, posicao, lateralidade):
        super().__init__(nome, sobrenome, idade, nascimento, sexo)
        self.altura = altura
        self.peso = peso
        self.posicao = posicao
        self.lateralidade = lateralidade

class Cargo(Pessoa):
    def __init__(self, nome, sobrenome, idade, nascimento, sexo, cargo):
        super().__init__(nome, sobrenome, idade, nascimento, sexo, cargo)