#!/usr/bin/env python
"""
Vertical layout example
"""
from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

if __name__ == '__main__':
    app = QApplication(argv)
    window = QWidget()
    window.setWindowTitle('QVBox Layout Example')

    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Center'))
    layout.addWidget(QPushButton('Bottom'))

    window.setLayout(layout)
    window.show()
    exit(app.exec_())