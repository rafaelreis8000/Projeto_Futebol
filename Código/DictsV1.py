lista_usuarios = []

class Usuario():
    # Define as variáveis da classe (objeto) "Usuario".
    nome = ''
    senha = ''

# Cadastro de usuário
    def cadastro(self):
    # Define as duas propriedades do objeto 'Usuario'.
        self.nome = input("Informe o nome de usuário desejado: ") 
        self.senha = input("Informe a senha desejada: ")
    # Anexa um usuário particular já definido com nome e senha a uma lista de objetos do mesmo tipo.
        lista_usuarios.append(self)
        print("Cadastrado com sucesso!")
        return self # Retorna o objeto à função que chamou a definição.

# Verificação de senha
def verificar_senha(usuario_identificado): # Recebe um objeto 'Usuario'
    consultar_senha = input("{} informe a senha: ".format(usuario_identificado.nome))
    if consultar_senha == usuario_identificado.senha: # Verifica se a senha fornecida é igual a propriedade senha do usuario que foi fornecido pela definição.
        print("Senha correta")
    else:
        print("Senha incorreta")

# Login   
def login():
    nome_para_teste = input("Informe o usuario: ") 
    for x in lista_usuarios: # Aloca em x os usuários cadastrados.
        if nome_para_teste  == x.nome: # Verifica se a propriedade nome dos usuários é igual ao nome fornecido.
            print("Usuário correto!")
            verificar_senha(x) # Chama a verificação de senha para o usuário 'x'.
        else:
            print("Usuário incorreto!")

# Menu cadastro
menu = 3
while menu != 0:
    print("Se você já é cadastrado digite (1)")
    print("Se você não é cadastrado digite (2)")
    print("Digite zero para sair.")
    menu= int(input("Digite a opção:"))
    if menu == 1:
        login()
    if menu == 2:
        pessoa = Usuario() # Define a variavel 'pessoa' como do tipo 'Usuario'.
        pessoa.cadastro() # Como 'pessoa' é da classe 'Usuario' ela tem a definição de classe "cadastro()".
        verificar_senha(pessoa) # Chama a verificação de senha pro usuário recêm cadastrado.
    if menu == 0:
        for x in lista_usuarios:
            print('Usuário: {}, senha: {}'.format(x.nome,x.senha))