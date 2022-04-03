#!/usr/bin/env python
"""
Simple Hello World example with PyQt5
"""

from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
)

if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(argv)

    # Create an instance of your application's GUI
    window = QWidget()
    window.setWindowTitle("Hello Qt")
    window.setGeometry(100, 100, 280, 80)
    window.move(60, 15)

    hello_msg = QLabel('<h1>Hello, World!</h1>', parent=window)
    hello_msg.move(60, 15)

    # Show your application's GUI
    window.show()

    # Run your application's event loop (or main loop)
    exit(app.exec_())




