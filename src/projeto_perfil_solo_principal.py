import sys

from projeto_perfil_solo import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class Projeto_perfil_solo_principal(Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.frame_msg_erro.hide()
        self.stacked_widget.setCurrentWidget(self.page_login)
        self.pushButton_entrar.clicked.connect(self.realizar_login)

    def realizar_login (self):
        login = self.lineEdit_inserir_login.text()
        senha = self.lineEdit_inserir_senha.text()
        if login == 'cllw' and senha == '128167':
            self.lineEdit_inserir_login.setText('')
            self.lineEdit_inserir_senha.setText('')
            self.frame_msg_erro.hide('')
            self.stacked_widget.setCurrentWidget(self.page_principal)
        else:
            self.label_msg_erro.setText('Seu login ou senha estão incorrtos!!!')
            self.frame_msg_erro.show()  


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    projeto_perfil_solo_principal = Projeto_perfil_solo_principal()
    projeto_perfil_solo_principal.show()
    qt.exec()

