import threading

def print_even_list(numbers):
    Sum = 0
    for n in numbers:
        even_list = []
        for i in range(1, n+1):
              if n % i == 0 and i % 2 == 0:
                even_list.append(i)
                Sum = Sum + i

    print(f"Even list additon is: {Sum}")

def print_odd_list(numbers):
    Sum = 0
    for n in numbers:
        odd_list = []
        for i in range(1, n+1):
            if n % i == 0 and i % 2 != 0:
                odd_list.append(i)
                Sum = Sum + i
            
    print(f"Odd list is : {Sum}")

def main():
    
    n = int(input("Enter number of elements"))
    numbers = []

    for i in range(n):
        num = int(input("Enter elements"))
        numbers.append(num)

    even_thread = threading.Thread(target = print_even_list, args=(numbers,))

    odd_thread = threading.Thread(target = print_odd_list, args=(numbers,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()