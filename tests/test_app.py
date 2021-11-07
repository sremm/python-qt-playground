from pycalc import PyCalcUi


class TestPyCalcUi:
    def test_open_and_close(self, qtbot):
        pycalcUI = PyCalcUi()
        qtbot.addWidget(pycalcUI)

        pycalcUI.show()
        pycalcUI.close()
