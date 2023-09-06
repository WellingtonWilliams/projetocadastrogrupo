
class Perfil_Solo: 
    def __init__(self, codigo_de_serviço = None, tipo_de_solo = None, cor = None, estrutura = None, localização_área = None, horizonte = None, textura = None, profundidade = None) -> None:
        self.error = ''
        self.codigo_de_serviço = codigo_de_serviço
        self.tipo_de_solo = tipo_de_solo 
        self.cor = cor 
        self.estrutura = estrutura 
        self.localização_área = localização_área
        self.horizonte = horizonte
        self.textura = textura 
        self.profundidade = profundidade 

    @property
    def  codigo_de_serviço(self):
        return self.__codigo_de_serviço
    
    @codigo_de_serviço.setter
    def codigo_de_serviço(self, codigo_de_serviço):
        if codigo_de_serviço != None and len(codigo_de_serviço) != 0:
            self.error = 'O "codigo_de_serviço" é obrigatório'
        else:
            self.__codigo_de_serviço = codigo_de_serviço
            