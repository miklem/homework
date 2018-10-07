from PySide.QtGui import *
from PySide.QtCore import *
import os
from IC_settings import settings


class ExtListClass(QListWidget):
    def __init__(self):
        super(ExtListClass, self).__init__()
        self.setViewMode(QListView.ListMode)

    def add_item(self, item=None):
        if item:
            item_name = item
            item = QListWidgetItem()
            item.setText(item_name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked)
            self.addItem(item)

    def uncheck_item(self, item=None):
        if item:
            self.editItem(item)

    def check_format_support(self, ext=None ):
        if ext:
            ext_list = settings.parameters.get('extensions')
            converter = settings.parameters.get('activeConverter')
            ext_supported = settings.parameters.get(converter)
            if converter != '':
                if ext not in ext_list:
                    if ext in ext_supported:
                        ext_list.append(ext)
                        settings.set_values('extensions', ext_list)
                        return 1
                    else:
                        # not supported by converter
                        return -1
                else:
                    #already in list
                    return 0
            else:
                return -2 #call set converter function



    def deselect_all(self):
        for i in range(self.count()):
            self.item(i).setCheckState(Qt.Unchecked)

    def select_all(self):
        for i in range(self.count()):
            self.item(i).setCheckState(Qt.Checked)

    def get_all_selected_ext(self):
        "return all selected extensions"
        filtered = []
        items = self.selectAll()
        for i in range(self.count()):
            if self.item(i).checkState() == Qt.CheckState.Checked:
                filtered.append(self.item(i).text())

        settings.set_values('filtered', filtered)



