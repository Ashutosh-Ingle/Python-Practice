def pattern(No):
    for i in range(No):
        for j in range(No):
            print('*', end = '  ')
        print('')


def main():
    No = int(input("Enter number: "))
    pattern(No)

if __name__ == "__main__":
    main()