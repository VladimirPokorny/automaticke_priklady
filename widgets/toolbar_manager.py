from PySide6 import QtWidgets, QtCore, QtGui
import config


class ToolbarManager:
    def __init__(self, parent, type="left"):
        self.parent = parent
        self.type = type
        self.toolbars = []

        self.scrollbar = QtWidgets.QScrollBar()
        self.scrollbar.setParent(self.parent)
        self.scrollbar.hide()
        self.scrollbar_width = 15
        self.scrollbar.valueChanged.connect(self.slider_changed)

    def addToolbar(self, toolbar, set_parent=True):
        self.toolbars.append(toolbar)
        if set_parent:
            toolbar.setParent(self.parent)
        toolbar.toolbar_manager = self
        return toolbar

    def slider_changed(self, value):
        self.parent_resized()

    def parent_resized(self, size=None):
        if size is None:
            size = self.parent.size()
        total_size = 0
        add = 10
        for toolbar in self.toolbars:
            total_size += add + toolbar.size().height()

        scroll_bar_width = 0

        vertical_position = 0

        if total_size > size.height():
            self.scrollbar.show()
            self.scrollbar.setMaximum(total_size - size.height())
            self.scrollbar.setPageStep(size.height())
            self.scrollbar.setFixedSize(self.scrollbar_width, size.height())
            if self.type == "left":
                self.scrollbar.move(0, 0)
            else:
                self.scrollbar.move(size.width() - self.scrollbar_width, 0)
            scroll_bar_width = self.scrollbar_width
            vertical_position = -self.scrollbar.value()
        else:
            self.scrollbar.hide()
        # (self.parent.size().height() - total_size)/len(self.toolbars)

        for toolbar in self.toolbars:
            toolbar.slider_width = scroll_bar_width
            if toolbar.expanded:
                toolbar.setFixedWidth(config.panel_size * 2 - scroll_bar_width)
                if self.type == "right":
                    toolbar.move(size.width() - config.panel_size * 2, vertical_position)
                else:
                    toolbar.move(scroll_bar_width, vertical_position)

            else:
                toolbar.setFixedWidth(config.panel_size - scroll_bar_width)
                if self.type == "right":
                    toolbar.move(size.width() - config.panel_size, vertical_position)
                else:
                    toolbar.move(scroll_bar_width, vertical_position)

            vertical_position += toolbar.size().height() + add
