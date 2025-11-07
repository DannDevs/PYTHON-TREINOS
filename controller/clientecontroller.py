from model.cliente import cliente


clientes = []



def cadastrarc(codigo,nome,saldo,tipo):

    if validacodcli(codigo) == True :
        print("Cod ja existe!") 
        return;

    novocliente = cliente(codigo,nome,saldo,tipo)
    clientes.append(novocliente)

    print("Cliente Cadastrado com sucesso!")


def exibir():
    if not clientes:
        print("Nao existe Clientes cadastrados!!")
        return

    for c in clientes:
        print("====")
        print(f"Codigo: {c.get_codigo()}")
        print(f"Nome: {c.get_nome()}")
        print(f"Saldo: {c.get_saldo()}")
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

def vender(cliente,valor):
    if cliente.get_saldo() > valor:
        print("Venda Realizada")
        novo_saldo = cliente.get_saldo() - valor
        cliente.set_saldo() == novo_saldo

def validacodcli(codigo):
    for c in clientes:
        if c.codigo == codigo:
            return True
    return False

 
    