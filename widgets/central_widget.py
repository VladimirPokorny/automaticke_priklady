from PySide6 import QtWidgets


class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.absolute_widgets = {}

    def register_absolute_widget(self, name, widget):
        if not hasattr(widget, "parent_resized"):
            print("widget has to have parent_resized function")
        self.absolute_widgets[name] = widget
        return widget

    def resizeEvent(self, event):
        for item in self.absolute_widgets.values():
            item.parent_resized(self.size())
        super().resizeEvent(event)
