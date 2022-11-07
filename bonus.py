def salaryBonus(years,salary):

    if years >= 5:
        salary =(salary+(salary*0.05))
    else:
        salary=salary
        return(salary)


def main():
    years = int(input("How long have you been working at your company in years?"))
    salary = int(input("How much do you make a year at your company?"))
    total = salaryBonus(years,salary)
    print("your total salary is", total)
main()
