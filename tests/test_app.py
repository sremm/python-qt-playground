from qtpy.QtWidgets import QWidget


def test_hello(qtbot):
    widget = QWidget()
    qtbot.addWidget(widget)

    assert True
