from PySide6 import QtWidgets, QtCore


class Splitter(QtWidgets.QSplitter):
    def __init__(self, left_bar, right_bar, parent=None):
        super().__init__()
        self.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.addWidget(left_bar)
        self.addWidget(right_bar)

        self.setSizes([int(self.width() * 0.2), int(self.width() * 0.8)])
        self.setHandleWidth(1)