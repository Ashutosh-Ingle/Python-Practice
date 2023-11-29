import os
import glob
import sys

def list_files_with_extension(directory, extension):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Use glob to find files with the specified extension
    files = glob.glob(os.path.join(directory, f"*.{extension}"))

    # Check if any files with the given extension were found
    if not files:
        print(f"No files with '{extension}' extension found in '{directory}'.")
    else:
        print(f"Files with '{extension}' extension in '{directory}':")
        for file in files:
            print(file)

if __name__ == "__main__":
    # Check if the user provided the correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <extension>")
    else:
        directory = sys.argv[1]
        extension = sys.argv[2]

        list_files_with_extension(directory, extension)
