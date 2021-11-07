""" A simple qt app largely from https://realpython.com/python-pyqt-gui-calculator/"""

import sys

from qtpy.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)
# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle("PyQt5 App")
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel("<h1>Hello World!</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())
