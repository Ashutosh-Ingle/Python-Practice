
def Add(No1, No2):
    Ans = No1 + No2
    return Ans
  
def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))
    Ret = Add(Num1,Num2)
    print("Addition is ",Ret)

if __name__ == "__main__":
    main()