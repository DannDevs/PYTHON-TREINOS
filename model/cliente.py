class cliente:
    def __init__(self,codigo,nome,saldo,tipo):
        self.codigo = codigo
        self.nome = nome
        self.saldo = saldo
        self.tipo = tipo


    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome
    
    def get_saldo(self):
        return self.saldo
    
    def get_tipo(self):
        return self.tipo
    
    def set_saldo(self,saldo):
        self._saldo = saldo
    
    