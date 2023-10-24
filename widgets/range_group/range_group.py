from PySide6 import QtWidgets


class RangeGroup(QtWidgets.QGroupBox):
    def __init__(self):
        super().__init__("Range")

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        range_from_widget = QtWidgets.QWidget()
        range_from_layout = QtWidgets.QHBoxLayout()
        range_from_widget.setLayout(range_from_layout)

        range_from_label = QtWidgets.QLabel("From: ")
        range_from = QtWidgets.QSpinBox()
        range_from.setValue(0)
        

        range_from_widget = QtWidgets.QWidget()
        range_from_layout = QtWidgets.QHBoxLayout()
        range_from_widget.setLayout(range_from_layout)

        range_from_label = QtWidgets.QLabel("From: ")
        range_from = QtWidgets.QSpinBox()
        range_from.setValue(0)
        range_from_layout.addWidget(range_from_label)
        range_from_layout.addWidget(range_from)

        range_to_widget = QtWidgets.QWidget()
        range_to_layout = QtWidgets.QHBoxLayout()
        range_to_widget.setLayout(range_to_layout)

        range_to_label = QtWidgets.QLabel("To: ")
        range_to = QtWidgets.QSpinBox()
        range_to.setValue(30)
        range_to_layout.addWidget(range_to_label)
        range_to_layout.addWidget(range_to)

        range_layout.addWidget(range_from_widget)
        range_layout.addWidget(range_to_widget)