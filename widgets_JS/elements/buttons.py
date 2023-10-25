from PySide6 import QtWidgets, QtCore, QtGui, QtSvgWidgets


class ToolbarMultiButton(QtWidgets.QWidget):
    clicked = QtCore.Signal(str)

    def __init__(self, options, multi_select=False, no_select=False, default_option=None):
        super().__init__()
        self.multi_select = multi_select
        self.no_select = no_select
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.options = options
        self.buttons = {}
        self.selected = default_option

        for name, option in self.options.items():
            widget = QtWidgets.QPushButton(option[0])
            self.layout().addWidget(widget)
            self.buttons[name] = widget
            if option[1] is not None:
                self.buttons[name].setIcon(QtGui.QIcon(option[1]))
            self.buttons[name].setProperty("class", "toolbarButton")
            if self.multi_select and self.selected is not None:
                self.buttons[name].setProperty("selected", name in self.selected)
            else:
                self.buttons[name].setProperty("selected", name == self.selected)
            self.buttons[name].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.buttons[name].clicked.connect((lambda index: (lambda: self.option_clicked(index)))(name))

    def option_clicked(self, name, emit=True):
        if self.multi_select:
            if self.selected is None:
                self.buttons[name].setProperty("selected", True)
                self.selected = [name]
            elif name in self.selected:
                self.selected.remove(name)
                self.buttons[name].setProperty("selected", False)
            else:
                self.selected.append(name)
                self.buttons[name].setProperty("selected", True)
        elif self.no_select:
            if name == self.selected:
                self.selected = None
                self.buttons[name].setProperty("selected", False)
            else:
                if self.selected is not None:
                    self.buttons[self.selected].setProperty("selected", False)
                self.selected = name
                self.buttons[name].setProperty("selected", True)
        else:
            if self.selected is not None:
                self.buttons[self.selected].setProperty("selected", False)
            self.selected = name
            self.buttons[self.selected].setProperty("selected", True)

        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

        if emit:
            self.clicked.emit(name)


class ToolbarMultiPushButton(QtWidgets.QWidget):
    clicked = QtCore.Signal(str)

    def __init__(self, options, multi_select=False, no_select=False, default_option=None):
        super().__init__()
        self.multi_select = multi_select
        self.no_select = no_select
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.options = options
        self.buttons = {}
        self.selected = default_option

        for name, option in self.options.items():
            widget = QtWidgets.QPushButton(option[0])
            self.layout().addWidget(widget)
            self.buttons[name] = widget
            if option[1] is not None:
                self.buttons[name].setIcon(QtGui.QIcon(option[1]))
            self.buttons[name].setProperty("class", "toolbarPushButton")
            if self.multi_select and self.selected is not None:
                self.buttons[name].setProperty("selected", name in self.selected)
            else:
                self.buttons[name].setProperty("selected", name == self.selected)
            self.buttons[name].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.buttons[name].clicked.connect((lambda index: (lambda: self.option_clicked(index)))(name))

    def option_clicked(self, name, emit=True):
        if self.multi_select:
            if self.selected is None:
                self.buttons[name].setProperty("selected", True)
                self.selected = [name]
            elif name in self.selected:
                self.selected.remove(name)
                self.buttons[name].setProperty("selected", False)
            else:
                self.selected.append(name)
                self.buttons[name].setProperty("selected", True)
        elif self.no_select:
            if name == self.selected:
                self.selected = None
                self.buttons[name].setProperty("selected", False)
            else:
                if self.selected is not None:
                    self.buttons[self.selected].setProperty("selected", False)
                self.selected = name
                self.buttons[name].setProperty("selected", True)
        else:
            if self.selected is not None:
                self.buttons[self.selected].setProperty("selected", False)
            self.selected = name
            self.buttons[self.selected].setProperty("selected", True)

        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

        if emit:
            self.clicked.emit(name)


class ToolbarPushButton(QtWidgets.QPushButton):
    update_selected_signal = QtCore.Signal(bool)
    update_text_signal = QtCore.Signal(str)
    update_style_signal = QtCore.Signal()
    update_enabled_signal = QtCore.Signal(bool)

    def __init__(self, name, selectable=False, icon=None, tooltip=None):
        super().__init__(name)
        if icon is not None:
            self.setIcon(QtGui.QIcon(icon))
        self.setProperty("class", "toolbarButton")
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.selectable = selectable
        self.selected = False

        if tooltip:
            self.setToolTip(tooltip)

        self.update_selected_signal.connect(self.set_selected)  # use this from different threads
        self.update_text_signal.connect(self.setText)
        self.update_style_signal.connect(self.update_style)
        self.update_enabled_signal.connect(self.setEnabled)

    def update_style(self):
        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

    def mousePressEvent(self, e):
        if self.selectable:
            self.set_selected(not self.selected)
        super().mousePressEvent(e)

    def set_selected(self, value):
        self.setProperty("selected", value)
        self.selected = value
        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property


class ToolbarStateButton(QtWidgets.QPushButton):
    clicked = QtCore.Signal(bool)
    update_selected_signal = QtCore.Signal(bool)
    update_text_signal = QtCore.Signal(str)

    def __init__(self, name, selected=False, name_off=None, icon=None, icon_off=None, tooltip=None):
        if not selected and name_off is not None:
            super().__init__(name_off)
        else:
            super().__init__(name)
        self.names = [name, name_off]
        self.icons = [icon, icon_off]
        if (selected and icon is not None) or (not selected and icon_off is None):
            self.setIcon(QtGui.QIcon(icon))
        elif not selected and icon_off is not None:
            self.setIcon(QtGui.QIcon(icon_off))

        self.setProperty("class", "toolbarButton")
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.selected = selected
        self.busy = False
        self.setProperty("selected", selected)
        self.setProperty("busy", False)
        if tooltip:
            self.setToolTip(tooltip)

        self.update_selected_signal.connect(self.set_selected)
        self.update_text_signal.connect(self.setText)

    def set_busy(self, value):
        self.setProperty("busy", value)
        self.busy = value
        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

    def set_error(self, value):
        self.setProperty("error", value)
        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

    def set_selected(self, value, set_busy=False):
        if value:
            if self.names[0] is not None and self.names[1] is not None:
                self.setText(self.names[0])
            if self.icons[0] is not None:
                self.setIcon(QtGui.QIcon(self.icons[0]))
        else:
            if self.names[0] is not None and self.names[1] is not None:
                self.setText(self.names[1])
            if self.icons[1] is not None:
                self.setIcon(QtGui.QIcon(self.icons[1]))

        self.setProperty("selected", value)
        self.selected = value
        self.set_busy(set_busy)
        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

    def update_style(self):
        self.setStyleSheet(self.styleSheet())  # need to redraw the selected property

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.set_selected(not self.selected)
            self.clicked.emit(self.selected)
        else:
            super().mousePressEvent(e)


class HoverSignalsButton(ToolbarPushButton):
    hover_enter = QtCore.Signal()
    hover_leave = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.installEventFilter(self)

    def eventFilter(self, watched, event):
        result = super().eventFilter(watched, event)
        if event.type() == QtCore.QEvent.HoverEnter:
            self.hover_enter.emit()
        elif event.type() == QtCore.QEvent.HoverLeave:
            self.hover_leave.emit()
        return result
