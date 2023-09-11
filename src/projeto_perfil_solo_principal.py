import sys

from projeto_perfil_solo_base import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QTableWidgetItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from modelo_cadastro.perfil_solo import Perfil_Solo
from controle_cadastro.perfil_control import Perfil_Control

class Projeto_perfil_solo_principal(Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.controle_perfil = Perfil_Control()
        self.load_imgs() # trocar
        self.inicializar_componentes()
        self.cor_erro = 'background-color: rgb(139, 0, 0); color: rgb(255, 255, 255)'
        self.cor_sucesso = 'background-color: rgb(51, 255, 51); color: rgb(255, 255, 255)'

    def inicializar_componentes(self) -> None:
        #page_login
        self.frame_msg_erro.hide()
        #self.label_icone_login
        self.pushButton_entrar.clicked.connect(self.realizar_login)
        self.pushButton_fechar_msg_erro.clicked.connect(lambda: self.frame_msg_erro.hide())

        #page_principal
        #self.label_logo_empresa
        self.push_button_cadastrar.clicked.connect(self.acessar_cadastrar)
        self.push_button_listar.clicked.connect(self.acessar_listar)
        self.push_button_sair.clicked.connect(self.sair)

        #page_cadastrar
        self.frame_msg_cadastro_invalido.hide()
        #self.label_logo_empresa_2
        self.push_button_voltar.clicked.connect(self.acessar_principal)
        self.push_button_salvar.clicked.connect(self.salvar_perfil)
        self.push_button_fechar_msg_cadastro_invalido.clicked.connect(lambda: self.frame_msg_cadastro_invalido.hide())

        #page_listar
        self.push_button_voltar_2.clicked.connect(self.acessar_principal)
        self.push_button_alterar.clicked.connect(self.alterar_dados)
        self.push_button_excluir.clicked.connect(self.excluir_perfil)

    def realizar_login (self) -> None:
        login = self.lineEdit_inserir_login.text()
        senha = self.lineEdit_inserir_senha.text()
        if login == 'cllw' and senha == '128167':
            self.lineEdit_inserir_login.setText('')
            self.lineEdit_inserir_senha.setText('')
            self.frame_msg_erro.hide()
            self.acessar_principal()
            print('Login realizado com sucesso')
        else:
            msg = 'Login ou Senha incorretos'
            self.label_msg_erro.setText(msg)
            self.label_msg_erro.setStyleSheet(self.cor_erro)
            self.frame_msg_erro.show()

    #Métodos de Perfil de Solo

    def salvar_perfil(self) -> None:
        indice = self.table_widget_itens.currentRow()
        perfil_solo = Perfil_Solo()
        perfil_solo.codigo_servico = self.line_edit_codigo_servio.text()
        perfil_solo.tipo_solo = self.combo_box_tipo_solo.currentText()
        perfil_solo.cor = self.line_edit_cor.text()
        perfil_solo.estrutura = self.line_edit_estrutura.text()
        perfil_solo.localizacao_area = self.line_edit_localizacao_area.text()
        perfil_solo.horizonte = self.lineEdit_horizonte.text()
        perfil_solo.textura = self.line_edit_textura.text()
        perfil_solo.profundidade = self.lineEdit_profundidade.text()
        if len(perfil_solo.error) != 0:
            self.label_msg_erro_cadastro.setText(perfil_solo.error)
            self.label_msg_erro_cadastro.setStyleSheet(self.cor_erro)
            self.frame_msg_cadastro_invalido.show()
        else:
            if indice >= 0:
                msg = self.controle_perfil.alterar_perfil(indice, perfil_solo)
                self.label_msg_erro_cadastro.setText(msg)
                self.label_msg_erro_cadastro.setStyleSheet(self.cor_sucesso)
                self.frame_msg_cadastro_invalido.show()
                self.tabelar_perfil()
                self.limpar_formulario()
                self.table_widget_itens.clearSelection()
            else:
                msg = self.controle_perfil.adicionar_perfil(perfil_solo)
                self.label_msg_erro_cadastro.setText(msg)
                self.label_msg_erro_cadastro.setStyleSheet(self.cor_sucesso)
                self.frame_msg_cadastro_invalido.show()
                self.tabelar_perfil()
                self.limpar_formulario()

    def tabelar_perfil(self) -> None:
        cont_linhas = 0
        self.table_widget_itens.clearContents()
        self.table_widget_itens.setRowCount(len(self.controle_perfil.lista_perfis))
        for perfil_solo in self.controle_perfil.lista_perfis:
            self.table_widget_itens.setItem(cont_linhas, 0, QTableWidgetItem(perfil_solo.codigo_servico))
            self.table_widget_itens.setItem(cont_linhas, 1, QTableWidgetItem(perfil_solo.localizacao_area))
            self.table_widget_itens.setItem(cont_linhas, 2, QTableWidgetItem(perfil_solo.tipo_solo))
            self.table_widget_itens.setItem(cont_linhas, 3, QTableWidgetItem(perfil_solo.horizonte))
            self.table_widget_itens.setItem(cont_linhas, 4, QTableWidgetItem(perfil_solo.cor))
            self.table_widget_itens.setItem(cont_linhas, 5, QTableWidgetItem(perfil_solo.textura))
            self.table_widget_itens.setItem(cont_linhas, 6, QTableWidgetItem(perfil_solo.estrutura))
            self.table_widget_itens.setItem(cont_linhas, 7, QTableWidgetItem(perfil_solo.profundidade))
            cont_linhas += 1

    def alterar_dados(self) -> None:
        indice = self.table_widget_itens.currentRow()
        if indice >= 0:
            perfil = self.controle_perfil.acessar_perfil(indice)
            self.line_edit_codigo_servio.setText(perfil.codigo_servico)
            if perfil.tipo_solo == 'Argiloso':
                indice = 1
            elif perfil.tipo_solo == 'Arenoso':
                indice = 2
            elif perfil.tipo_solo == 'Calcário':
                indice = 3
            elif perfil.tipo_solo == 'Humoso':
                indice = 4
            self.combo_box_tipo_solo.setCurrentIndex(indice)
            self.line_edit_cor.setText(perfil.cor)
            self.line_edit_estrutura.setText(perfil.estrutura)
            self.line_edit_localizacao_area.setText(perfil.localizacao_area)
            self.lineEdit_horizonte.setText(perfil.horizonte)
            self.line_edit_textura.setText(perfil.textura)
            self.lineEdit_profundidade.setText(perfil.profundidade)
            self.acessar_cadastrar()
        else:
            print('Selecione o perfil a ser alterado')

    def excluir_perfil(self) -> None:
        indice = self.table_widget_itens.currentRow()
        if indice >= 0:
            msg = self.controle_perfil.excluir_perfil(indice)
            self.table_widget_itens.clearSelection()
            self.tabelar_perfil()
            print(msg)
        else:
            print('Selecione o perfil a ser excluído')

    def limpar_formulario(self) -> None:
        self.line_edit_codigo_servio.clear()
        self.combo_box_tipo_solo.setCurrentIndex(0)
        self.line_edit_cor.clear()
        self.line_edit_estrutura.clear()
        self.line_edit_localizacao_area.clear()
        self.lineEdit_horizonte.clear()
        self.line_edit_textura.clear()
        self.lineEdit_profundidade.clear()

    #Metódos Gerais
    def acessar_principal(self) -> None:
        self.stacked_widget.setCurrentWidget(self.page_principal)

    def acessar_cadastrar(self) -> None:
        self.stacked_widget.setCurrentWidget(self.page_cadastrar)

    def acessar_listar(self) -> None:
        self.stacked_widget.setCurrentWidget(self.page_listar)

    def sair(self) -> None:
        self.stacked_widget.setCurrentWidget(self.page_login)

    def set_label_img(self, label: QLabel, end_img: str):
        img = QPixmap(end_img)
        img = img.scaled(label.width(), label.height(), Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(img)

    def load_imgs(self):
        self.set_label_img(self.label_icone_login, 'img/icone_login.jpg')
        self.set_label_img(self.label_logo_empresa, 'img/icone_login_CLLW.png')
        self.set_label_img(self.label_logo_empresa_2, 'img/icone_login_CLLW.png')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    projeto_perfil_solo_principal = Projeto_perfil_solo_principal()
    projeto_perfil_solo_principal.show()
    qt.exec()
