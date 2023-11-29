
def ChkNum(No):
    if(No % 2 ==0):
        print("Even number")
    else:
        print("odd Number")    
def main():
    Num = int(input("Enter number : "))
    Ret = ChkNum(Num)

if __name__ == "__main__":
    main()