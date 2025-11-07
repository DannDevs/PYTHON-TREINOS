from model.pessoa import pessoa

class cliente(pessoa):
    def __init__(self,codigo,nome,saldo,tipo):
        super().__init__(codigo,nome)
        self.saldo = saldo
        self.tipo = tipo


    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome
    
    def get_saldo(self):
        return self.saldo
    
    def get_tipo(self):
        return self.tipo
    
    def set_saldo(self,saldo):
        self._saldo = saldo
    
    