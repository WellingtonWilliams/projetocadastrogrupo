class Perfil_Solo:

    def __init__(self) -> None:
        self.codigo_servico:str = ''
        self.tipo_solo:str = ''
        self.cor:str = ''
        self.estrutura:str = ''
        self.localizacao_area:str = ''
        self.horizonte:str = ''
        self.textura:str = ''
        self.profundidade:str = ''
        self.error = ''

    @property
    def codigo_servico(self) -> str:
        return self.__codigo_servico

    @codigo_servico.setter
    def codigo_servico(self, codigo_servico:str) -> None:
        self.__codigo_servico = ''
        if codigo_servico != '':
            self.__codigo_servico = codigo_servico
            self.error =  ''
        else:
            self.error = 'O campo "Código de Serviço" é obrigatório'

    @property
    def tipo_solo(self) -> str:
        return self.__tipo_solo

    @tipo_solo.setter
    def tipo_solo(self, tipo_solo:str) -> None:
        self.__tipo_solo = ''
        if tipo_solo != '' and tipo_solo != '-':
            self.__tipo_solo = tipo_solo
            self.error = ''
        else:
            self.error = 'O campo "Tipo de Solo" é obrigatório'

    @property
    def cor(self) -> str:
        return self.__cor

    @cor.setter
    def cor(self, cor:str) -> None:
        self.__cor = ''
        if cor != '':
            self.__cor = cor
            self.error = ''
        else:
            self.error = 'O campo "Cor" é obrigatório'

    @property
    def estrutura(self) -> str:
        return self.__estrutura

    @estrutura.setter
    def estrutura(self, estrutura:str) -> None:
        self.__estrutura = ''
        if estrutura != '':
            self.__estrutura = estrutura
            self.error = ''
        else:
            self.error = 'O campo "Estrutura" é obrigatório'

    @property
    def localizacao_area(self) -> str:
        return self.__localizacao_area

    @localizacao_area.setter
    def localizacao_area(self, localizacao_area:str) -> None:
        self.__localizacao_area = ''
        if localizacao_area != '':
            self.__localizacao_area = localizacao_area
            self.error = ''
        else:
            self.error = 'O campo "Localização/Área" é obrigatório'

    @property
    def horizonte(self) -> str:
        return self.__horizonte

    @horizonte.setter
    def horizonte(self, horizonte:str) -> None:
        self.__horizonte = ''
        if horizonte != '':
            self.__horizonte = horizonte
            self.error = ''
        else:
            self.error = 'O campo "Horizonte" é obrigatório'

    @property
    def textura(self) -> str:
        return self.__textura

    @textura.setter
    def textura(self, textura:str) -> None:
        self.__textura = ''
        if textura != '':
            self.__textura = textura
            self.error = ''
        else:
            self.error = 'O campo "Textura" é obrigatório'

    @property
    def profundidade(self) -> str:
        return self.__profundidade

    @profundidade.setter
    def profundidade(self, profundidade: str) -> None:
        self.__profundidade = ''
        if profundidade != '':
            self.__profundidade = profundidade
            self.error = ''
        else:
            self.error = 'O campo "Profundidade (m/cm)" é obrigatório'
