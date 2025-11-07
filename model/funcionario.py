from model.pessoa import pessoa

class funcionario(pessoa):
    def __init__(self,codigo,nome,salario,cargo):
        super().__init__ (codigo,nome)
        self.salario = salario
        self.cargo = cargo

    def get_codigo(self):
        return self.codigo
    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario
    def get_cargo(self):
        return self.cargo