
def digits(No):
    count = 0
    while(No != 0):
        No = int(No / 10)
        count+= 1
    return count
def main():
    Num = int(input("Enter a number"))
    ret = digits(Num)
    print(ret)



if __name__ == "__main__":
    main()