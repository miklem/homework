import os
import json

jsettings = "IC_settings.json"


class ICsettingsClass(object):
    def __init__(self):
        self.parameters = dict(
            settings_path=os.path.expanduser("~"),
            converter_path=None,
            readSubFolders=1,
            scale=100,
            extensions=['.jpg', '.png'],
            sizeLimit=-1,
            output=None,
            fileAction=['replace, skip, auto'],
            iconvert=[
                '.pic',
                '.rat',
                '.pic.gz',
                '.pic.Z',
                '.picnc',
                '.ratnc',
                '.ip',
                '.iw',
                '.md',
                '.png',
                '.psd',
                '.psb',
                '.fip',
                '.vf',
                '.a60',
                '.cin',
                '.kdk',
                '.fit',
                '.gif',
                '.gif89',
                '.ies',
                '.jpg',
                '.jpeg',
                '.qtl',
                '.rla',
                '.rla16',
                '.pix',
                '.sgi',
                '.rgb',
                '.rgba',
                '.si',
                '.pic',
                '.tif',
                '.tiff',
                '.tif3',
                '.tif16',
                '.tx',
                '.tga',
                '.vst',
                '.vtg',
                '.yuv'
        ],
            activeConverter="",
            output_path="",
            default_convert_to_ext='.jpg',
            convert_to_ext=".jpg",
            compress=True,
            quality_compression=10,
            support_compression=[".jpg"],
            filtered=[]
        )
        self.files = []
        self.paths = []
        self.rel_files = [] #output files
        self.settingFullPath = os.path.join(self.parameters['settings_path'], jsettings)
        # check if settings is on the place
        if not os.path.exists(self.settingFullPath):
            self.__write_json()
        else:
            self.parameters = self.__read_json()

    def __write_json(self):
        path = self.settingFullPath
        with open(path, 'w') as f:
            json.dump(self.parameters, f, indent=4)

    def __read_json(self):
        if os.path.isfile(self.settingFullPath):
            try:
                return json.load(open(self.settingFullPath))
            except IOError:
                print "IO error while reading {0} file".format(jsettings)
            except:
                print "Some error while reading {0} file".format(jsettings)

    def set_values(self, name = None, value=None):
        if name and value is not None:
            if name in self.parameters:
                self.parameters[name] = value
                self.__write_json()
            else:
                print "there is no such key in settings: {0}". format(name)
                pass

    def get_supported_extensions(self, converter='iconvert'):
        return self.parameters.get(converter)


settings = ICsettingsClass()
    



