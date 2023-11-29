import os 
import sys
def check_file_exists(file_name):

    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            file_contents = file.read()
            print(file_contents)
    else:
        print(f"file {file_name} not exist in the current directory")

def main():
    file_name = argv[1]

    new_file = create(file_name)

    check_file_exists(file_name)


if __name__ == "__main__":
    main()