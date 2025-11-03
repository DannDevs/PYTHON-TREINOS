class funcionario:
    def __init__(self,codigo,nome,salario,tipo):
        self.codigo = codigo
        self.nome = nome
        self.salario = salario
        self.tipo = tipo

    def get_codigo(self):
        return self.codigo
    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario