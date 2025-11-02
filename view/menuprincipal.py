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
            case 1: controller.cadastrar()
            
            case 2: controller.exibir()