import os

iconvert = r'"C:\Program Files\Side Effects Software\Houdini 16.5.268\bin\iconvert.exe"'


def convert(src, trg=None):
    if trg:
        if not os.path.exists(trg):
            os.makedirs(trg)
        elif os.path.isfile(trg):
            trg = os.path.dirname(trg)
        basename = os.path.basename(src)
        name, ext = os.path.splitext(basename)
        trg = os.path.join(trg, name + '.bmp')
    else:
        trg = os.path.splitext(src)[0] + '.bmp'
    cmd = ' '.join([iconvert, src, trg])
    os.popen(cmd)


    # convert('E:/GoogleDrive/3D/Python/education/12_Converter/imageConverter/edit.png')