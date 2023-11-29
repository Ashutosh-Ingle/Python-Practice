
def main():
    No = int(input("Enter number: "))
    temp = int(No/2 + 1)

    count = 2

    while ( count < temp):
        if(No % count == 0):
            print("Not prime")
        return 
        count += 1

    prime("It is a prime number")

if __name__ == "__main__":
    main()