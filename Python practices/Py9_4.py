import os 
import sys

def compare_file_contents(input_file_name1,input_file_name2):
    try:
        with open(input_file_name1,"r") as input_file1:
            with open(input_file_name2,"r") as input_file2:
                contents1 = input_file1.read()
                contents2 = input_file2.read()
                if(contents1 == contents2):
                    print(f"{input_file_name1} and {input_file_name2} are similar")
                else:
                    print("Error : Files are not similar")

    except FileNotFoundError:
        print(f"Error : file not found")

    except Exception as e:
        print("An Error occured ")


def main():
    
    if len(sys.argv) != 3:
        print("Usage : copy_file.py <input.py><output.py>")
        return

    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]

    compare_file_contents(input_file1,input_file2)  

if __name__ == "__main__":
    main()