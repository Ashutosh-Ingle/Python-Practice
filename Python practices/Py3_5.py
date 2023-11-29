import CheckPrime_num

def ListPrime(numbers):
    prime_Sum = 0

    for num in numbers:
        if CheckPrime_num.ChkPrime(num):
            prime_Sum += num

    return prime_Sum
    


def main():
    n = int(input("Enter the number of elements"))
    numbers = []

    for i in range(n):
        num = int(input("Enter the elements"))
        numbers.append(num)

    result = ListPrime(numbers)
    print("Addition of prime numbers is : ",result)

if __name__ == "__main__":
    main()