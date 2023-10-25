import sys
from PySide6 import QtWidgets
from widgets import splitter, group_box, output_editor
from example_generator import example_generator


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Addition generator")
        self.setGeometry(100, 100, 800, 600)

        self.addition_configuration = example_generator.AdditionConfiguration()
        self.subtraction_configuration = example_generator.SubtractionConfiguration()
        self.example_configuration = example_generator.ExampleConfiguration()
        self.generator = example_generator.Generator(self.example_configuration, 
                                                     self.addition_configuration, 
                                                     self.subtraction_configuration,
                                                     parent=self)

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(QtWidgets.QVBoxLayout())

        self.left_panel = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_panel.setLayout(self.left_layout)

        self.range_group_box = group_box.RangeGroupBox([0, 50], [0, 50], parent=self)
        self.range_group_box.update_configuration()
        self.left_layout.addWidget(self.range_group_box)

        self.example_generator_box = group_box.ExampleGeneratorBox(parent=self)
        self.example_generator_box.update_configuration()
        self.left_layout.addWidget(self.example_generator_box)

        self.generator_button = QtWidgets.QPushButton('Generate', self)
        self.generator_button.clicked.connect(self.generator.generate_and_update_view)
        self.left_layout.addWidget(self.generator_button)

        verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_layout.addItem(verticalSpacer)

        self.main_area = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_area.setLayout(self.main_layout)

        self.text_edit = output_editor.OutputTextEdit(parent=self)
        self.main_layout.addWidget(self.text_edit)       

        self.splitter = splitter.Splitter(self.left_panel, self.main_area, parent=self)
        self.central_widget.layout().addWidget(self.splitter)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
