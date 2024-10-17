import shutil
import os
from time import sleep
import customtkinter as ctk
from fileExtensions import commonFileTypes
from tkinter import filedialog
from tkinter import messagebox
import argparse

# Parsing the CLI arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='File Sorter')
    parser.add_argument('directory', nargs='?', default=None, help='The directory to sort')
    return parser.parse_args()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.geometry("240x240")
window.title("File Sorter")
window.resizable(False, False)

directory = None

def createFolder(parent_dir):
    global dir_list
    dir_list = os.listdir(parent_dir)
    if not os.path.exists(parent_dir + "/Others"):
        os.mkdir(parent_dir + "/Others")
    for fileTypes in dir_list:
        if not os.path.isdir(parent_dir + "\\" + fileTypes):
            fileExt = fileTypes.split(".")[-1].lower()
            if (
                fileExt.lower() in commonFileTypes
                and os.path.exists(parent_dir + "/" + commonFileTypes[fileExt]) == False
            ):
                os.mkdir(parent_dir + "/" + commonFileTypes[fileExt])

def sortFiles(parent_dir):
    for fileTypes in dir_list:
        if not os.path.isdir(parent_dir + "\\" + fileTypes):
            fileExt = fileTypes.split(".")[-1].lower()
            if fileExt.lower() in commonFileTypes:
                shutil.move(
                    f"{parent_dir}/{fileTypes}",
                    f"{parent_dir}/{commonFileTypes[fileExt]}/{fileTypes}",
                )
            else:
                shutil.move(
                    f"{parent_dir}/{fileTypes}",
                    f"{parent_dir}/Others/{fileTypes}",
                )

def deleteEmptyFolders(parent_dir):
    for folder in os.listdir(parent_dir):
        folder_path = os.path.join(parent_dir, folder)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)

def countFilesInFolders(parent_dir):
    folder_counts = {}
    for folder in os.listdir(parent_dir):
        folder_path = os.path.join(parent_dir, folder)
        if os.path.isdir(folder_path):
            file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
            folder_counts[folder] = file_count
    if len(folder_counts) == 0:
        return {"Files": "No"}
    else:
        return folder_counts  

def getFileExtensionStatistics(parent_dir):
    extension_counts = {}
    for folder in os.listdir(parent_dir):
        folder_path = os.path.join(parent_dir, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                file_extension = file.split('.')[-1].lower()
                extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1
    if len(extension_counts) == 0:
        return {"File Extensions": "No"}
    else:
        return extension_counts

def moveSpecificFileType(parent_dir, file_extension, destination_folder):
    for file in os.listdir(parent_dir):
        if file.lower().endswith(f".{file_extension.lower()}"):
            source_path = os.path.join(parent_dir, file)
            destination_path = os.path.join(parent_dir, destination_folder, file)
            shutil.move(source_path, destination_path)

def sortButton():
    global directory
    if directory not in [None, ""]:
        createFolder(directory)
        sleep(0.5)
        sortFiles(directory)
        deleteEmptyFolders(directory)
        messagebox.showinfo(
            "Finished sorting", "The files in your chosen directory have been sorted"
        )
    else:
        messagebox.showwarning(
            "Something's wrong",
            "It was an error. You didn't specify a path",
        )

def exploreFolder(directory):
    if directory is None:
        messagebox.showwarning("Error", 'No folder selected')
    elif os.path.isdir(directory):
        os.startfile(directory)
    else:
        messagebox.showwarning("Error", 'Not a folder')

def directorySelectButton():
    global directory
    directory = filedialog.askdirectory(title="Select a directory")

def showFileCounts():
    if directory not in [None, ""]:
        counts = countFilesInFolders(directory)
        message = "\n".join([f"{folder}: {count} files" for folder, count in counts.items()])
        messagebox.showinfo("File Counts", message)
    else:
        messagebox.showwarning("Error", "Please select a directory first.")

def showExtensionStatistics():
    if directory not in [None, ""]:
        stats = getFileExtensionStatistics(directory)
        message = "\n".join([f"{extension}: {count} files" for extension, count in stats.items()])
        messagebox.showinfo("File Extension Statistics", message)
    else:
        messagebox.showwarning("Error", "Please select a directory first.")

dirButton = ctk.CTkButton(master=window, command=directorySelectButton, text="Choose directory", width=20)
sortFilesButton = ctk.CTkButton(master=window, command=sortButton, text="Sort the files", width=20)
explorerButton = ctk.CTkButton(master=window, command=lambda: exploreFolder(directory), text="Open Folder", width=20)
fileCountsButton = ctk.CTkButton(master=window, command=showFileCounts, text="Show File Counts", width=20)
extensionStatsButton = ctk.CTkButton(master=window, command=showExtensionStatistics, text="Show Extension Statistics", width=20)

dirButton.pack(pady=10, padx=15)
sortFilesButton.pack(pady=10, padx=15)
explorerButton.pack(pady=10, padx=15)
fileCountsButton.pack(pady=10, padx=15)
extensionStatsButton.pack(pady=10, padx=15)

def main():
    global directory
    args = parse_arguments()
    if args.directory:
        directory = args.directory
        createFolder(directory)
        sleep(0.5)
        sortFiles(directory)
        deleteEmptyFolders(directory)
        print("Files sorted successfully.")
    else:
        # Use CWD as default if not provided
        directory = os.getcwd()
        window.mainloop()

if __name__ == "__main__":
    main()