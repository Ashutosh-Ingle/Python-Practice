
def digits(No):
    Sum = 0
    
    while(No != 0):
        digit = int(No % 10)
        Sum = Sum + digit       
        No = int(No / 10)
        
        
    return Sum
def main():
    Num = int(input("Enter a number"))
    ret = digits(Num)
    print(ret)

if __name__ == "__main__":
    main()