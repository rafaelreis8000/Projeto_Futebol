user_dict= []

"""loop no código"""
ativo = True

while ativo:
    keys= input("Nome: ")
    values= input("Data: ")

    if ativo or values == 'quit':
        ativo = False
    else:
        user_dict.update({keys: values})