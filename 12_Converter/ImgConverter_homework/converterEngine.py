import os
from IC_settings import settings
from PIL import Image


class ConverterEngineClass(object):
    def __init__(self):
        super(ConverterEngineClass, self).__init__()

    def run_converter(self, item):
            trg = self.__build_target(item)
            self.convert(item, trg)

    #
    # def __build_target(self, path=None):
    #     rel_path = os.path.relpath(path, "")
    #     rel_path = rel_path.replace(rel_path.split('\\')[0]+"\\", "")
    #     ######################### get folder and name
    #     folder, file = os.path.split(rel_path)
    #     basename = os.path.basename(rel_path)
    #     name, ext = os.path.splitext(basename)
    #     trg = os.path.join(settings.parameters.get('output_path'), folder)
    #     if not os.path.isdir(trg):
    #         os.makedirs(trg)
    #     trg = os.path.join(trg, name + settings.parameters.get('convert_to_ext'))
    #     return trg

    def __build_target(self, path=None, root = None):
        # if not root:
        #     root = os.path.dirname(path)
        rel_path = os.path.relpath(path, "")
        rel_path = rel_path.replace(rel_path.split('\\')[0]+"\\", "")
        ######################### get folder and name
        folder, file = os.path.split(rel_path)
        basename = os.path.basename(rel_path)
        name, ext = os.path.splitext(basename)
        trg = os.path.join(settings.parameters.get('output_path'), folder)
        if not os.path.isdir(trg):
            os.makedirs(trg)
        trg = os.path.join(trg, name + settings.parameters.get('convert_to_ext'))
        return trg


    def scale_image(self, src=None):
        if src and os.path.isfile(src):
            original_img = Image.open(src)
            w, h = original_img.size
            w = (w*settings.parameters.get('scale'))/100
            h = (h*settings.parameters.get('scale'))/100
            max_size = (w, h)
            original_img.thumbnail(max_size, Image.ANTIALIAS)
            original_img.save(src)
        else:
            pass

    def convert(self, src="", trg=None):
        src = src.replace("\\","/")
        basename = os.path.basename(src)
        name, ext = os.path.splitext(basename)
        if ext in settings.parameters.get('filtered'):
            trg = trg.replace("\\","/")
            # ""converter" "path1" "path2""
            cmd = '"' + '"%s"' % settings.parameters.get('converter_path') + ' "%s"' % src + ' "%s"' % trg
            if settings.parameters.get('compress'):
                cmd = cmd + " quality %i" % int(settings.parameters.get('quality_compression')*10) #allows range 10-100
            cmd = cmd + '"'

            try:
                os.popen(cmd)
                # print cmd
                if settings.parameters.get('scale') != 100:
                    self.scale_image(trg)
                else:
                    pass
            except:
                pass

        else:
            pass


convEngine = ConverterEngineClass()