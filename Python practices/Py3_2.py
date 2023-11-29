def Maximum(n):
    numbers = []
    max_num = None
    for i in range(n):
        try:
            num = int(input("Enter number: "))
            numbers.append(num)
            
            if max_num is None or num > max_num:
                max_num = num
        except ValueError:
            print("Invalid input")
            return None

    return max_num

def main():
    n = int(input("Enter the number of elements: "))
    ret = Maximum(n)
    
    if ret is not None:
        print("Maximum number is:", ret)

if __name__ == "__main__":
    main()
