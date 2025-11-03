from model.cliente import cliente

clientes = []


def cadastrar(codigo,nome,saldo,tipo):
    if validacod(codigo) == True :
        print("Cod ja existe!")
        return;
    novocliente = cliente(codigo,nome,saldo,tipo)
    clientes.append(novocliente)

    print("Cliente Cadastrado com sucesso!")

def exibir():

    for c in clientes:
        print("====")
        print(f"Codigo: {c.codigo}")
        print(f"Nome: {c.nome}")
        print(f"Saldo: {c.saldo}")
        print("====")

def validacod(codigo):
    for c in clientes:
        if c.codigo == codigo:
            return True
    return False

        
        
 
    
    