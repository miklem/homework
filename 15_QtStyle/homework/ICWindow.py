from PySide.QtGui import *
from PySide.QtCore import *

import os



from widgets import SourceFilesList
from widgets import ExtList
from widgets import LineEdit
from widgets import ComboBox
import converter_uis as ui
import converterEngine as convEngine
from IC_settings import settings
import Tkinter
import tkFileDialog









update=False





class ImageConverterMainClass(QMainWindow, ui.Ui_ImgConverter):
    def __init__(self):
        super(ImageConverterMainClass, self).__init__()
        self.setupUi(self)

        self.filesList = SourceFilesList.SourceFilesListClass()
        self.sourceFiles_ly.addWidget(self.filesList)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.extManagerList = ExtList.ExtListClass()
        self.extList_ly.addWidget(self.extManagerList)
        self.outputPath_le = LineEdit.EditLineClass()
        self.outputPath_ly.addWidget(self.outputPath_le)
        self.outExt_cb = ComboBox.ComboBoxClass()
        self.outExt_ly.addWidget(self.outExt_cb)

        # connections
        self.convPath_btn.clicked.connect(self.set_converter)
        self.addExt_le.returnPressed.connect(self.add_ext)
        self.selectAll_btn.clicked.connect(self.extManagerList.select_all)
        self.selectNone_btn.clicked.connect(self.extManagerList.deselect_all)
        self.outputPath_btn.clicked.connect(self.set_outputFolder)
        self.startStop_btn.clicked.connect(self.filter_extensions) #convEngine.run_converter
        self.outExt_cb.currentIndexChanged.connect(self.ext_changed)
        self.compression_chb.stateChanged.connect(self.compression_on_off)
        self.compression_spb.valueChanged.connect(self.set_compression)
        self.scale_sldr.valueChanged.connect(self.change_scale)
        self.folder_btn.clicked.connect(self.add_folder_to_src)
        self.img_btn.clicked.connect(self.add_img_to_src)
        self.delAll_btn.clicked.connect(self.filesList.del_all_item)

        self.pathToWatch = os.path.dirname(__file__)
        self.style = os.path.join(os.path.dirname(__file__), 'IC.css')

        self.fs_watcher = QFileSystemWatcher([self.pathToWatch, self.style])
        self.fs_watcher.directoryChanged.connect(self.directory_changed)
        self.fs_watcher.fileChanged.connect(self.file_changed)

        print update

        # start
        settings.set_values('convert_to_ext', '.jpg')
        if not settings.parameters.get('convert_to_ext') == ".jpg":
            self.compression_chb.setEnabled(0)
            self.compression_spb.setEnabled(0)
        settings.set_values('scale', 100)
        settings.set_values('compress', False)
        self.scaleVal_le.setText(str(self.scale_sldr.value()))

        self.__fill_labels()
        self.__fill_extensions()
        root = Tkinter.Tk()
        root.withdraw()


    def mousePressEvent(self, event):
        pass
        # print "mouse"

    def set_converter(self):
        path = tkFileDialog.askopenfilename(title='Please select converter file', filetypes=[('*.exe', '*.exe')]).replace('/','\\')
        settings.set_values("converter_path", path)
        if os.path.basename(path) == 'iconvert.exe':
            settings.set_values('activeConverter', 'iconvert')
        self.__fill_labels()

    def __fill_labels(self):
        temp = settings.parameters.get("converter_path", "")
        self.convPath_lb.setText(temp)
        self.convPath_lb.setToolTip(temp)
        self.outputPath_le.setText(settings.parameters.get("output_path", ""))

    def __fill_extensions(self):
        ext = settings.parameters.get('extensions')
        for e in ext:
            self.extManagerList.add_item(e)

    def add_ext(self):
        # add extension to execution list
        new_ext = "." + self.addExt_le.text()
        result = self.extManagerList.check_format_support(new_ext)
        if result == 1:
            self.extManagerList.add_item(new_ext)
        if result == -1:
            self.addExt_le.setText("not supported")
            self.addExt_le.selectAll()
        if result == 0:
            self.addExt_le.setText("already exist")
        if result == -2:
            self.set_converter()
            self.add_ext()
        self.addExt_le.setText("")

    def set_outputFolder(self):
        path = tkFileDialog.askdirectory(title='Please select output path').replace('/','\\')
        if os.path.isdir(path):
            settings.set_values("output_path", path)
            self.outputPath_le.setText(path)
        else:
            print "wrong path"

    def ext_changed(self):
        value = self.outExt_cb.itemText(self.outExt_cb.currentIndex())
        settings.set_values('convert_to_ext', value)
        if settings.parameters.get('convert_to_ext') in settings.parameters.get('support_compression'):
            self.compression_chb.setEnabled(1)
            self.compression_spb.setEnabled(1)
        else:
            self.compression_chb.setEnabled(0)
            self.compression_spb.setEnabled(0)

    def compression_on_off(self):
        if self.compression_chb.isChecked():
            settings.set_values('compress', True)
            self.set_compression()
        else:
            settings.set_values('compress', False)

    def set_compression(self):
        settings.set_values('quality_compression', self.compression_spb.value())

    def change_scale(self):
        settings.set_values('scale', self.scale_sldr.value())

    def filter_extensions(self):
        self.extManagerList.get_all_selected_ext()
        inc = 100 / len(settings.files)
        for item in settings.files:
            convEngine.run_converter(item)
            self.progressBar.setValue(self.progressBar.value() + inc)
        self.progressBar.setValue(0)

    def add_folder_to_src(self):
        path = tkFileDialog.askdirectory(title='Please select folder').replace('/','\\')
        if os.path.isdir(path):
            self.filesList.add_object(path)

    def add_img_to_src(self):
        path = tkFileDialog.askopenfilename(title='Please select file').replace('/','\\')
        if os.path.isfile(path):
            self.filesList.add_object(path)

    def directory_changed(self):
        print('Directory Changed!!!')

    def file_changed(self):
        print('File Changed!!!')
        try:
            result = self.setStyleSheet(open(self.style).read())
            print result
        except:
            print "error in CSS"


if __name__ == '__main__':
    app = QApplication([])
    w = ImageConverterMainClass()
    w.show()
    app.exec_()