from model.cliente import cliente
from dao.clientedao import clientedao

clientes = []

dao =  clientedao()

def cadastrarc(codigo,nome,saldo):

    if validacodcli(codigo) == True :
        print("Cod ja existe!") 
        return;

    novocliente = cliente(codigo,nome,saldo)
    dao.inserir(novocliente)

def exibir():
    atualizalista()

    for c in clientes:
        print("======")
        print(f"Codigo: {c.codigo}")
        print(f"Nome: {c.nome}")
        print(f"saldo: {c.saldo}")
        print("======")

def excluir(codigo):
    
    atualizalista()

    if not validacodcli(codigo):
        print("Codigo Nao esta no sistema")
        return
    clienteexistente =  None

    for c in clientes:
        if codigo == c.codigo:
            clienteexistente = c
    
    dao.excluir(clienteexistente)
   


def validacodcli(codigo):
    atualizalista()
    for c in clientes:
        if c.codigo == codigo:
            return True
    return False


def atualizalista():

    clientesatualizados = dao.listar()
    clientes.clear()

    for c in clientesatualizados:
        clientes.append(c)
    

    


 
    