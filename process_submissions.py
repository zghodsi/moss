import os
import zipfile
from zipfile import BadZipfile
#pip install rarfile
import rarfile
from rarfile import RarFile

import fnmatch

rootdir = './Lab1'
submission = '/mips.cpp'


# Rename folders
def rename():
    for filename in os.listdir(rootdir):
        newname = filename[filename.find("(")+1:filename.find(")")]
        os.rename (os.path.join(rootdir,filename), os.path.join(rootdir, newname))


# Uncompress submissions
def uncompress():
    for filename in os.listdir(rootdir):
        subdir = os.path.join(rootdir,filename)
        for subfile in os.listdir(subdir):
            if subfile.endswith(".txt"):
                print "removing: " + subfile
                os.remove(os.path.join(subdir,subfile))
            else:
                subsubdir = os.path.join(subdir,subfile)
                for subsubfile in os.listdir(subsubdir):
                    compressedfile = os.path.join(subsubdir, subsubfile)
                    if subsubfile.endswith(".zip"):
                        try:
                            zipr = zipfile.ZipFile(compressedfile, 'r')
                            zipr.extractall(subsubdir)
                            zipr.close()
                        except BadZipfile:
                            print "Bad Zip File:" + subsubdir + " " + subsubfile

                        print "removing: " + subsubfile
                        os.remove(compressedfile)


                    if subsubfile.endswith(".rar"):
                        rarr = rarfile.RarFile(compressedfile)
                        rarr.extractall(subsubdir)

                        print "removing: " + subsubfile
                        os.remove(compressedfile)


# Move files to correct directory
def movefiles():
    i=1
    for root, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if filename.endswith(".cpp") and  not filename.startswith("."):
                #print str(i), root
                cppfile = os.path.join(root,filename)
                print str(i), cppfile
                # Clean up here
                i1=root.find("1/")
                i2=root.find("/S")
                snetid = root[i1+2:i2]
                os.rename(cppfile, os.path.join(rootdir, snetid+submission))
                i+=1

def main():
    rename()
    uncompress()
    movefiles()

if __name__=="__main__":
    main()
