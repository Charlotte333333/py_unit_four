
def even_or_odd(number):
    if number % 2 == 0:
        return (str(number) +   " is an even number")
    else:
       return (str(number) +  " is an odd number")




def main():
    number = int(input("Please enter a number"))
    print(even_or_odd(number))





if __name__ == '__main__':
    main()




