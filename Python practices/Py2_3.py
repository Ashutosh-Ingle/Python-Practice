def Fact(No):
    fact = 1
    for i in range(No, 0, -1 ):
        fact = fact * i
    return fact


def main():
    No = int(input("Enter number: "))
    
    Ret = Fact(No)
    print(Ret)

if __name__ == "__main__":
    main()