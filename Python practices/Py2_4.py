def Fact(No):
    Sum = 0
    for i in range(No//2, 0, -1 ):
        if(No % i == 0):
            Sum =  Sum + i
    return Sum


def main():
    No = int(input("Enter number: "))
    
    Ret = Fact(No)
    print(Ret)

if __name__ == "__main__":
    main()