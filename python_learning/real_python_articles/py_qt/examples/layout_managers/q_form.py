#!/usr/bin/env python
from sys import argv, exit

from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

if __name__ == '__main__':

    app = QApplication(argv)
    window = QWidget()
    window.setWindowTitle('QFormLayout Example')

    layout = QFormLayout()
    layout.addRow('Name:', QLineEdit())
    layout.addRow('Age:', QLineEdit())
    layout.addRow('Job:', QLineEdit())
    layout.addRow('Hobbies:', QLineEdit())

    window.setLayout(layout)
    window.show()
    exit(app.exec_())