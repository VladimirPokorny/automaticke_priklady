from ..elements import buttons
from . import base
from style import images_dir
from PySide6 import QtWidgets


class ExampleConfiguration(base.Toolbar):
    def __init__(self, main_window):
        super().__init__('example configuration', images_dir + "section_icons/stem_tools.svg")
        self.main_window = main_window
        
        example_types = ['addition', 'subtraction', 'multiplication', 'division']

        self.configuration = {}

        for i in range(len(example_types)):
            self.configuration[example_types[i]] = {}

            expand_button = buttons.ToolbarPushButton(example_types[i].upper())
            expand_button.setStyleSheet("background-color: #d14a2e;")
            expand_button.example_type = example_types[i]
            expand_button.clicked.connect(self.expand_options)
            self.configuration[example_types[i]]['expand_button'] = expand_button

            type_options = AdditionConfiguration(self)
            type_options.setVisible(True)
            self.configuration[example_types[i]]['options'] = type_options

            self.content.layout().addWidget(expand_button, i * 2, 0, 1, 8)
            self.content.layout().addWidget(type_options, i * 2 + 1, 0, 1, 8)

    def expand_options(self):
        button = self.sender()
        example_type = button.example_type
        options = self.configuration[example_type]['options']
        options.setVisible(not options.isVisible())

        self.adjustSize()

    def update_button_color(self):
        for example_type in self.configuration.keys():
            if self.configuration[example_type]['options'].labels['enable'].isChecked():
                self.configuration[example_type]['expand_button'].setStyleSheet("background-color: green;")
            else:
                self.configuration[example_type]['expand_button'].setStyleSheet("background-color: #d14a2e;")

    def delete_data(self):
        pass

    def measure_manager(self, button):
        pass


class AdditionConfiguration(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.labels = {}

        layout = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QLabel()
        widget.setText("Enable")
        layout.addWidget(widget)

        widget = QtWidgets.QCheckBox()
        widget.setChecked(False)
        widget.name = 'addition'
        widget.stateChanged.connect(parent.update_button_color)

        layout.addWidget(widget)
        self.layout().addLayout(layout)
        self.labels["enable"] = widget

        self.options = {
            'rozsah': {
                'od': 0,
                'do': 30
            },
            'pocet_prikladu': 10,
        }

        layout = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QLabel()
        widget.setText("Range: ")
        layout.addWidget(widget)
        self.layout().addLayout(layout)

        layout = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QLabel()
        widget.setText("From")
        layout.addWidget(widget)

        widget = QtWidgets.QSpinBox()
        widget.setValue(0)
        layout.addWidget(widget)

        widget = QtWidgets.QLabel()
        widget.setText("To")
        layout.addWidget(widget)

        widget = QtWidgets.QSpinBox()
        widget.setValue(30)
        layout.addWidget(widget)
        self.layout().addLayout(layout)

        layout = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QLabel()
        widget.setText("Number of examples: ")
        layout.addWidget(widget)

        widget = QtWidgets.QSpinBox()
        widget.setValue(10)
        layout.addWidget(widget)
        
        self.layout().addLayout(layout)



        


        # for name, option in self.options.items():
        #     layout = QtWidgets.QHBoxLayout()

        #     widget = QtWidgets.QLabel()
        #     widget.setText(option[0])
        #     layout.addWidget(widget)

        #     widget = QtWidgets.QComboBox()
        #     for key in option[1].keys():
        #         widget.addItem(key, option[1][key])
        #     widget.currentIndexChanged.connect(self.parent.combobox_updated)
        #     layout.addWidget(widget)

        #     self.layout().addLayout(layout)
        #     self.labels[name] = widget
