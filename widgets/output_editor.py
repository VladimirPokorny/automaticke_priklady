from PySide6 import QtWidgets


class OutputTextEdit(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.setReadOnly(True)
        self.setText("There will be the generated addition tasks")

    def update_text(self, text):
        self.setText(text)
