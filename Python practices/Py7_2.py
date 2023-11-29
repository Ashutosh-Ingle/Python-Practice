import threading 

def print_even_factor(n):
    sumE = 0
    for i in range(2,n+1,2):
        if (n % i == 0):
            sumE = sumE + i
    print(f"The sum of even factors of {n}: {sumE}")

def print_odd_factor(n):
    sumO = 0
    for i in range(1, n+1 , 2):
        if (n % i == 0):
            sumO =sumO + i
    print(f"The sum of even factors of {n}: {sumO}")


def main():

    n = int(input("Enter the number"))
    
    even_thread = threading.Thread(target = print_even_factor, args = (n,))
    odd_thread = threading.Thread(target = print_odd_factor, args = (n,))


    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()