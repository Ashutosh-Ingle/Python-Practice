
def CheckNum(No):
    if(No>0):
        print("Positive number")
    elif(No<0):
        print("Negative number")
    else:
        print("zero")
def main():
    Num = int(input("Enter a number"))
    CheckNum(Num)

if __name__ == "__main__":
    main()