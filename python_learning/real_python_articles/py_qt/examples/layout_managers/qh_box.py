#!/usr/bin/env python
"""
Horizontal layout example
"""

from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget
)

if __name__ == '__main__':
    app = QApplication(argv)
    window = QWidget()
    window.setWindowTitle('QHBox Layout Example')

    layout = QHBoxLayout()
    layout.addWidget(QPushButton('Left'))
    layout.addWidget(QPushButton('Center'))
    layout.addWidget(QPushButton('Righ'))

    window.setLayout(layout)
    window.show()
    exit(app.exec_())