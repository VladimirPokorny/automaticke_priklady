from ..elements import buttons, spin_box
from . import base
from style import images_dir
from PySide6 import QtWidgets


class RecordingInformation(base.Toolbar):
    def __init__(self, main_window):
        super().__init__("RECORDING INFORMATION", images_dir + "section_icons/debug.svg")
        self.main_window = main_window

        self.device_name = QtWidgets.QLabel('Device name:')
        self.device_name_value = QtWidgets.QLabel('NaN')

        self.active_channel = QtWidgets.QLabel('Channel:')
        self.active_channel_value = QtWidgets.QLabel('NaN')

        self.used_range = QtWidgets.QLabel('ADC voltage range:')
        self.used_range_value = QtWidgets.QLabel('NaN')

        self.voltage_label = QtWidgets.QLabel('Measured voltage:')
        self.voltage_label_value = QtWidgets.QLabel('NaN')

        self.temperature_label = QtWidgets.QLabel('Actual temperature:')
        self.temperature_label_value = QtWidgets.QLabel('NaN')

        self.content.layout().addWidget(self.device_name, 0, 0, 1, 1)
        self.content.layout().addWidget(self.device_name_value, 0, 1, 1, 1)

        self.content.layout().addWidget(self.active_channel, 1, 0, 1, 1)
        self.content.layout().addWidget(self.active_channel_value, 1, 1, 1, 1)

        self.content.layout().addWidget(self.used_range, 2, 0, 1, 1)
        self.content.layout().addWidget(self.used_range_value, 2, 1, 1, 1)

        self.content.layout().addWidget(self.voltage_label, 3, 0, 1, 1)
        self.content.layout().addWidget(self.voltage_label_value, 3, 1, 1, 1)

        self.content.layout().addWidget(self.temperature_label, 4, 0, 1, 1)
        self.content.layout().addWidget(self.temperature_label_value, 4, 1, 1, 1)

    def update_measured_values(self, device_name, active_channel, used_range, voltage, temperature):
        self.device_name_value.setText(f'{device_name}')
        self.active_channel_value.setText(f'{active_channel}')
        self.used_range_value.setText(str(used_range))
        self.voltage_label_value.setText(f'{voltage:.3f} mV')
        self.temperature_label_value.setText(f'{temperature:.2f}°C')
