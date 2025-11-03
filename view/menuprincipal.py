import controller.controller as controller


def menuprinc():

    opcao = -1

    while opcao != 0:
        print("======")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Funcionario")
        print("3 - Exibir")
        print("4 - Vender")
        print("======")
        opcao = int(input('Opcao: '))

        match opcao:
            case 1:
                codigo = input('Digite o codigo: ')
                nome = input('Digite o nome: ')
                saldo = int(input('Digite o saldo: '))
                tipo = input('Digite o tipo: ')

                controller.cadastrarc(codigo,nome,saldo,tipo)
            case 2: 
                codigo = input('Digite o codigo: ')
                nome = input('Digite o nome: ')
                salario = int(input('Digite o salario: '))
                tipo = input('Digite o tipo: ')

                controller.cadastrarf(codigo,nome,salario,tipo)


            case 3: controller.exibir()
            

          
            