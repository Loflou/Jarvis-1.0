
import os

def rename_files(directory, prefix):
    """
    Renames all files in the specified directory by adding a prefix.
    
    Args:
    directory (str): The path to the directory containing the files to be renamed.
    prefix (str): The prefix to add to each file name.
    """
    for filename in os.listdir(directory):
        if not filename.startswith(prefix):
            new_name = prefix + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f'Renamed: {filename} to {new_name}')

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    prefix = input("Enter the prefix to add: ")
    rename_files(dir_path, prefix)
