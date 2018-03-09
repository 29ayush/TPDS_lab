import os, tarfile,sys

dir_name = sys.argv[1]
dest_dir = dir_name+sys.argv[2]
engext = ".e.gz"
frenext = ".f.gz"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(engext): # check for ".tar" extension
        efile = os.path.abspath(item) # get full path of files
        ffile = efile[:-len(engext)] + frenext
             # create tarfile object
        tarf = tarfile.tarFile(ffile) # create tarfile object
        tare.extractall(item[:-len(engext)]) # extract file to dir
        tarf.extractall(item[:-len(engext)]) # extract file to dir
        tare.extractall(dest_dir) # extract file to dir
        tarf.extractall(dest_dir) # extract file to dir
        tare.close() # close file
        tarf.close() # close file
        os.remove(file_name) # delete tarped file
