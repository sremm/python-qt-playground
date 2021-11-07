""" A simple qt app largely from https://realpython.com/python-pyqt-gui-calculator/"""

import sys

from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from qtpy.QtWidgets import QApplication, QLabel, QWidget


class MainWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5 App")
        self.setGeometry(100, 100, 280, 80)
        self.move(60, 15)

        vertical_box_layout = QVBoxLayout()

        helloMsg = QLabel("<h1>Hello World!</h1>")
        helloMsg.move(60, 15)

        text_box = QLineEdit()

        button = QPushButton()
        button.setText("I am a button.")

        vertical_box_layout.addWidget(helloMsg)
        vertical_box_layout.addWidget(text_box)
        vertical_box_layout.addWidget(button)
        self.setLayout(vertical_box_layout)

        # Show your application's GUI
        self.show()


def main():
    app = QApplication(sys.argv)

    main_widget = MainWidget()
    # Run your application's event loop (or main loop)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
