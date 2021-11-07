# Filename: signals_slots.py

"""Signals and slots example."""

import functools
import sys

from qtpy.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def greeting(who):
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(functools.partial(greeting, "Bro"))  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
