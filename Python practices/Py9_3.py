import os 
import sys

def copy_file_contents(input_file_name,output_file_name):
    try:
        with open(input_file_name,"r") as input_file:
            with open(output_file_name,"a") as output_file:
                contents = input_file.read()
                output_file.write(contents)
        print(f"contents copied from {input_file_name} to {output_file_name}")

    except FileNotFoundError:
        print(f"Error : file not found")

    except Exception as e:
        print("An Error occured ")


def main():
    
    if len(sys.argv) != 3:
        print("Usage : copy_file.py <input.py><output.py>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    copy_file_contents(input_file,output_file)  

if __name__ == "__main__":
    main()