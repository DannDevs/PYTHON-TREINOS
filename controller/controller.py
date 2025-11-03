from model.cliente import cliente
from model.funcionario import funcionario

clientes = []
funcionarios = []


def cadastrarc(codigo,nome,saldo,tipo):

    if validacodcli(codigo) == True :
        print("Cod ja existe!") 
        return;

    novocliente = cliente(codigo,nome,saldo,tipo)
    clientes.append(novocliente)

    print("Cliente Cadastrado com sucesso!")

def cadastrarf(codigo,nome,salario,tipo):
    
    if validacodfun(codigo) == True:
        print("Codigo ja foi cadastrado!")
        return

    novofuncionario = funcionario(codigo,nome,salario,tipo)
    funcionarios.append(novofuncionario)

    print("Funcionario Cadastrado com sucesso")

def exibir():
    if not clientes:
        print("Nao existe Clientes cadastrados!!")

    for c in clientes:
        print("====")
        print(f"Codigo: {c.get_codigo()}")
        print(f"Nome: {c.get_nome()}")
        print(f"Saldo: {c.get_saldo()}")
        print("====")

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

def validacodfun(codigo):
    for f in funcionario:
        if f.codigo == codigo:
            return True
    return False    
    