import os
path = r"D:\GoogleDrive\3D\Python\education\folders"
proj = "project_1"
folders = ['input', 'output', 'scenes', 'assets']

proj_path=os.path.join(path,proj)

if not os.path.exists(proj_path):
    os.mkdir(proj_path)
    for folder in folders:
        os.mkdir(os.path.join(proj_path,folder))
else:
    pass

