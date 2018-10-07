import os
path = r"D:\GoogleDrive\3D\Python\education\folders"
folders =\
[
    ['source',
        [
            ['drawings',[]],
            ['sourcemodels',[]],
            ['references',
                [
                    ['fromclient',[]],
                    ['fromweb',[]]
                ]
            ]
        ]
    ],
    ['output',
        [
            ['renders',[]],
            ['models',[]]
        ]
    ]
]

def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        pass

def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            createFolder(path)
            build(path, d[1])

projectname = raw_input('Enter project name: ')
if projectname:
    proj_path = os.path.join(path, projectname)
    createFolder(proj_path)
    build(proj_path, folders)
