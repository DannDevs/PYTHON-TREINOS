from model.cliente import cliente

clientes = []


def cadastrar():
    cliente1 = cliente("Daniel",1200,"VIP")
    clientes.append(cliente1)

    print("Cliente Cadastrado com sucesso!")

def exibir():

    for c in clientes:
        print(f"Nome: {c.nome}")
        print(f"Saldo: {c.saldo}")


 
    
    