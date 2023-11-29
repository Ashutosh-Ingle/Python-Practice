import sys
import os

def check_string_exists(file_name,string):
    try:
        with open(file_name,"r") as file:
            file_contents = file.read()

        frequency = file_contents.count(string)
        return frequency

    except FileNotFoundError:
        print("File not found")

    except Exception as e :
        print("Error")


def main():
    file_name = input("Enter file name: ")

    string = input("Enter string to search: ")

    check_freq= check_string_exists(file_name,string)

    print("Frequency of string is : ",check_freq)

if __name__ == "__main__":
    main()