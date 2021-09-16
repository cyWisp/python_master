#!/usr/bin/env python
from sys import argv, exit

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

# Dialog
class Dialog(QDialog):
    # Contructor / Initializer
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('QDialog Example')

        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        formLayout.addRow('Name: ', QLineEdit())
        formLayout.addRow('Age: ', QLineEdit())
        formLayout.addRow('Job: ', QLineEdit())
        formLayout.addRow('Hobbies: ', QLineEdit())

        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(argv)
    dlg = Dialog()
    dlg.show()
    exit(app.exec_())