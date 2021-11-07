from pycalc import PyCalcCtrl, PyCalcUi
from qtpy.QtCore import Qt


class TestPyCalcUi:
    def test_open_and_close(self, qtbot):
        pycalcUI = PyCalcUi()
        qtbot.addWidget(pycalcUI)

        pycalcUI.show()
        pycalcUI.close()

    def test_add_expression_and_read_display(self, qtbot):
        pycalcUI = PyCalcUi()
        qtbot.addWidget(pycalcUI)

        PyCalcCtrl(view=pycalcUI)

        qtbot.mouseClick(pycalcUI.buttons["1"], Qt.MouseButton.LeftButton)
        qtbot.mouseClick(pycalcUI.buttons["+"], Qt.MouseButton.LeftButton)
        qtbot.mouseClick(pycalcUI.buttons["2"], Qt.MouseButton.LeftButton)

        display_contents = pycalcUI.displayText()

        pycalcUI.show()
        pycalcUI.close()

        assert display_contents == "1+2"
