from PySide6 import QtCore, QtWidgets
import config


class MainArea(QtWidgets.QWidget):
    def __init__(self, temperature_graph_view):
        super().__init__()

        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(temperature_graph_view)

    def parent_resized(self, size):
        w_size = self.size()
        self.move(config.panel_size, 0)
        self.setFixedSize(size.width() - config.panel_size, size.height())
