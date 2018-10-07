from PySide.QtGui import *
from IC_settings import settings

import webbrowser


class ComboBoxClass(QComboBox):
    def __init__(self):
        super(ComboBoxClass, self).__init__()
        self.load_ext()
        self.currentIndexChanged.connect(self.index_changed)

    def load_ext(self, converter='iconvert'):
        self.addItems(settings.parameters.get(converter))
        # set jpg as default parameter
        item = self.findText(settings.parameters.get('default_convert_to_ext'))
        self.setCurrentIndex(item)

    def index_changed(self):
        pass



