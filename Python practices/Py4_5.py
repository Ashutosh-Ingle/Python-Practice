from functools import reduce


def Num_Prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

def main():
    n = int(input("enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input("enter elements: "))
        numbers.append(num)

    output = list(filter(Num_Prime,numbers))
    print("filter is ",output)

    map_output = list(map(lambda No : No * 2 ,output))
    print("map is",map_output)

    result = reduce(lambda x,y : x if x > y else y, map_output)
    print("reduce is ",result)


if __name__ == "__main__":
    main()