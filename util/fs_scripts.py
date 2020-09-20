import logging, sys
import shutil
import os
from pathlib import Path

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class FsFolderSort:
    
    EXCLUDE_FILES = ["desktop.ini"]

    @staticmethod
    def sort_files_in_folder(folder):
        filesInDir = []
        foldersInDir = []
        folder_creation_counter = 0
        # Split up files and folders
        os.chdir(folder)
        for d in os.listdir(folder):
            if os.path.isdir(d):
                foldersInDir.append(d)
            elif os.path.isfile(d):
                filesInDir.append(d)
            else:
                logging.warn("Unexpected element %s" % d)

        logging.debug("Found %s unsorted files and %s folders" %
            (len(filesInDir), len(foldersInDir)))

        logging.debug("Removing %s files to exclude from cleaning process" % len(FsFolderSort.EXCLUDE_FILES))
        for i in range(0, len(FsFolderSort.EXCLUDE_FILES)):
            if FsFolderSort.EXCLUDE_FILES[i] in filesInDir:
                filesInDir.remove(FsFolderSort.EXCLUDE_FILES[i])

        logging.debug("Cleaning the remaining %s files" % len(filesInDir))
        for f in filesInDir:
            fileToMove = f
            # Get the filetype of this file
            splitByDot = f.split(".")
            filetype = splitByDot[len(splitByDot)-1]

            # Check if there is already a folder for this filetype
            filetypeFolderExists = False
            for f in foldersInDir:
                if f.lower() == filetype.lower():
                    filetypeFolderExists = True
                    break

            # Create folder if it does not already exist
            foldername = filetype.lower()
            if not filetypeFolderExists:
                folder_creation_counter += 1
                logging.debug("Creating new filetype folder %s because it didn't exist" % foldername)
                os.mkdir(foldername)
                foldersInDir.append(foldername)

            # Move the file to the according folder for this filetype
            srcFile = folder / fileToMove
            dstFile = folder / foldername / fileToMove
            logging.debug("Moving file from %s to %s" % (srcFile, dstFile))
            shutil.move(srcFile, dstFile)
        return (len(filesInDir), folder_creation_counter)