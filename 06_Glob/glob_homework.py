
import os
from zipfile import ZipFile

src = "C:/temp/testpack/cometJointOrient.mel"
zFile = "D:/GoogleDrive/3D/Python/education/06_Glob/arch.zip"

# # zf = ZipFile(zFile, 'w')
# # zf.write(src, os.path.basename(src))
# # zf.close()

# trg = "D:/GoogleDrive/3D/Python/education/06_Glob/unpack"
# zf = ZipFile(zFile, 'r')
# print zf.namelist()
# for f in zf.namelist():
#     full = os.path.join(trg, f)
#     d = os.path.dirname(full)
#     if d:
#         if not os.path.exists(d):
#             os.makedirs(d)
#     if os.path.basename(f):
#         out = open(full, 'wb')
#         out.write(zf.read(f))
#         out.close()
# zf.close()

folder = "C:/temp/testpack"
zf = ZipFile('D:/GoogleDrive/3D/Python/education/06_Glob/arch.zip', 'w')

for path, dirs, files in os.walk(folder):
    for file in files:
        full = os.path.join(path, file)
        zf.write(full)
zf.close()




