import controller.clientecontroller as clientecontroller


def menucliente():
   opcao = -1
   
   while opcao != 0:

    print("======")
    print("1 - Cadastar")
    print("2 - Exibir")
    print("3 - Remover")
    print("0 - Voltar")
    print("======")     

    try:
      opcao = int(input("Digite a Opçao: "))
    except:
      print("Opçao invalida!")   
      continue

    match opcao:
        case 1:
                codigo = int(input('Digite o codigo: '))
                nome = input('Digite o nome: ')
                saldo = int(input('Digite o saldo: '))

                clientecontroller.cadastrarc(codigo,nome,saldo)
       
        case 2:
            clientecontroller.exibir()
        case 3:
            codigo = int(input('Digite o codigo do cliente a remover: '))
            clientecontroller.excluir(codigo)
          

     











   





