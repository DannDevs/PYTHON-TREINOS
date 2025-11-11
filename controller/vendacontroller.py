from model.venda import venda
from . import clientecontroller as clicontroller
from . import funcionariocontroller as funccontroller
from dao.vendadao import vendadao

dao = vendadao()


vendas = []

def vender(codigo,valor,cliente,funcionario):
    
    atualizarlista()
    clicontroller.atualizalista()
    funccontroller.atualizarlista()

    if validarcodvenda(codigo):
        print("Codigo venda ja existe")
        return

    if funccontroller.validacodfun(cliente) == True:
        if clicontroller.validacodcli(funcionario) == True:

            for c in clicontroller.clientes:
                if cliente == c.codigo:
                    clienteexistente = c

            for f in funccontroller.funcionarios:
                if funcionario == f.codigo:
                    funcionarioexistente = f
        
            novavenda = venda(codigo,valor,clienteexistente,funcionarioexistente)        

            if clienteexistente.saldo >= novavenda.valor:

                    valorsaldoposvenda = clienteexistente.saldo - novavenda.valor
                    clienteexistente.saldo = valorsaldoposvenda
                    dao.inserir(novavenda)
            else:
                print("Saldo Insuficiente para a compra")
                return
        else:
            print("Cliente não está cadastrado")
            return
    else:
        print("O Funcionario nao está no sistema")
        return

def emitirrelatorio():
    
    atualizarlista()
    if not vendas:
        print("Nao há vendas a exibir")
        return
    
    for v in vendas:
        print("======")
        print(f"Codigo: {v.codigo}")
        print(f"Valor: {v.valor}")
        print(f"Cliente: {v.cliente}")
        print(f"Funcionario: {v.funcionario}")
        print("======")


def validarcodvenda(codigo):
    
    atualizarlista()
    for v in vendas:
        if v.codigo == codigo:
            return True
    return False
    


def atualizarlista():

    vendaatualizadas = dao.listar()
    vendas.clear()

    for v in vendaatualizadas:
        vendas.append(v)


       