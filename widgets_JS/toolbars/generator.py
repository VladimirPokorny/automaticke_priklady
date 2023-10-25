from PySide6 import QtCore, QtWidgets
from ..elements import buttons, spin_box
from . import base
from style import images_dir
import datetime
import config
import csv
import numpy as np
import pickle
import os

class Generator(base.Toolbar):
    """
    Initializes an instance of the "FILE PROCESSING" window with a specified main window.

    Args:
        main_window: The main window of the application.
    """
    def __init__(self, main_window):
        super().__init__('FILE PROCESSING', images_dir + 'tools_icons/save.svg')
        self.main_window = main_window

        self.data_directory = config.data_folder

        self.log_filename = None

        self.load_csv_button = buttons.ToolbarPushButton('Load dat file')
        self.load_csv_button.clicked.connect(self.open_log_file)

        control_options = {
            "choose_folder": ('Choose folder', None),
            "make_new_file": ('Create new file', None)
        }

        self.control_buttons = buttons.ToolbarMultiPushButton(control_options, multi_select=True)
        self.control_buttons.clicked.connect(self.working_file_manager)

        self.content.layout().addWidget(self.load_csv_button, 0, 0, 1, 2)
        self.content.layout().addWidget(self.control_buttons, 1, 0, 1, 2)

    def working_file_manager(self, option):
        """
        Manages working files based on the given option.

        Args:
            option (str): A string indicating the desired operation. It can be either
                          'make_new_file' or 'choose_folder'.

        Returns:
            None
        """
        if option == 'make_new_file':
            self.create_new_log_file()
        elif option == "choose_folder":
            self.choose_data_directory()

    def choose_data_directory(self):
        """
        Displays a dialog box to choose a directory and sets the selected directory as the data directory.

        Args:
            self: The object pointer.

        Returns:
            None
        """
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOptions(QtWidgets.QFileDialog.ShowDirsOnly)

        if dialog.exec():
            self.data_directory = dialog.selectedFiles()[0]

    def create_new_log_file(self, log_filename=None ):
        """
        Creates a new log file with the given filename.

        Args:
            log_filename (str): The filename for the new log file.

        Returns:
            None
        """
        if log_filename is None:
            actual_date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            log_filename = os.path.join(self.data_directory, actual_date + '_temperature.dat')
            print(log_filename)

        with open(log_filename, 'wb') as f:
            pickle.dump([], f)
            f.close()
        
        self.log_filename = log_filename
    
    def open_log_file(self):
        """
        Opens a dialog to select a log file, reads the data from the file, and displays the data in a graph view.

        Returns:
            None
        """
        file_filter = 'Log files (*.dat);; All Files (*.*)'
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a log file',
            dir=self.data_directory,
            filter=file_filter,
            selectedFilter='Log files (*.dat)'
        )

        self.load_data_from_log(self.file_name)


    def save_temperature_value(self, data: dict):
        """
        Saves the given temperature value and its associated time in a CSV file.

        Args:
            self: The object instance.
            time (str): The time at which the temperature was recorded in '%Y-%m-%d_%H-%M-%S.%f' format.
            temperature (float): The temperature value that needs to be saved.

        Returns:
            None
        """

        if self.log_filename is None:
            self.create_new_log_file()
        else:
            pass

        saving_data = {}


        for channel in data.keys():
            saving_data[channel] = {}
            saving_data[channel]['time'] = data[channel]['time']
            saving_data[channel]['data'] = data[channel]['data']
            saving_data[channel]['time_filtered'] = data[channel]['time_filtered']
            saving_data[channel]['data_filtered'] = data[channel]['data_filtered']

        with open(self.log_filename, 'wb') as f:
            pickle.dump(saving_data, f)
            f.close()
        

    def load_data_from_log(self, file_name: str):
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
            f.close()

        self.imported_plots = {}

        for channel in data.keys():
            self.imported_plots[channel] = {}
            self.imported_plots[channel]['time'] = data[channel]['time']
            self.imported_plots[channel]['data'] = data[channel]['data']
            self.imported_plots[channel]['time_filtered'] = data[channel]['time_filtered']
            self.imported_plots[channel]['data_filtered'] = data[channel]['data_filtered']

        self.main_window.graph_view.show_imported_data(self.imported_plots)