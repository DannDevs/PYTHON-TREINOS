from model.funcionario import funcionario
from . import clientecontroller as clicontroller
from dao.funcionariodao import funcionariodao

dao = funcionariodao()

funcionarios = []

def cadastrarf(codigo,nome,salario,cargo):
    
    if validacodfun(codigo) == True:
        print("Codigo ja foi cadastrado!")
        return

    novofuncionario = funcionario(codigo,nome,salario,cargo)
    dao.inserir(novofuncionario)

def exibir():

    atualizarlista()

    if not funcionarios:
        print("A lista de funcionarios esta vazia")
    
    else:
        for f in funcionarios:
            
            print("=======")
            print(f"Codigo:  {f.codigo}" )
            print(f"Nome:  {f.nome} " )
            print(f"Cargo: {f.cargo}"  )
            print(f"Salario: {f.salario}" )
            print("=======")

def validacodfun(codigo):
    atualizarlista()
    
    for f in funcionarios:
        if f.codigo == codigo:
            return True
    return False   
def atualizarlista():
    resultados = dao.listar()
    funcionarios.clear()
    
    for f in resultados:
        funcionarios.append(f)
        



