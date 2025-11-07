from model.venda import venda
from . import clientecontroller as clicontroller
from . import funcionariocontroller as funccontroller


vendas = []

def vender(codigo,valor,cliente,funcionario):
    for c in clicontroller.clientes:
        if cliente == c.codigo:
            clienteexistente = c

    for f in funccontroller.funcionarios:
        if funcionario == f.codigo:
            funcionarioexistente = f

    
    novavenda = venda(codigo,valor,clienteexistente,funcionarioexistente)        


    if funccontroller.validacodfun(novavenda.funcionario.codigo) == True:
        if clicontroller.validacodcli(novavenda.cliente.codigo) == True:
            if novavenda.cliente.saldo >= novavenda.valor:
                valorsaldoposvenda = novavenda.cliente.saldo - novavenda.valor
                novavenda.cliente.saldo = valorsaldoposvenda
                vendas.append(novavenda)
                print("Venda Realizada com sucesso")
            else:
                print("Saldo Insuficiente para a compra")
        else:
            print("Cliente não está cadastrado")
            return
    else:
        print("O Funcionario nao está no sistema")
       