from pycalc import PyCalcCtrl, PyCalcUi, evaluateExpression
from qtpy.QtCore import Qt


class TestPyCalcUi:
    def test_open_and_close(self, qtbot):
        pycalcUI = PyCalcUi()
        qtbot.addWidget(pycalcUI)

        pycalcUI.show()
        pycalcUI.close()

    def test_add_expression_and_compute_result(self, qtbot):
        pycalcUI = PyCalcUi()
        qtbot.addWidget(pycalcUI)

        PyCalcCtrl(view=pycalcUI, model=evaluateExpression)

        pycalcUI.show()

        qtbot.mouseClick(pycalcUI.buttons["1"], Qt.MouseButton.LeftButton)
        qtbot.mouseClick(pycalcUI.buttons["+"], Qt.MouseButton.LeftButton)
        qtbot.mouseClick(pycalcUI.buttons["2"], Qt.MouseButton.LeftButton)
        initial_display_contents = pycalcUI.displayText()

        qtbot.mouseClick(pycalcUI.buttons["="], Qt.MouseButton.LeftButton)
        final_display_contents = pycalcUI.displayText()

        pycalcUI.close()

        assert initial_display_contents == "1+2"
        assert final_display_contents == "3"
