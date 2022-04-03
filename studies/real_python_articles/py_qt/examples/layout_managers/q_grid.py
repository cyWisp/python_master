#!/usr/bin/env python
from sys import argv, exit

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

if __name__ == '__main__':

    app = QApplication(argv)
    window = QWidget()
    window.setWindowTitle('QGridLayout Example')

    layout = QGridLayout()
    layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
    layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
    layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)

    layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
    layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
    layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)

    layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
    layout.addWidget(QPushButton('Button (2, 1) + 2 Column Span'), 2, 1, 1, 2)

    window.setLayout(layout)
    window.show()

    exit(app.exec_())