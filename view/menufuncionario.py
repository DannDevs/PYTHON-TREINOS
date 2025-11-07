import controller.funcionariocontroller as funcionariocontroller

def menufuncionario():
    opcao = -1

    while opcao != 0:
         
        print("======")
        print("1 -  Cadastar Funcionario")
        print("2 -  Exibir Funcionario")
        print("3 -  Vender")
        print("======")

        try:
            opcao = int(input(('Digite a Opçao: ')))
        except:
            print("Digite uma opçao valida")
            continue
        
        match opcao:
            case 1:
                codigo = int(input('Digite o codigo: '))
                nome = input('Digite o nome: ')
                salario = int(input('Digite o salario: '))
                cargo = input('Digite o Cargo: ')

                funcionariocontroller.cadastrarf(codigo,nome,salario,cargo)
                
            case 2: funcionariocontroller.exibir()
            case 3: funcionariocontroller.vender()
    