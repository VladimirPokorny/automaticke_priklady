import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QVBoxLayout, QPushButton, QWidget
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt

from widgets import splitter, group_box



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Addition generator")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.left_panel = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_panel.setLayout(self.left_layout)

        self.range_group_box = group_box.RangeGroupBox([0, 30], [0,30], parent=self)
        self.left_layout.addWidget(self.range_group_box)

        

        # Create a splitter to divide the window into left and right areas
        self.splitter = splitter.Splitter(self.left_panel, QtWidgets.QWidget(), parent=self)
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(self.splitter)

        # Create the left panel (Settings)


        # range = QtWidgets.QGroupBox("Range")
        # range_layout = QtWidgets.QVBoxLayout()
        # range.setLayout(range_layout)

        # range_from_widget = QtWidgets.QWidget()
        # range_from_layout = QtWidgets.QHBoxLayout()
        # range_from_widget.setLayout(range_from_layout)

        # range_from_label = QtWidgets.QLabel("From: ")
        # range_from = QtWidgets.QSpinBox()
        # range_from.setValue(0)
        # range_from_layout.addWidget(range_from_label)
        # range_from_layout.addWidget(range_from)

        # range_to_widget = QtWidgets.QWidget()
        # range_to_layout = QtWidgets.QHBoxLayout()
        # range_to_widget.setLayout(range_to_layout)

        # range_to_label = QtWidgets.QLabel("To: ")
        # range_to = QtWidgets.QSpinBox()
        # range_to.setValue(30)
        # range_to_layout.addWidget(range_to_label)
        # range_to_layout.addWidget(range_to)
        
        # range_layout.addWidget(range_from_widget)
        # range_layout.addWidget(range_to_widget)



        # setting_addition = QtWidgets.QGroupBox("Addition")
        # setting_addition_layout = QtWidgets.QVBoxLayout()
        # setting_addition.setLayout(setting_addition_layout)

        # setting_addition_enable = QtWidgets.QWidget()
        # setting_addition_enable_layout = QtWidgets.QHBoxLayout()






        verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_layout.addItem(verticalSpacer)


        # Create the main content (Right panel)
        main_area = QtWidgets.QWidget()
        main_layout = QVBoxLayout()
        main_area.setLayout(main_layout)

        text_edit = QtWidgets.QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText("There will be the generated addition tasks")

        main_layout.addWidget(text_edit)

        # Add the left panel and main content widgets to the splitter
        # splitter.addWidget(left_panel)
        # splitter.addWidget(main_area)

        # Set the size policy for the splitter handle to make the left panel 30% of the screen width
        # splitter.setSizes([int(self.width() * 0.2), int(self.width() * 0.8)])
        # splitter.setHandleWidth(1)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
