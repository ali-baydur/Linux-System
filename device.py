from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, platform
from object import Label


class Device(QWidget):

    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        g = QGroupBox("Device Information")
        h = QHBoxLayout()
        f = QFormLayout()

        uname = platform.uname()

        f.addRow(QLabel("System: "), Label(uname.system))
        f.addRow(QLabel("Node Name: "), Label(uname.node))
        f.addRow(QLabel("Release: "), Label(uname.release))
        f.addRow(QLabel("Version: "), Label(uname.version))
        f.addRow(QLabel("Machine: "), Label(uname.machine))
        f.addRow(QLabel("Processor: "), Label(uname.processor))


        g.setLayout(f)
        h.addWidget(g)
        self.setLayout(h)
