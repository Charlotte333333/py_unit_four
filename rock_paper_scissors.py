import random


def who_wins(user, computer):
    # 1 is rock, 2 is paper, 3 is scissors


    if user == computer:
        return "its a tie"
    elif computer==1 and user==2:
        return "user wins"
    elif computer == 2 and user == 1:
        return "computer wins"
    elif computer == 3 and user==1:
        return "user wins"
    elif computer==1 and user==3:
        return "computer wins"
    elif computer==2 and user==3:
        return "user wins"
    elif computer==3 and user==2:
        return "computer wins"
    else:
        return "error"






    pass



def main():

    computer = random.randint(1,3)
    user = input("enter 1 for rock, 2 for paper, and 3 for scissers")


    pass



if __name__ == '__main__':
    main()