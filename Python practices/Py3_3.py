def Minimum(n):
    numbers = []
    min_num = None
    for i in range(n):
        try:
            num = int(input("Enter number: "))
            numbers.append(num)
            
            if min_num is None or num < min_num:
                min_num = num
        except ValueError:
            print("Invalid input")
            return None

    return min_num

def main():
    n = int(input("Enter the number of elements: "))
    ret = Minimum(n)
    
    if ret is not None:
        print("Maximum number is:", ret)

if __name__ == "__main__":
    main()
