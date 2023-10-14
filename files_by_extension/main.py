import os
import shutil


def group_files_by_extension(folder_path: str,
                             create_folders: bool = True,
                             move_files: bool = False,
                             exclude_extensions: list = None) -> None:
    """
       Group files in a specified folder by their file extensions.

       Args:
           folder_path (str): The path to the folder containing the files to be grouped.
           create_folders (bool, optional): If True, create separate folders for each file extension. Defaults to True.
           move_files (bool, optional): If True, move files into their respective folders. Defaults to False.
           exclude_extensions (list, optional):  List of files to exclude. Defaults to None.

       Returns:
           None
    """

    # Check if files can be moved
    if exclude_extensions is None:
        exclude_extensions = ['']
    if create_folders is False and move_files is True:
        print("Files cannot be moved if no folder is created.")
        return

    # Check if the specified folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Create a dictionary to store files by extension
    files_by_extension = list_files_extension(folder_path=folder_path, exclude_extensions=exclude_extensions)

    if create_folders:
        create_folders_by_extension(folder_path=folder_path, files_by_extension=files_by_extension)

    if move_files:
        move_files_to_folders(folder_path=folder_path, files_by_extension=files_by_extension)

    return


def list_files_extension(folder_path: str, exclude_extensions: list = None) -> dict:
    # Create a dictionary to store files by extension
    files_by_extension = {}

    # Iterate through the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            # Get the file extension (e.g., '.txt')
            _, file_extension = os.path.splitext(filename)

            # Remove the leading dot from the extension
            file_extension = file_extension[1:]

            # Add the file to the dictionary based on its extension
            if file_extension not in exclude_extensions:
                if file_extension in files_by_extension:
                    files_by_extension[file_extension].append(filename)
                else:
                    files_by_extension[file_extension] = [filename]

    return files_by_extension


def create_folders_by_extension(folder_path: str, files_by_extension: dict) -> None:
    # Create folders for each file extension
    for extension in files_by_extension.keys():
        extension_folder = os.path.join(folder_path, extension)
        os.makedirs(extension_folder, exist_ok=True)

    return


def move_files_to_folders(folder_path: str, files_by_extension: dict) -> None:
    # Move files to their respective folders
    for extension, file_list in files_by_extension.items():
        extension_folder = os.path.join(folder_path, extension)
        for filename in file_list:
            source_file = os.path.join(folder_path, filename)
            destination_file = os.path.join(extension_folder, filename)
            shutil.move(source_file, destination_file)

    return


if __name__ == "__main__":
    folder = "/path/to/your/folder"  # Replace with your folder path
    creator = True  # Set to True to create separate folders
    move = True  # Set to True to move files
    exclude_ext = ['py']  # List of extensions to exclude

    group_files_by_extension(folder_path=folder, create_folders=creator, move_files=move, exclude_extensions=exclude_ext)
