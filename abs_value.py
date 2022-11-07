def absolute(number):
    absolute = abs(number)
    return absolute

def main():
    number = int(input("please enter a number"))
    print("the absolute value of", number, "is", absolute(number))


if __name__ == '__main__':
    main()