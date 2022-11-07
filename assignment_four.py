import random
print("This is a game of black jack! If ")
def get_card():


def random_card():
    return(random.randint(1,11))



def who_wins(user,computer):
    if user> 21:
        return("user loses")
    elif computer>21:
        return "computer loses"
    elif user and computer>21:
        "computer and user lose"
    elif user> computer:
        "user wins"
    elif computer> user:
        "computer wins"
    elif user == computer:
        "its a tie"



    retun



def main():
    user = random_card()
    print(user)
    second_card = random_card()
    print("your second card is", second_card)
    user = user + second_card
    print(user)

main()