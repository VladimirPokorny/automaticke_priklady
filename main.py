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
