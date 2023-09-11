from typing import List
from modelo_cadastro.perfil_solo import Perfil_Solo

class Perfil_Control:

    def __init__(self):
        self.__lista_perfis:List[Perfil_Solo] = []

    def adicionar_perfil(self, perfil:Perfil_Solo) -> str:
        self.__lista_perfis.append(perfil)
        return 'Perfil adicionado com sucesso'

    def acessar_perfil(self, indice:int) -> Perfil_Solo:
        perfil = self.__lista_perfis[indice]
        return perfil

    def alterar_perfil(self, indice:int, perfil:Perfil_Solo) -> str:
        self.__lista_perfis[indice] = perfil
        return 'Perfil alterado com sucesso'

    def excluir_perfil(self, indice:int) -> str:
        del self.__lista_perfis[indice]
        return 'Perfil excluído com sucesso'

    @property
    def lista_perfis(self) -> List[Perfil_Solo]:
        return self.__lista_perfis

    @lista_perfis.setter
    def lista_perfis(self, lista:List[Perfil_Solo]) -> None:
        pass
