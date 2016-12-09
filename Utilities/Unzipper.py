import os
import zipfile
import sys

EXTENSION = ".zip"

def unzip_files(source, destination):
    print source
    print destination
    source = 'F://272//SoilData'
    dest = 'F://272//data//'

    os.chdir(source)  # change directory from working dir to dir with files

    for item in os.listdir(source):  # loop through items in dir
        if item.endswith(EXTENSION):  # check for ".zip" extension
            file_name = os.path.abspath(item)  # get full path of files
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(dest)  # extract file to dir
            zip_ref.close()  # close file
            # os.remove(file_name) # delete zipped file


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Please check the syntax."
        print "Unzipper.py <source_dir> <destination_dir>"

    unzip_files(sys.argv[1], sys.argv[2])
