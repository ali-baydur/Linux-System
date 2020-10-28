from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, os
from object import Label

class System(QWidget):

    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        g = QGroupBox("System Information")
        h = QHBoxLayout()
        f = QFormLayout()

        for i in os.environ:
            f.addRow(QLabel(i+": "), Label(os.environ[i]))



        g.setLayout(f)
        h.addWidget(g)
        self.setLayout(h)
