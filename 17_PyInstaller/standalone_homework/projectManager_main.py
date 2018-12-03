from PySide.QtGui import *
import os
import datetime

import settingsDialog
import createProject
from uis import projectManager_uis as ui


class ProjectManagerMainClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(ProjectManagerMainClass, self).__init__()
        self.setupUi(self)
        self.settings = settingsDialog.SettingsClass()
        self.createProject = createProject.CreateProjectClass()
        #update features
        self.cleanup_btn.setEnabled(0) #disable button
        self.arch_btn.setEnabled(0) #disable button
        self.create_btn.setEnabled(0) #disabe while all fields are filled

        #connects
        self.settings_btn.clicked.connect(self.open_settings_dialog)
        self.create_btn.clicked.connect(self.build_project)
        self.proj_list.itemClicked.connect(self.load_proj_info)
        self.projName_le.textChanged.connect(self.__activate_create_btn)
        self.cutomerName_le.textChanged.connect(self.__activate_create_btn)
        self.deadline_de.dateChanged.connect(self.__activate_create_btn)
        #
        #Load settings
        self.settingsData = self.settings.load()

        #Start
        self.deadline_de.setDate(datetime.datetime.now())
        self.update_list()

    def __activate_create_btn(self):
        if self.projName_le.text()!="":
            if self.cutomerName_le.text()!="":
                if self.deadline_de.date()>=datetime.datetime.now():
                    self.create_btn.setEnabled(1)


    def build_project(self):
        self.__fill_project_parameters()
        path = self.get_full_project_path()
        self.createProject.main(path)
        self.update_list()


    def get_full_project_path(self):
        return os.path.join(self.settings.get_project_path(), self.createProject.parameters['proj_name'])

    def __fill_project_parameters(self):
        self.createProject.parameters['proj_name'] = self.projName_le.text()
        self.createProject.parameters['customer_name'] = self.cutomerName_le.text()
        self.createProject.parameters['deadline'] = self.deadline_de.text()
        self.createProject.parameters['proj_manager_name'] = self.projManagerName_le.text()
        self.createProject.parameters['proj_manager_email'] = self.projManagerEmail_le.text()

    def open_settings_dialog(self):
        if self.settings.exec_():
            self.settings.save_template()
            self.settings.save_settings()

    def update_list(self):
        path = self.settingsData['proj_path']
        if os.path.exists(path):
            for f in os.listdir(path):
                fullPath = os.path.join(path, f)
                if self.is_project(fullPath):
                    item = self.add_item(f)
                    item.setData(32, os.path.join(fullPath, os.path.basename(fullPath) + createProject.projectInfoFileName))

    def is_project(self, path):
        path = os.path.join(path, os.path.basename(path) + createProject.projectInfoFileName)
        return os.path.exists(path)

    def add_item(self, name):
        item = QListWidgetItem()
        item.setText(name)
        self.proj_list.addItem(item)
        return item

    def load_proj_info(self, item):
        self.info_lb.setText(self.createProject.get_project_info(item.data(32)))





if __name__ == '__main__':
    app = QApplication([])
    w = ProjectManagerMainClass()
    w.show()
    app.exec_()

