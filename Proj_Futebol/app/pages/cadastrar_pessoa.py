import sqlite3
import flet as ft

def buscar_times(nome_time: str):
    # Conecte-se ao banco de dados
    conn = sqlite3.connect('futebol.db')
    cursor = conn.cursor()

    # Busque os times que começam com o nome_time
    cursor.execute("SELECT nome FROM times WHERE nome LIKE ?", (f"{nome_time}%",))
    resultados = cursor.fetchall()
    # Feche a conexão
    conn.close()
    return [r[0] for r in resultados]  # Retorne uma lista de nomes

def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Validação simples do CPF (não é completa)
    if cpf == cpf[0] * len(cpf):  # Se todos os dígitos forem iguais
        return False
    
    # Cálculo dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False
    return True

def cadastrar_pessoa(page: ft.Page):
    input_nome = ft.TextField(label="Nome")
    input_email = ft.TextField(label="Email")
    
    # Campo para CPF com limitação de caracteres
    input_cpf = ft.TextField(label="CPF", hint_text="Digite o CPF sem pontos ou traços", max_length=11)

    selecione_cargo = ft.Dropdown(
        label="Cargo",
        options=[
            ft.dropdown.Option("Torcedor"),
            ft.dropdown.Option("Ajudante"),
            ft.dropdown.Option("Jogador"),
            ft.dropdown.Option("Técnico")
        ]
    )

    input_time = ft.TextField(label="Nome do Time")  # Campo para entrada do nome do time
    lista_sugestoes = ft.Column(controls=[], visible=False)  # Lista para sugestões

    # Adicionando um texto para indicar que as opções são sugestões
    sugestao_label = ft.Text("Sugestões:", size=16, weight="bold", visible=False)

    def atualizar_sugestoes(e):
        # Obtenha as sugestões baseadas no que o usuário digitou
        sugestoes = buscar_times(input_time.value)

        # Atualize as opções da lista de sugestões
        lista_sugestoes.controls.clear()  # Limpe as sugestões anteriores

        for nome in sugestoes:
            # Adicione cada sugestão como um botão clicável
            lista_sugestoes.controls.append(
                ft.TextButton(
                    text=nome,
                    on_click=lambda e, nome=nome: selecionar_time(nome),  # Passa o nome do time
                )
            )
        if sugestoes:
            sugestao_label.visible = True  # Torna o texto de sugestão visível
        else:
            sugestao_label.visible = False  # Esconde o texto se não houver sugestões

        lista_sugestoes.visible = bool(sugestoes)
        page.update()  # Atualize a página para refletir a mudança

    def selecionar_time(nome: str):
        # Quando o usuário selecionar uma sugestão, preencha o campo de texto
        input_time.value = nome
        lista_sugestoes.visible = False
        sugestao_label.visible = False  # Esconde o texto de sugestão
        page.update()  # Atualize a página

    # Defina a função de atualização ao alterar o texto
    input_time.on_change = atualizar_sugestoes

    def validar_cpf_e_atualizar(e):
        if validar_cpf(input_cpf.value):
            print("CPF válido")
        else:
            print("CPF inválido")
        page.update()  # Atualiza a página para refletir mudanças

    # Adicionando a validação do CPF ao campo perder foco
    input_cpf.on_blur = validar_cpf_e_atualizar

    botao_cadastrar = ft.ElevatedButton(
        "Cadastrar",
        on_click=lambda e: [
            print(f"Nome: {input_nome.value}, Email: {input_email.value}, CPF: {input_cpf.value}, Cargo: {selecione_cargo.value}, Time: {input_time.value}")
        ]
    )

    return ft.Column(
        controls=[
            input_nome,
            input_email,
            input_cpf,  # Adicione o campo CPF
            selecione_cargo,
            input_time,
            sugestao_label,  # Adicione a label de sugestão
            lista_sugestoes,  # Adicione a lista de sugestões
            botao_cadastrar
        ]
    )

# def main(page: ft.Page):
#     page.title = "Cadastro de Pessoas"
#     page.add(cadastrar_pessoa(page))

# ft.app(target=main)
