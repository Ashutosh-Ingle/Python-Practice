
def CheckDiv(No):
    if(No % 5 == 0 and No != 0):
        print("True")
    else:
        print("False")
    
def main():
    Num = int(input("Enter a number"))
    CheckDiv(Num)

if __name__ == "__main__":
    main()