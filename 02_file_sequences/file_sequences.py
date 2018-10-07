import os
import shutil

PATH = r'D:\GoogleDrive\3D\Python\education\02_file_sequences\images'
CORRECTNAME = 'shot_01'
PADDING = 4

# list of FILES
TEMP = os.listdir(PATH)
FILES = []
for t in TEMP:
    if os.path.isfile(os.path.join(PATH, t)):
        FILES.append(t)

TEMP = os.listdir(PATH)
FILES = []
for t in TEMP:
    if os.path.isfile(os.path.join(PATH, t)):
        FILES.append(t)


FRAMES = []
# separate
for f in FILES:
    name, ext = os.path.splitext(f)
    fullName = name
    while name[-1].isdigit():
        # delete symbols from the beginning to the pre-last symbol.
        name = name[:-1]
        digits = int(fullName.replace(name, ''))
        FRAMES.append(digits)
OFFSET = min(FRAMES)
# print "OFFSET:{0}".format(OFFSET)

# new name
OUTPUTFOLDER = os.path.join(PATH, CORRECTNAME)
if not os.path.exists(OUTPUTFOLDER):
    os.mkdir(OUTPUTFOLDER)
for i, f in enumerate(FILES):
    old = os.path.join(PATH, f)
    name, ext = os.path.splitext(f)
    newName = CORRECTNAME + '_' + str(FRAMES[i] - OFFSET).zfill(PADDING) + ext
    new = os.path.join(PATH, CORRECTNAME, newName)
    if os.path.exists(new):
        os.remove(new)
    shutil.copy2(old, new)


# skipped frames
FULLRANGE = range(min(FRAMES), max(FRAMES) + 1)

MISSING = []
for i in FULLRANGE:
    if not i in FRAMES:
        MISSING.append(i)
print "Missing frames: ", MISSING

A = raw_input('remove old files? [y/n]: ')
if A == 'Y' or A == 'y':
    print "ok"
    for f in FILES:
        os.remove(os.path.join(PATH, f))
print "Complete."
raw_input()

# # message
