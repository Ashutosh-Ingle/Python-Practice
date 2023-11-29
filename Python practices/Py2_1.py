import Arithmetic

def main():
    Num1 = int(input("Enter first number"))
    Num2 = int(input("Enter second number"))
    print("Addition is : ", Arithmetic.Add(Num1,Num2))
    print("Sub is : ", Arithmetic.Sub(Num1,Num2))
    print("Mult is : ", Arithmetic.Mult(Num1,Num2))
    print("Division is : ", Arithmetic.Div(Num1,Num2))


if __name__ == "__main__":
    main()