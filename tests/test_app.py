from pycalc import PyCalcUi, initiate_mvc
from qtpy.QtCore import Qt


class TestPyCalcUi:
    def test_open_and_close(self, qtbot):
        pycalcUI = PyCalcUi()
        qtbot.addWidget(pycalcUI)

        pycalcUI.show()
        pycalcUI.close()

    def test_add_expression_and_compute_result(self, qtbot):
        view = initiate_mvc()
        qtbot.addWidget(view)

        view.show()

        qtbot.mouseClick(view.buttons["1"], Qt.MouseButton.LeftButton)
        qtbot.mouseClick(view.buttons["+"], Qt.MouseButton.LeftButton)
        qtbot.mouseClick(view.buttons["2"], Qt.MouseButton.LeftButton)
        initial_display_contents = view.displayText()

        qtbot.mouseClick(view.buttons["="], Qt.MouseButton.LeftButton)
        final_display_contents = view.displayText()

        view.close()

        assert initial_display_contents == "1+2"
        assert final_display_contents == "3"
