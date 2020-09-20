import logging, sys
import click
import shutil
import os
from pathlib import Path
from filesystem_scripts.fs_scripts import FsFolderSort

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

@click.group()
def automo_cli():
    pass

@automo_cli.command(help="Sort the Files in your Download Folder by Fileextension.")
def sort_downloads():
    folder_dir = Path.home() / "Downloads"
    click.echo("[Automo] Sorting Downloads Folder: '%s'" % folder_dir)
    files_moved, folders_created = FsFolderSort.sort_files_in_folder(folder_dir)
    click.echo("[Automo] Moved {fileqty} files into {folderqty} folders.".format(fileqty=files_moved, folderqty=folders_created))

@automo_cli.command(help="Sort the Files in your Download Folder by Fileextension.")
def sort_desktop():
    folder_dir = Path.home() / "Desktop"
    click.echo("[Automo] Sorting Desktop Folder: '%s'" % folder_dir)
    files_moved, folders_created = FsFolderSort.sort_files_in_folder(folder_dir)
    click.echo("[Automo] Moved {fileqty} files into {folderqty} folders.".format(fileqty=files_moved, folderqty=folders_created))

if __name__ == "__main__":
    automo_cli()