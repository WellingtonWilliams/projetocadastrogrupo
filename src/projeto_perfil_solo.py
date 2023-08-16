# Form implementation generated from reading ui file 'projeto_perfil_solo.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_widget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stacked_widget.setGeometry(QtCore.QRect(20, 10, 781, 551))
        self.stacked_widget.setObjectName("stacked_widget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.frame_login_fundo = QtWidgets.QFrame(parent=self.page_login)
        self.frame_login_fundo.setGeometry(QtCore.QRect(40, 80, 651, 351))
        self.frame_login_fundo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_login_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login_fundo.setObjectName("frame_login_fundo")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_login_fundo)
        self.gridLayout.setObjectName("gridLayout")
        self.label_incone_login = QtWidgets.QLabel(parent=self.frame_login_fundo)
        self.label_incone_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_incone_login.setObjectName("label_incone_login")
        self.gridLayout.addWidget(self.label_incone_login, 0, 1, 1, 1)
        self.line_edit_inserir_login = QtWidgets.QLineEdit(parent=self.frame_login_fundo)
        self.line_edit_inserir_login.setMinimumSize(QtCore.QSize(0, 0))
        self.line_edit_inserir_login.setText("")
        self.line_edit_inserir_login.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.line_edit_inserir_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_inserir_login.setObjectName("line_edit_inserir_login")
        self.gridLayout.addWidget(self.line_edit_inserir_login, 1, 1, 1, 1)
        self.line_edit_inserir_senha = QtWidgets.QLineEdit(parent=self.frame_login_fundo)
        self.line_edit_inserir_senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.line_edit_inserir_senha.setCursorPosition(0)
        self.line_edit_inserir_senha.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_inserir_senha.setObjectName("line_edit_inserir_senha")
        self.gridLayout.addWidget(self.line_edit_inserir_senha, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.push_button_entrar = QtWidgets.QPushButton(parent=self.frame_login_fundo)
        self.push_button_entrar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_entrar.setObjectName("push_button_entrar")
        self.gridLayout.addWidget(self.push_button_entrar, 4, 1, 1, 1)
        self.frame_msg_erro = QtWidgets.QFrame(parent=self.frame_login_fundo)
        self.frame_msg_erro.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg_erro.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg_erro.setObjectName("frame_msg_erro")
        self.push_button_fecha_msg_erro = QtWidgets.QPushButton(parent=self.frame_msg_erro)
        self.push_button_fecha_msg_erro.setGeometry(QtCore.QRect(530, 40, 40, 25))
        self.push_button_fecha_msg_erro.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_fecha_msg_erro.setObjectName("push_button_fecha_msg_erro")
        self.label_msg_erro = QtWidgets.QLabel(parent=self.frame_msg_erro)
        self.label_msg_erro.setGeometry(QtCore.QRect(60, 40, 451, 25))
        self.label_msg_erro.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_msg_erro.setObjectName("label_msg_erro")
        self.gridLayout.addWidget(self.frame_msg_erro, 3, 0, 1, 3)
        self.stacked_widget.addWidget(self.page_login)
        self.page_principal = QtWidgets.QWidget()
        self.page_principal.setObjectName("page_principal")
        self.frame_fundo_principal = QtWidgets.QFrame(parent=self.page_principal)
        self.frame_fundo_principal.setGeometry(QtCore.QRect(0, 19, 761, 511))
        self.frame_fundo_principal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_fundo_principal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_fundo_principal.setObjectName("frame_fundo_principal")
        self.label_logo_empresa = QtWidgets.QLabel(parent=self.frame_fundo_principal)
        self.label_logo_empresa.setGeometry(QtCore.QRect(50, 60, 100, 100))
        self.label_logo_empresa.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo_empresa.setObjectName("label_logo_empresa")
        self.label_descricao = QtWidgets.QLabel(parent=self.frame_fundo_principal)
        self.label_descricao.setGeometry(QtCore.QRect(10, 170, 151, 61))
        self.label_descricao.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_descricao.setObjectName("label_descricao")
        self.push_button_cadastrar = QtWidgets.QPushButton(parent=self.frame_fundo_principal)
        self.push_button_cadastrar.setGeometry(QtCore.QRect(260, 160, 90, 40))
        self.push_button_cadastrar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_cadastrar.setObjectName("push_button_cadastrar")
        self.push_button_listar = QtWidgets.QPushButton(parent=self.frame_fundo_principal)
        self.push_button_listar.setGeometry(QtCore.QRect(390, 160, 90, 40))
        self.push_button_listar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_listar.setObjectName("push_button_listar")
        self.push_button_sair = QtWidgets.QPushButton(parent=self.frame_fundo_principal)
        self.push_button_sair.setGeometry(QtCore.QRect(520, 160, 90, 40))
        self.push_button_sair.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_sair.setObjectName("push_button_sair")
        self.stacked_widget.addWidget(self.page_principal)
        self.page_cadastrar = QtWidgets.QWidget()
        self.page_cadastrar.setObjectName("page_cadastrar")
        self.frame_cadastrar_fundo = QtWidgets.QFrame(parent=self.page_cadastrar)
        self.frame_cadastrar_fundo.setGeometry(QtCore.QRect(0, 20, 761, 511))
        self.frame_cadastrar_fundo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastrar_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastrar_fundo.setObjectName("frame_cadastrar_fundo")
        self.label_logo_empresa_2 = QtWidgets.QLabel(parent=self.frame_cadastrar_fundo)
        self.label_logo_empresa_2.setGeometry(QtCore.QRect(70, 40, 100, 100))
        self.label_logo_empresa_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo_empresa_2.setObjectName("label_logo_empresa_2")
        self.frame_msg_cadastro_invalido = QtWidgets.QFrame(parent=self.frame_cadastrar_fundo)
        self.frame_msg_cadastro_invalido.setGeometry(QtCore.QRect(180, 40, 551, 91))
        self.frame_msg_cadastro_invalido.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_msg_cadastro_invalido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_msg_cadastro_invalido.setObjectName("frame_msg_cadastro_invalido")
        self.label_mes_erro_cadastro = QtWidgets.QLabel(parent=self.frame_msg_cadastro_invalido)
        self.label_mes_erro_cadastro.setGeometry(QtCore.QRect(30, 30, 441, 25))
        self.label_mes_erro_cadastro.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_mes_erro_cadastro.setObjectName("label_mes_erro_cadastro")
        self.push_button_fechar_msg_cadastro_invalido = QtWidgets.QPushButton(parent=self.frame_msg_cadastro_invalido)
        self.push_button_fechar_msg_cadastro_invalido.setGeometry(QtCore.QRect(480, 30, 40, 25))
        self.push_button_fechar_msg_cadastro_invalido.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_fechar_msg_cadastro_invalido.setObjectName("push_button_fechar_msg_cadastro_invalido")
        self.push_button_salvar = QtWidgets.QPushButton(parent=self.frame_cadastrar_fundo)
        self.push_button_salvar.setGeometry(QtCore.QRect(280, 430, 80, 30))
        self.push_button_salvar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_salvar.setObjectName("push_button_salvar")
        self.push_button_voltar = QtWidgets.QPushButton(parent=self.frame_cadastrar_fundo)
        self.push_button_voltar.setGeometry(QtCore.QRect(390, 430, 80, 30))
        self.push_button_voltar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_voltar.setObjectName("push_button_voltar")
        self.frame_cadastro_itens = QtWidgets.QFrame(parent=self.frame_cadastrar_fundo)
        self.frame_cadastro_itens.setGeometry(QtCore.QRect(20, 169, 721, 251))
        self.frame_cadastro_itens.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_cadastro_itens.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_cadastro_itens.setObjectName("frame_cadastro_itens")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.frame_cadastro_itens)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 29, 681, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_layout_itens = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_layout_itens.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_itens.setObjectName("grid_layout_itens")
        self.label_textura = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_textura.setObjectName("label_textura")
        self.grid_layout_itens.addWidget(self.label_textura, 2, 2, 1, 1)
        self.label_codigo_servico = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_codigo_servico.setObjectName("label_codigo_servico")
        self.grid_layout_itens.addWidget(self.label_codigo_servico, 0, 0, 1, 1)
        self.label_localizacao_area = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_localizacao_area.setObjectName("label_localizacao_area")
        self.grid_layout_itens.addWidget(self.label_localizacao_area, 0, 2, 1, 1)
        self.label_horizonte = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_horizonte.setObjectName("label_horizonte")
        self.grid_layout_itens.addWidget(self.label_horizonte, 1, 2, 1, 1)
        self.combo_box_tipo_solo = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.combo_box_tipo_solo.setObjectName("combo_box_tipo_solo")
        self.combo_box_tipo_solo.addItem("")
        self.combo_box_tipo_solo.addItem("")
        self.combo_box_tipo_solo.addItem("")
        self.combo_box_tipo_solo.addItem("")
        self.combo_box_tipo_solo.addItem("")
        self.grid_layout_itens.addWidget(self.combo_box_tipo_solo, 1, 1, 1, 1)
        self.label_cor = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_cor.setObjectName("label_cor")
        self.grid_layout_itens.addWidget(self.label_cor, 2, 0, 1, 1)
        self.label_tipo_solo = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_tipo_solo.setObjectName("label_tipo_solo")
        self.grid_layout_itens.addWidget(self.label_tipo_solo, 1, 0, 1, 1)
        self.label_estrutura = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_estrutura.setObjectName("label_estrutura")
        self.grid_layout_itens.addWidget(self.label_estrutura, 3, 0, 1, 1)
        self.label_profundidade = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_profundidade.setObjectName("label_profundidade")
        self.grid_layout_itens.addWidget(self.label_profundidade, 3, 2, 1, 1)
        self.line_edit_localizacao_area = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_localizacao_area.setObjectName("line_edit_localizacao_area")
        self.grid_layout_itens.addWidget(self.line_edit_localizacao_area, 0, 3, 1, 1)
        self.line_edit_codigo_servio = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_codigo_servio.setObjectName("line_edit_codigo_servio")
        self.grid_layout_itens.addWidget(self.line_edit_codigo_servio, 0, 1, 1, 1)
        self.line_edit_textura = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_textura.setObjectName("line_edit_textura")
        self.grid_layout_itens.addWidget(self.line_edit_textura, 2, 3, 1, 1)
        self.line_edit_cor = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_cor.setObjectName("line_edit_cor")
        self.grid_layout_itens.addWidget(self.line_edit_cor, 2, 1, 1, 1)
        self.line_edit_estrutura = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.line_edit_estrutura.setObjectName("line_edit_estrutura")
        self.grid_layout_itens.addWidget(self.line_edit_estrutura, 3, 1, 1, 1)
        self.lineEdit_profundidade = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_profundidade.setObjectName("lineEdit_profundidade")
        self.grid_layout_itens.addWidget(self.lineEdit_profundidade, 3, 3, 1, 1)
        self.lineEdit_horizonte = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_horizonte.setObjectName("lineEdit_horizonte")
        self.grid_layout_itens.addWidget(self.lineEdit_horizonte, 1, 3, 1, 1)
        self.stacked_widget.addWidget(self.page_cadastrar)
        self.page_listar = QtWidgets.QWidget()
        self.page_listar.setObjectName("page_listar")
        self.frame_listar_fundo = QtWidgets.QFrame(parent=self.page_listar)
        self.frame_listar_fundo.setGeometry(QtCore.QRect(10, 20, 591, 511))
        self.frame_listar_fundo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_listar_fundo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_listar_fundo.setObjectName("frame_listar_fundo")
        self.table_widget_itens = QtWidgets.QTableWidget(parent=self.frame_listar_fundo)
        self.table_widget_itens.setGeometry(QtCore.QRect(5, 11, 581, 491))
        self.table_widget_itens.setObjectName("table_widget_itens")
        self.table_widget_itens.setColumnCount(8)
        self.table_widget_itens.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_itens.setHorizontalHeaderItem(7, item)
        self.frame_buttons = QtWidgets.QFrame(parent=self.page_listar)
        self.frame_buttons.setGeometry(QtCore.QRect(619, 29, 131, 491))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setObjectName("verticalLayout")
        self.push_button_alterar = QtWidgets.QPushButton(parent=self.frame_buttons)
        self.push_button_alterar.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_alterar.setObjectName("push_button_alterar")
        self.verticalLayout.addWidget(self.push_button_alterar)
        self.push_button_excluir = QtWidgets.QPushButton(parent=self.frame_buttons)
        self.push_button_excluir.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_excluir.setObjectName("push_button_excluir")
        self.verticalLayout.addWidget(self.push_button_excluir)
        self.push_button_voltar_2 = QtWidgets.QPushButton(parent=self.frame_buttons)
        self.push_button_voltar_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.push_button_voltar_2.setObjectName("push_button_voltar_2")
        self.verticalLayout.addWidget(self.push_button_voltar_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.stacked_widget.addWidget(self.page_listar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_incone_login.setText(_translate("MainWindow", "Incine_login"))
        self.line_edit_inserir_login.setPlaceholderText(_translate("MainWindow", "Digite seu login"))
        self.line_edit_inserir_senha.setPlaceholderText(_translate("MainWindow", "Digite sua senha"))
        self.push_button_entrar.setText(_translate("MainWindow", "ENTRAR"))
        self.push_button_fecha_msg_erro.setText(_translate("MainWindow", "X"))
        self.label_msg_erro.setText(_translate("MainWindow", " Login ou senha invalidos!!!"))
        self.label_logo_empresa.setText(_translate("MainWindow", " Logo_empresa"))
        self.label_descricao.setText(_translate("MainWindow", "Descrição_empresa"))
        self.push_button_cadastrar.setText(_translate("MainWindow", " Cadastrar"))
        self.push_button_listar.setText(_translate("MainWindow", "Listar"))
        self.push_button_sair.setText(_translate("MainWindow", "Sair"))
        self.label_logo_empresa_2.setText(_translate("MainWindow", " Logo_empresa"))
        self.label_mes_erro_cadastro.setText(_translate("MainWindow", " Cadastro inválido!!!"))
        self.push_button_fechar_msg_cadastro_invalido.setText(_translate("MainWindow", "X"))
        self.push_button_salvar.setText(_translate("MainWindow", "Salvar"))
        self.push_button_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_textura.setText(_translate("MainWindow", " Textura:"))
        self.label_codigo_servico.setText(_translate("MainWindow", " Codigo de serviço:"))
        self.label_localizacao_area.setText(_translate("MainWindow", "Localização/área:"))
        self.label_horizonte.setText(_translate("MainWindow", " Horizonte:"))
        self.combo_box_tipo_solo.setItemText(0, _translate("MainWindow", "-"))
        self.combo_box_tipo_solo.setItemText(1, _translate("MainWindow", "Argiloso"))
        self.combo_box_tipo_solo.setItemText(2, _translate("MainWindow", "Arenoso"))
        self.combo_box_tipo_solo.setItemText(3, _translate("MainWindow", "Calcário"))
        self.combo_box_tipo_solo.setItemText(4, _translate("MainWindow", "Humoso"))
        self.label_cor.setText(_translate("MainWindow", " Cor:"))
        self.label_tipo_solo.setText(_translate("MainWindow", " Tipo de solo:"))
        self.label_estrutura.setText(_translate("MainWindow", " Estrutura:"))
        self.label_profundidade.setText(_translate("MainWindow", " Profundidade (m/cm):"))
        item = self.table_widget_itens.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "01"))
        item = self.table_widget_itens.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "02"))
        item = self.table_widget_itens.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "03"))
        item = self.table_widget_itens.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "04"))
        item = self.table_widget_itens.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "04"))
        item = self.table_widget_itens.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "06"))
        item = self.table_widget_itens.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "07"))
        item = self.table_widget_itens.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "08"))
        item = self.table_widget_itens.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "09"))
        item = self.table_widget_itens.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "10"))
        item = self.table_widget_itens.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "11"))
        item = self.table_widget_itens.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "12"))
        item = self.table_widget_itens.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "13"))
        item = self.table_widget_itens.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "14"))
        item = self.table_widget_itens.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "15"))
        item = self.table_widget_itens.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "16"))
        item = self.table_widget_itens.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "17"))
        item = self.table_widget_itens.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "18"))
        item = self.table_widget_itens.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "19"))
        item = self.table_widget_itens.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "20"))
        item = self.table_widget_itens.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", " Codigo de serviço"))
        item = self.table_widget_itens.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", " Localização/área"))
        item = self.table_widget_itens.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", " Tipos de solo"))
        item = self.table_widget_itens.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", " Horizonte"))
        item = self.table_widget_itens.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", " Cor"))
        item = self.table_widget_itens.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", " Textura"))
        item = self.table_widget_itens.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", " Estrutura"))
        item = self.table_widget_itens.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", " Profud. (m/cm)"))
        self.push_button_alterar.setText(_translate("MainWindow", "Alterar"))
        self.push_button_excluir.setText(_translate("MainWindow", "Excluir"))
        self.push_button_voltar_2.setText(_translate("MainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())