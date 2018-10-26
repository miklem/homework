import os


class IOextendedClass(object):
    """description of class"""
    def __init__(self):
        return super(IOextendedClass, self).__init__()

    def getRelativeFilePath(self, f=None):
        if f:
            path = os.path.join(os.path.dirname(__file__), f)
            print path
            if os.path.isfile(path):
                "IO: file was found"
                return "r{0}".format(path)
            else:
                print "{0} not exist or not a file".format("E:\GoogleDrive\3D\Python\education\16_Threads\worker.py")
        else:
            print "no file in IOextended.py>getRelativePath()"
            return None




