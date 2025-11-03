import controller.controller as controller

def menuprinc():
    opcao = -1

    while opcao != 0:
        print("======")
        print("1 cadastrar")
        print("2 exibir")
        print("======")
        
        opcao = int(input('Opcao: '))

        match opcao:
            case 1: 
                codigo = input('Digite o codigo: ')
                nome = input('Digite o nome: ')
                saldo = int(input('Digite o saldo: '))
                tipo = input('Digite o tipo: ')

                controller.cadastrar(codigo,nome,saldo,tipo)
            
            case 2: controller.exibir()