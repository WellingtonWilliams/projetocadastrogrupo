import sys
import typing

from PyQt6 import QtCore

from projeto_perfil_solo import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget

class projeto_perfil_solo_principal(Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent = None) -> Nome:
        super().__init__(parent)
        super().setupUi(self)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    projeto_perfil_solo_principal = projeto_perfil_solo_principal()
    projeto_perfil_solo_principal.show
    qt.exec()
       