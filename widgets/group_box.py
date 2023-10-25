from PySide6 import QtWidgets


class RangeGroupBox(QtWidgets.QGroupBox):
    def __init__(self, range_from: list, range_to: list, parent=None):
        super().__init__('Range', parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.range_from = LabeledSpin('From: ', range_from, parent=self)
        self.layout.addWidget(self.range_from)

        self.range_to = LabeledSpin('To: ', range_to, parent=self)
        self.layout.addWidget(self.range_to)

        self.result_in_range = LabelCheck('Result in range: ', parent=self)
        self.layout.addWidget(self.result_in_range)
        

class LabeledSpin(QtWidgets.QWidget):
    def __init__(self, label: str, spin_range: list, initial_spin_value=0, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel(text=label)
        self.layout.addWidget(self.label)

        self.spin = QtWidgets.QSpinBox()
        self.spin.setRange(*spin_range)
        self.spin.setValue(initial_spin_value)
        self.layout.addWidget(self.spin)


class LabelCheck(QtWidgets.QWidget):
    def __init__(self, label: str, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel(text=label)
        self.layout.addWidget(self.label)

        self.check = QtWidgets.QCheckBox()
        self.check.setChecked(True)
        self.layout.addWidget(self.check)





