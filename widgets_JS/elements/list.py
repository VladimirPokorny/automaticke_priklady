from PySide6 import QtWidgets, QtCore, QtGui


class ToolbarVerticalList(QtWidgets.QWidget):
    def __init__(self, options):
        super().__init__()

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.options = options
        self.labels = {}

        for name, option in self.options.items():
            layout = QtWidgets.QHBoxLayout()

            widget = QtWidgets.QLabel()
            widget.setText(option[0])
            layout.addWidget(widget)

            widget = QtWidgets.QComboBox()
            widget.addItems(option[1])
            layout.addWidget(widget)

            self.layout().addLayout(layout)
            self.labels[name] = widget
