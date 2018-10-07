import os
from zipfile import ZipFile
from os.path import basename
import shutil


src = "C:/temp/testpack"
tgt = "C:/temp/testunpack"
zFile = "C:/temp/archive.zip"
skip = (".TXT", ".SYS", ".LNG")

def pack(path = ""):
    if check_path(path):
        ##varian 1
        # shutil.make_archive(zFile, 'zip', path)
        
        #variant 2
        with ZipFile(zFile, 'w') as zf:
            for paths, folders, files in os.walk(path):
                for f in files:
                    if not check_name(f, skip):
                        full = os.path.join(paths, f)
                        zf.write(full, full[len(path):])
    print "packed!"


def pack_pseudoRecursion(path = "", zFileName = "archive.zip", zFilePath = "C:/temp"):
        if check_path(zFilePath):
            zFile = zFilePath + "/" + zFileName
            zf = ZipFile(zFile, 'w')
            for paths, folders, files in os.walk(path):
                for f in files:
                    if not check_name(f, skip):
                        full = os.path.join(paths, f)#[len(path):]
                        print full
                        nf =singlezip(full)
                        zf.write(nf,nf[len(path):] )
                        os.remove(nf)
            zf.close()


def singlezip(src = ""):
    name = src + ".zip"
    zf = ZipFile(name, 'w')
    zf.write(src, os.path.basename(src))
    zf.close()
    return name


def check_name(name = "", toSkip =""):
    if name !="":
        res = any(ext in name for ext in toSkip)
        if  res:
            return True
        else:
            return False
    else:
        pass

def unpack(path_target = "", zFile = ""):
    if check_path(path_target):
        if zFile != "":
            with ZipFile(zFile, 'r') as zf:
                for f in zf.namelist():
                    full = os.path.join(path_target, f)
                    d = os.path.dirname(full)
                    if d:
                        if not os.path.exists(d):
                            os.makedirs(d)
                    if os.path.basename(f):
                        out = open(full, 'wb')
                        out.write(zf.read(f))
                        out.close()
        else:
            print "no zip file to unpack!"



def check_path(path = ""):
    if path !="":
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
                return True
            except:
                print "can't create folder!"
                return False
        else:
            return True
    else:
        return False


# pack(src)
pack_pseudoRecursion(path = src, zFilePath = os.getenv('APPDATA'))
# unpack(tgt, zFile)
