import sys

from projeto_perfil_solo_base import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Projeto_perfil_solo_principal(Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.frame_msg_erro.hide()
        self.stacked_widget.setCurrentWidget(self.page_login)
        self.pushButton_entrar.clicked.connect(self.realizar_login)
        self.pushButton_fechar_msg_erro.clicked.connect(lambda : self.frame_msg_erro.hide())
        self.push_button_sair.clicked.connect(self.sair_sistema)
        self.push_button_cadastrar.clicked.connect(self.page_de_cadastro)
        self.push_button_listar.clicked.connect(self.page_de_listar)
        self.push_button_voltar.clicked.connect(self.voltar_page_principal)
        self.push_button_voltar_2.clicked.connect(self.voltar_2_page_principal)
    
    def voltar_2_page_principal(self):
        self.stacked_widget.setCurrentWidget(self.page_principal)


    def voltar_page_principal(self):
        self.stacked_widget.setCurrentWidget(self.page_principal)


        self.set_label_img(self.label_icone_login, 'img/icone_login.jpg')
        self.set_label_img(self.label_logo_empresa, 'img/icone_login_CLLW.png')
        self.set_label_img(self.label_logo_empresa_2, 'img/icone_login_CLLW.png')

    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)

    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)


    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)

    def page_de_listar(self):
        self.stacked_widget.setCurrentWidget(self.page_listar)   

    def page_de_cadastro(self):
        self.stacked_widget.setCurrentWidget(self.page_cadastrar)    

    def sair_sistema(self):
        self.stacked_widget.setCurrentWidget(self.page_login)

    def realizar_login (self):
        login = self.lineEdit_inserir_login.text()
        senha = self.lineEdit_inserir_senha.text()
        if login == 'cllw' and senha == '128167':
            self.lineEdit_inserir_login.setText('')
            self.lineEdit_inserir_senha.setText('')
            self.frame_msg_erro.hide()
            self.stacked_widget.setCurrentWidget(self.page_principal)
            print('Login realizado com sucesso')
            
        else:
            self.label_msg_erro.setText('Seu login ou senha estão incorretos!!!')
            self.frame_msg_erro.show()
        
      


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    projeto_perfil_solo_principal = Projeto_perfil_solo_principal()
    projeto_perfil_solo_principal.show()
    qt.exec()
