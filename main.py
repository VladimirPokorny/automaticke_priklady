import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QVBoxLayout, QPushButton, QWidget
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Addition generator")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a splitter to divide the window into left and right areas
        splitter = QSplitter()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(splitter)

        # Create the left panel (Settings)
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        range = QtWidgets.QGroupBox("Range")
        range_layout = QtWidgets.QVBoxLayout()
        range.setLayout(range_layout)

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



        setting_addition = QtWidgets.QGroupBox("Addition")
        setting_addition_layout = QtWidgets.QVBoxLayout()
        setting_addition.setLayout(setting_addition_layout)

        setting_addition_enable = QtWidgets.QWidget()
        setting_addition_enable_layout = QtWidgets.QHBoxLayout()






        verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        left_layout.addWidget(range)
        left_layout.addItem(verticalSpacer)


        # Create the main content (Right panel)
        main_area = QtWidgets.QWidget()
        main_layout = QVBoxLayout()
        main_area.setLayout(main_layout)

        text_edit = QtWidgets.QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText("There will be the generated addition tasks")

        main_layout.addWidget(text_edit)

        # Add the left panel and main content widgets to the splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(main_area)

        # Set the size policy for the splitter handle to make the left panel 30% of the screen width
        splitter.setSizes([int(self.width() * 0.2), int(self.width() * 0.8)])
        splitter.setHandleWidth(1)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
