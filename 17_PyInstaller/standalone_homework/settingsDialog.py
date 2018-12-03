import Tkinter
import json
import os
import tkFileDialog

from PySide.QtCore import *
from PySide.QtGui import *

from uis import settingsDialog_uis as ui

settingsFileName = 'ProjectManagerSettings.json'
templateFileName = 'ProjectManagerTemplate.json'



class SettingsClass(QDialog, ui.Ui_settingsDialog):

    parameters = dict(
        proj_path='',
        backUp_path=''
    )

    def __init__(self):
        super(SettingsClass, self).__init__()
        self.setupUi(self)
        self.projPath = os.path.join(os.path.expanduser('~'), settingsFileName)
        self.backUpPath = os.path.expanduser('~')
        self.templatePath = self.get_template_file()
        self.settingsPath = os.path.join(os.path.expanduser('~'), settingsFileName)

        # webbrowser.open(self.path)
        if not os.path.exists(self.projPath):
            self.__make_default(self.projPath)
        if not os.path.exists(self.templatePath):
            self.__make_default(self.templatePath, False)

        root = Tkinter.Tk()
        root.withdraw()
        #
        #connections
        self.projPathDialog_btn.clicked.connect(self.__set_project_path)
        self.backUpPathDialog_btn.clicked.connect(self.__set_backup_path)
        self.add_btn.clicked.connect(self.__add_item)
        self.rem_btn.clicked.connect(self.__rem_item)
        #
        # widget settings
        self.template_trw.setDragDropMode(QAbstractItemView.InternalMove)  # #turn drag and drop on
        self.template_trw.setSelectionMode(QAbstractItemView.ExtendedSelection)

        #start
        self.__load_template()



    def save_settings(self):
        with open(self.settingsPath, 'w') as f:
            json.dump(self.parameters, f, indent=4)

    def save_template(self):
        template = self.__get_structure()
        with open(self.templatePath, 'w') as f:
            json.dump(template, f, indent=4)

    def load(self):
        if os.path.isfile(self.projPath):
            try:
                self.parameters = json.load(open(self.projPath))
                self.__fill_data(self.parameters)
                return self.parameters
            except IOError:
                print "IO error while reading {0} file".format(settingsFileName)
            except:
                print "Some error while reading {0} file".format(settingsFileName)

    def get_project_path(self):
        return self.parameters['proj_path']

    def get_backup_path(self):
        return self.parameters['backUp_path']

    @staticmethod
    def get_template_file():
        return os.path.join(os.path.expanduser('~'), templateFileName)


    def __set_project_path(self):
        path = tkFileDialog.askdirectory(title='Please select a project directory').replace('/','\\')
        self.parameters['proj_path'] = path
        self.projPath_le.setText(path)

    def __set_backup_path(self):
        path = tkFileDialog.askdirectory(title='Please select a  backup directory').replace('/','\\')
        self.parameters['backUp_path'] = path
        self.backupPath_le.setText(path)

    def __make_default(self, path, settings=True):
        if settings:
            def_data = self.parameters
        else:
            def_data = ""
        with open(path, 'w') as f:
            json.dump(def_data, f, indent=4)

    def __fill_data(self, data):
        self.projPath_le.setText(data['proj_path'])
        self.projPath = data['proj_path']
        self.backupPath_le.setText(data['backUp_path'])
        self.backUpPath = data['backUp_path']

    def __add_item(self, name='Folder', parent=None):
        if not parent:
            parent = self.template_trw.invisibleRootItem()
        item = QTreeWidgetItem()
        #
        #https://doc.qt.io/qt-4.8/qt.html#ItemFlag-enum
        item.setFlags(
            Qt.ItemIsEnabled |
            Qt.ItemIsSelectable |
            Qt.ItemIsEditable |
            Qt.ItemIsDragEnabled |
            Qt.ItemIsDropEnabled
        )
        item.setText(0, name)
        parent.addChild(item)
        item.setExpanded(1)
        return item

    def __rem_item(self):
        items = self.template_trw.selectedItems()
        for i in items:
            (i.parent() or self.template_trw.invisibleRootItem()).takeChild(self.template_trw.indexFromItem(i).row())

    def __get_structure(self, parent=None):
        level = []
        if not parent:
            parent = self.template_trw.invisibleRootItem()
        for i in range(parent.childCount()):
            child = parent.child(i)
            content = self.__get_structure(child)
            level.append({
                'name': child.text(0),
                'content': content
            })
        return level

    def __load_template(self):
        if os.path.exists(self.templatePath):
            with open(self.templatePath) as f:
                template = json.load(f)
                self.__restore_structure(template)

    def __restore_structure(self, data, parent=None):
        if not parent:
            parent = self.template_trw.invisibleRootItem()
        for i in data:
            item = self.__add_item(i['name'], parent)
            self.__restore_structure(i['content'], item)





