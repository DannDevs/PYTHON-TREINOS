from model.cliente import cliente


clientes = []



def cadastrarc(codigo,nome,saldo):

    if validacodcli(codigo) == True :
        print("Cod ja existe!") 
        return;

    novocliente = cliente(codigo,nome,saldo)
    clientes.append(novocliente)

    print("Cliente Cadastrado com sucesso!")


def exibir():
    if not clientes:
        print("Nao existe Clientes cadastrados!!")
        return

    for c in clientes:
        print("====")
        print(f"Codigo: {c.codigo}")
        print(f"Nome: {c.nome}")
        print(f"Saldo: {c.saldo}")
        print("====")

def excluir(codigo):
    
    if not validacodcli(codigo):
        print("Codigo Nao esta no sistema")
        return
    clienteexistente =  None


    for c in clientes:
        if codigo == c.codigo:
            clienteexistente = c

    clientes.remove(clienteexistente)      
    print("Cliente removido com sucesso")

def validacodcli(codigo):
    for c in clientes:
        if c.codigo == codigo:
            return True
    return False

 
    