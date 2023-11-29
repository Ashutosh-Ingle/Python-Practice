def Frequency(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

def main():
    numbers = []
    n = int(input("Enter the number of elements: "))
    
    for i in range(n):
        try:
            num = int(input("Enter number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input")
            return

    freq = int(input("Enter the number to search for: "))

    ret = Frequency(numbers, freq)

    print(f"The frequency of {freq} in the list is: {ret}")

if __name__ == "__main__":
    main()
