from functools import reduce

Num_Greator = lambda No: No % 2 == 0
Increase = lambda No: No * No


def main():
    n = int(input("enter the number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input("enter elements: "))
        numbers.append(num)

    output = list(filter(Num_Greator,numbers))
    print("filter is ",output)

    map_output = list(map(Increase,output))
    print("map is",map_output)

    result = reduce(lambda x,y: x  + y ,map_output)
    print("reduce is ",result)


if __name__ == "__main__":
    main()