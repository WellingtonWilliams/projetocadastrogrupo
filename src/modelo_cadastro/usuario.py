class Usuario:
    
    def __init__(self):
        self.__nome:str = ''
        self.__sobrenome:str = ''
        self.__user:str = ''
        self.__senha_1:str = ''
        self.__senha_2:str = ''
        self.error:str = ''

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome:str) -> None:
        if nome != '':
            self.__nome = nome
            self.error = ''
        else:
            self.error = 'O campo "Nome" é obrigatório'

    @property
    def sobrenome(self) -> str:
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome:str) -> None:
        if sobrenome != '':
            self.__sobrenome = sobrenome
            self.error = ''
        else:
            self.error = 'O campo "Sobrenome" é obrigatório'

    @property
    def user(self) -> str:
        return self.__user

    @user.setter
    def user(self, user:str) -> None:
        if user != '':
            self.__user  = user
            self.error = ''
        else:
            self.error = 'O campo "user" é obrigatório'

    @property
    def senha_1(self) -> str:
        return self.__senha_1

    @senha_1.setter
    def senha_1(self, senha_1:str) -> None:
        if senha_1 != '':
            if len(senha_1) >= 5 and len(senha_1) <= 8:
                self.__senha_1 = senha_1
                self.error = ''
            else:
                self.error = 'A senha deve possuir entre 5 a 8 caracteres'
        else:
            self.error = 'O campo "senha" é obrigatório'

    @property
    def senha_2(self) -> str:
        return self.__senha_2

    @senha_2.setter
    def senha_2(self, senha_2:str) -> None:
        if senha_2 != '':
            if senha_2 == self.senha_1:
                self.__senha_2 = senha_2
            else:
                self.error = 'As senhas fornecidas não são iguais'
        else:
            self.error = 'É obrigatório a confirmação da senha'
