from . import menufuncionario as menufunc
from . import menucliente as menucli


def menuprinc():

    opcao = -1

    while opcao != 0:
        print("======")
        print("1 - Menu Cliente")
        print("2 - Menu Fornecedor")
        print("0 - Sair")
        print("======")
        opcao = int(input('Opcao: '))

        match opcao:
            case 1:
                menucli.menucliente()
            case 2: 
                menufunc.menufuncionario()
            case 0:
                print("Saindo.....")
            case _:
                print("Opçao invalida.")            
            

          
            