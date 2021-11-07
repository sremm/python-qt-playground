""" A simple qt app largely from https://realpython.com/python-pyqt-gui-calculator/"""

import sys

from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from qtpy.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)


window = QWidget()
window.setWindowTitle("PyQt5 App")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)

vertical_box_layout = QVBoxLayout()

helloMsg = QLabel("<h1>Hello World!</h1>")
helloMsg.move(60, 15)

text_box = QLineEdit()

button = QPushButton()
button.setText("I am a button.")

vertical_box_layout.addWidget(helloMsg)
vertical_box_layout.addWidget(text_box)
vertical_box_layout.addWidget(button)
window.setLayout(vertical_box_layout)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
