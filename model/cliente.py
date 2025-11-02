class cliente:
    def __init__(self,nome,saldo,tipo):
        self.nome = nome
        self.saldo = saldo
        self.tipo = tipo

    def get_nome(self):
        return self._nome
    
    def get_saldo(self):
        return self.saldo
    
    def get_tipo(self):
        return self.tipo
    