import sys
import os

ARG = sys.argv[1:]
root = ""
folders = []

#filter folders
for f in ARG:
    if os.path.isdir(f):
        folders.append(f)

for folder in folders:
    files = []
    allFiles = os.listdir(folder)
    if allFiles:
        for f in allFiles:
            if os.path.isfile(os.path.join(folder, f)):
                if os.path.splitext(f)[-1] == ".txt":
                    files.append(os.path.join(folder, f))
                    print files[-1]
        if files:
            for f in files:
                try:
                    text_file = open(f, "w")
                    text_file.write("File name is: {0} in folder {1}".format(f, folder))
                    text_file.close()
                except Exception as e:
                    raise e
        else:
            print "No text files in {0}".format(folder)
            
    else:
        print "No files in {0}".format(folder)
        
raw_input()