from PySide.QtGui import *
from IC_settings import settings

import webbrowser


class EditLineClass(QLineEdit):
    def __init__(self):
        super(EditLineClass, self).__init__()
        self.mouseDoubleClickEvent(QMouseEvent.MouseButtonDblClick)

    def mouseDoubleClickEvent(self, event):
        path = self.text()
        if path == settings.parameters.get('output_path'):
            webbrowser.open(path)




