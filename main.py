from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import system, device


class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.setUI()

        self.setWindowTitle("Linux System Information")
        self.setGeometry(200,200,700,450)
        self.show()

    def setUI(self):
        h = QHBoxLayout()

        spl = QSplitter(Qt.Horizontal)

        s = system.System()
        m = device.Device()

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(s)

        spl.addWidget(self.scroll)
        spl.addWidget(m)

        h.addWidget(spl)
        self.setLayout(h)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Main()
    sys.exit(app.exec())
