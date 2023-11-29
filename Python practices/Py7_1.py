import threading 
def print_even_numbers():
    for i in range(2,21,2):
        print("Even",i)

def print_odd_numbers():
    for i in range(1, 20 , 2):
        print("Odd",i)

def main():
    
    even_thread = threading.Thread(target = print_even_numbers)
    odd_thread = threading.Thread(target = print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()