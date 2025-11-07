from model.pessoa import pessoa

class cliente(pessoa):
    def __init__(self,codigo,nome,saldo):
        super().__init__(codigo,nome)
        self.saldo = saldo

    
    
