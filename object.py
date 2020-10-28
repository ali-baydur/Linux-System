from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, clipboard


class Label(QLabel):

    def __init__(self, *argv, **kwargv):
        super().__init__(*argv,**kwargv)

    def mouseDoubleClickEvent(self, event):
        clipboard.copy(self.text())
