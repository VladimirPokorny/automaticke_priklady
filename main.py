from PySide6 import QtWidgets, QtGui, QtCore
from widgets import central_widget, main_area, toolbar_manager
from widgets.views import text_view	
from widgets.toolbars import example_configuration

import sys


class MainWindow(QtWidgets.QMainWindow):
    """
    Main window of the application.
    """
    def __init__(self):
        """
        Initialize the main window.
        """
        super().__init__()

        self.absolute_widget = {}

        self.board_num = 0
        self.channel = 0
        self.measured_range = 10
        self.connected = False

        self.timer_value = 1000
        self.timer = QtCore.QTimer()

        self.setWindowTitle('EDX sensor temperature')
        self.setGeometry(50, 50, 1200, 800)

        self.setStyleSheet(open('style/style.qss', 'r').read())

        self.menu_bar = self.menuBar()
        self.menu_bar.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.menu_bar.setStyleSheet('padding:5px 0px;')

        self.file_submenu = self.menu_bar.addMenu('&File')
        reconnect_action = QtGui.QAction('Reconnect', self.file_submenu)
        reconnect_action.triggered.connect(self.adc_init)
        self.file_submenu.addAction(reconnect_action)

        self.setCentralWidget(QtWidgets.QWidget())
        self.centralWidget().setMouseTracking(True)
        self.centralWidget().setMinimumSize(500, 400)

        self.centralWidget().setLayout(QtWidgets.QVBoxLayout())
        self.centralWidget().layout().setSpacing(0)
        self.centralWidget().layout().setContentsMargins(0, 0, 0, 0)

        self.survey_central_widget = central_widget.CentralWidget(self)
        self.centralWidget().layout().addWidget(self.survey_central_widget)

        self.graph_view = text_view.TextView()


        self.main_area = main_area.MainArea(self.graph_view)
        self.main_area.setFixedHeight(self.survey_central_widget.size().height())
        self.main_area.setParent(self.survey_central_widget)

        self.survey_central_widget.register_absolute_widget('main_area', self.main_area)
        self.left_toolbars = self.survey_central_widget.register_absolute_widget('left_toolbars', 
            toolbar_manager.ToolbarManager(self.survey_central_widget, 'left'))

        self.data_capturing = self.left_toolbars.addToolbar(example_configuration.ExampleConfiguration(self))
        # self.file_processing = self.left_toolbars.addToolbar(file_processing.FileProcessing(self))
        # self.recording_information = self.left_toolbars.addToolbar(recording_information.RecordingInformation(self))
        # self.device_configuration = self.left_toolbars.addToolbar(device_configuration.DeviceConfiguration(self))

    def adc_init(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.showMaximized()
    sys.exit(app.exec())
