import os 

def check_file_exists(file_name):

    if os.path.exists(file_name):
        print(f"file {file_name} exists in the current directory")
    else:
        print(f"file {file_name} not exist in the current directory")

def main():
    file_name = input("Enter file name")

    check_file_exists(file_name)


if __name__ == "__main__":
    main()