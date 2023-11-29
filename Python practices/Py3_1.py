
def main():

    numbers = []
    n = int(input("Enter number for list"))
    for i in range(n):
        try:
            num = int(input("Enter number :"))
            numbers.append(num)
        except ValueError:
            print("Invalid input")
            return None

        total = sum(numbers)
        print(total)
if __name__ == "__main__":
    main()