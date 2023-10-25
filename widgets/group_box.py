from PySide6 import QtWidgets


class RangeGroupBox(QtWidgets.QGroupBox):
    def __init__(self, range_from: list, range_to: list, parent=None):
        super().__init__('Range')
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.range_from = LabeledSpin('From: ', range_from, initial_spin_value=0, parent=self)
        self.range_from.spin.valueChanged.connect(self.update_configuration)
        self.layout.addWidget(self.range_from)

        self.range_to = LabeledSpin('To: ', range_to, initial_spin_value=30, parent=self)
        self.range_to.spin.valueChanged.connect(self.update_configuration)
        self.layout.addWidget(self.range_to)

        self.result_in_range = LabelCheck('Result in range: ', parent=self)
        self.result_in_range.check.stateChanged.connect(self.update_configuration)
        self.layout.addWidget(self.result_in_range)
    
    def update_configuration(self):
        range_from = self.range_from.spin.value()
        range_to = self.range_to.spin.value()
        result_in_range = self.result_in_range.check.isChecked()
        
        self.parent.addition_configuration.number_range = [range_from, range_to]
        self.parent.addition_configuration.result_in_range = result_in_range


class ExampleGeneratorBox(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super().__init__('Example generator settings')
        self.parent = parent

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.number_of_exercises_in_column = LabeledSpin('Number of exercises in column: ', [0, 100], 
                                                         initial_spin_value=5, parent=self)
        self.number_of_exercises_in_column.spin.valueChanged.connect(self.update_configuration)
        self.layout.addWidget(self.number_of_exercises_in_column)

        self.number_of_columns = LabeledSpin('Number of columns: ', [0, 100], initial_spin_value=4, parent=self)
        self.number_of_columns.spin.valueChanged.connect(self.update_configuration)
        self.layout.addWidget(self.number_of_columns)

        self.show_results = LabelCheck('Show result: ', parent=self)
        self.show_results.check.stateChanged.connect(self.update_configuration)
        self.layout.addWidget(self.show_results)


    def update_configuration(self):
        """
        Updates the configuration of the example generator
        """
        number_of_exercises_in_column = self.number_of_exercises_in_column.spin.value()
        number_of_columns = self.number_of_columns.spin.value()
        show_results = self.show_results.check.isChecked()

        self.parent.example_configuration.number_of_exercises_in_column = number_of_exercises_in_column
        self.parent.example_configuration.number_of_columns = number_of_columns
        self.parent.example_configuration.show_results = show_results


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





