import re

class Jogador:
    def __init__(self, nome, sobrenome, idade, sexo, altura, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def exibir_informacoes(self):
        print(f"\nInformações do Jogador:")
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade} anos")
        print(f"Sexo: {self.sexo}")
        print(f"Altura: {self.altura} metros")
        print(f"Peso: {self.peso} kg")

def solicitar_input(mensagem, padrao):
    while True:
        entrada = input(mensagem)
        if re.match(padrao, entrada):
            return entrada
        else:
            print("Entrada inválida. Tente novamente.")

# Padrões de validação
padrao_nome_sobrenome = r"^[A-Za-zÀ-ÿ\s]+$"
padrao_sexo = r"^[A-Za-zÀ-ÿ\s]+$"
padrao_idade = r"^\d+$"
padrao_altura_peso = r"^\d+(\.\d+)?$"

# Solicitar informações do usuário com validação
nome = solicitar_input("Digite o nome do jogador: ", padrao_nome_sobrenome)
sobrenome = solicitar_input("Digite o sobrenome do jogador: ", padrao_nome_sobrenome)
idade = int(solicitar_input("Digite a idade do jogador: ", padrao_idade))
sexo = solicitar_input("Digite o sexo do jogador: ", padrao_sexo)
altura = float(solicitar_input("Digite a altura do jogador (em metros): ", padrao_altura_peso))
peso = float(solicitar_input("Digite o peso do jogador (em kg): ", padrao_altura_peso))

# Criar instância da classe Jogador
jogador = Jogador(nome, sobrenome, idade, sexo, altura, peso)

# Exibir as informações do jogador
jogador.exibir_informacoes()