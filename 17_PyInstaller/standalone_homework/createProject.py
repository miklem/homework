import os, json, settingsDialog
from uis import projectManager_uis as ui

from PySide.QtGui import *

#store info for each project
projectInfoFileName = '.prjinfo'


class CreateProjectClass(object):

    parameters = dict(
        proj_name='',
        customer_name='',
        deadline='',
        proj_manager_name='',
        proj_manager_email=''
    )


    def __init__(self):
        super(CreateProjectClass, self).__init__()
        self.settings = settingsDialog.SettingsClass()
        self.settings.load()

    def main(self, path):
        if self.__make_folder(path):
            template = json.load(open(self.settings.get_template_file()))
            self.__make_project_folders(path, template)
            self.__save_project_info(path)

    def __make_folder(self, path):
        try:
            os.mkdir(path)
            return True
        except IOError as error:
            print error
            return False
        except:
            return False

    def __make_project_folders(self, root, folders):
        for f in folders:
            path = os.path.join(root, f['name'])
            self.__make_folder(path)
            self.__make_project_folders(path, f['content'])

    def __save_project_info(self,path):
        path = os.path.join(path, self.parameters['proj_name'] + projectInfoFileName)
        with open(path, 'w') as f:
            json.dump(self.parameters, f, indent=4)

    def get_project_info(self,path):
        data = json.load(open(path))
        return """
        Project name: {0}
        Customer: {1}
        Deadline: {2}
        Manager: {3}
        Email: {4}        
        
        """.format(
            data['proj_name'],
            data['customer_name'],
            data['deadline'],
            data['proj_manager_name'],
            data['proj_manager_email']

        )