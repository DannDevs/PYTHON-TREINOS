from model.pessoa import pessoa

class funcionario(pessoa):
    def __init__(self,codigo,nome,salario,cargo):
        super().__init__ (codigo,nome)
        self.salario = salario
        self.cargo = cargo
