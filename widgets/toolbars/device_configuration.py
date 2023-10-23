from PySide6 import QtWidgets

from ..elements import buttons
from . import base
from style import images_dir


class DeviceConfiguration(base.Toolbar):
    def __init__(self, main_window):
        super().__init__("DEVICE CONFIGURATION", images_dir + "section_icons/stem_tools.svg")
        self.main_window = main_window
        number_of_channels = main_window.number_of_channels

        self.channels = {}
        self.buttons = []
        self.color_buttons = []

        channel_type = {
            'Voltage': AiChanType.VOLTAGE,
            'Temperature': AiChanType.TC
        }

        channel_mode = {
            'Differential': AnalogInputMode.DIFFERENTIAL,
            'Single-Ended': AnalogInputMode.SINGLE_ENDED
        }

        channel_range = {
            '±10 V': ULRange.BIP10VOLTS,
            '±5 V': ULRange.BIP5VOLTS,
            '±2.5 V': ULRange.BIP2PT5VOLTS,
            '± 1.25 V': ULRange.BIP1PT25VOLTS,
            '± 0.625 V': ULRange.BIPPT625VOLTS,
            '± 0.313 V': ULRange.BIPPT312VOLTS,
            '± 0.156 V': ULRange.BIPPT156VOLTS,
            '± 0.078 V': ULRange.BIPPT078VOLTS
        }

        channel_tc_type = {
            'J': TcType.J,
            'K': TcType.K,
            'T': TcType.T,
            'E': TcType.E,
            'R': TcType.R,
            'S': TcType.S,
            'B': TcType.B,
            'N': TcType.N
        }

        channel_tc_scale = {
            'Celsius': TempScale.CELSIUS,
            'Fahrenheit': TempScale.FAHRENHEIT,
            'Kelvin': TempScale.KELVIN
        }

        inform_options = {
            "channel_type": ('Channel Type', channel_type),
            "channel_mode": ('Mhannel Mode', channel_mode),
            "channel_range": ('Channel Range', channel_range),
            "channel_tc_type": ('Termocouple Type', channel_tc_type),
            "channel_tc_scale": ('Termocouple Scale', channel_tc_scale)
        }

        for i in range(number_of_channels):
            self.channels[i] = {}

            channel_button = buttons.ToolbarPushButton('CHANNEL ' + str(i))
            channel_button.setStyleSheet("background-color: #d14a2e;")
            channel_button.number = i
            channel_button.clicked.connect(self.expand_options)
            self.channels[i]['channel_button'] = channel_button

            color_button = buttons.ToolbarPushButton('')
            color_button.setStyleSheet(f"background-color: {self.main_window.default_colors[i]};")
            color_button.number = i
            color_button.clicked.connect(self.change_color)
            self.channels[i]['color_button'] = color_button

            channel_options = ToolbarVerticalChannelConfiguration(inform_options, self)
            channel_options.setVisible(False)
            self.channels[i]['channel_options'] = channel_options

            self.content.layout().addWidget(color_button, i * 2, 7, 1, 1)
            self.content.layout().addWidget(channel_button, i * 2, 0, 1, 7)
            self.content.layout().addWidget(channel_options, i * 2 + 1, 0, 1, 8)

    def expand_options(self):
        button = self.sender()
        number = button.number
        options = self.channels[number]['channel_options']

        options.setVisible(not options.isVisible())
        self.adjustSize()

    def update_button_color(self):
        for i in range(len(self.channels)):
            if self.channels[i]['channel_options'].labels['enable'].isChecked():
                self.channels[i]['channel_button'].setStyleSheet("background-color: green;")
            else:
                self.channels[i]['channel_button'].setStyleSheet("background-color: #d14a2e;")

    def change_color(self):
        color = QtWidgets.QColorDialog.getColor()
        number = self.sender().number

        self.channels[number]['color_button'].setStyleSheet(f"background-color: {color.name()};")
        self.main_window.graph_view.plots[number]['plot'].setPen(color)

    def combobox_updated(self):
        board_num = 0
        for i in range(len(self.channels)):
            if self.channels[i]['channel_options'].labels['channel_type'].currentData() == AiChanType.TC:
                self.channels[i]['channel_options'].labels['channel_tc_type'].setEnabled(True)
                self.channels[i]['channel_options'].labels['channel_tc_scale'].setEnabled(True)
                self.channels[i]['channel_options'].labels['channel_mode'].setEnabled(False)
                self.channels[i]['channel_options'].labels['channel_range'].setEnabled(False)
            else:
                self.channels[i]['channel_options'].labels['channel_tc_type'].setEnabled(False)
                self.channels[i]['channel_options'].labels['channel_tc_scale'].setEnabled(False)
                self.channels[i]['channel_options'].labels['channel_mode'].setEnabled(True)
                self.channels[i]['channel_options'].labels['channel_range'].setEnabled(True)

            if self.channels[i]['channel_options'].labels['enable'].isChecked():
                if self.channels[i]['channel_options'].labels['channel_type'].currentData() == AiChanType.TC:
                    ul.ignore_instacal()
                    ul.create_daq_device(board_num, self.main_window.device_descriptor)

                    ul.set_config(InfoType.BOARDINFO, board_num, i, BoardInfo.ADCHANTYPE,
                                  self.channels[i]['channel_options'].labels['channel_type'].currentData())
                    ul.set_config(InfoType.BOARDINFO, board_num, i, BoardInfo.CHANTCTYPE,
                                  self.channels[i]['channel_options'].labels['channel_tc_type'].currentData())
                    ul.set_config(InfoType.BOARDINFO, board_num, i, BoardInfo.TEMPSCALE,
                                  self.channels[i]['channel_options'].labels['channel_tc_scale'].currentData())
                
                else:
                    ul.set_config(InfoType.BOARDINFO, board_num, i, BoardInfo.ADCHANTYPE, 
                                  self.channels[i]['channel_options'].labels['channel_type'].currentData())
                    ul.a_chan_input_mode(board_num, i, 
                                         self.channels[i]['channel_options'].labels['channel_mode'].currentData())


class ToolbarVerticalChannelConfiguration(QtWidgets.QWidget):
    def __init__(self, inform_options, parent=None):
        super().__init__()
        self.parent = parent

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.options = inform_options
        self.labels = {}

        layout = QtWidgets.QHBoxLayout()
        widget = QtWidgets.QLabel()
        widget.setText("Enable")
        layout.addWidget(widget)

        widget = QtWidgets.QCheckBox()
        widget.setChecked(False)
        widget.stateChanged.connect(parent.update_button_color)

        layout.addWidget(widget)
        self.layout().addLayout(layout)
        self.labels["enable"] = widget

        for name, option in self.options.items():
            layout = QtWidgets.QHBoxLayout()

            widget = QtWidgets.QLabel()
            widget.setText(option[0])
            layout.addWidget(widget)

            widget = QtWidgets.QComboBox()
            for key in option[1].keys():
                widget.addItem(key, option[1][key])
            widget.currentIndexChanged.connect(self.parent.combobox_updated)
            layout.addWidget(widget)

            self.layout().addLayout(layout)
            self.labels[name] = widget
