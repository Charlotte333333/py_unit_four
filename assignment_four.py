import random
print("This is a game of black jack! Your goal is to get a higer number than the dealer without going over 21. If you go over 21 you lose, and if the dealer goes over 21 they lose")

def random_card():
    """This function makes the random cards"""
    return(random.randint(1,11))



def who_wins(user,computer):
    '''This function determines who wins

    :param user: user's total card
    :param computer: dealer's total cards
    :return: who wins
    '''
    print("user has",user,", dealer has", computer)
    if user > 21:
        return "user loses"
    elif computer > 21:
        return "computer loses"
    elif user > 21 and computer > 21:
        return "computer and user lose"
    elif user > computer:
        return "user wins"
    elif computer> user:
        return "computer wins"
    elif user == computer:
        return "its a tie"



def dealers_cards(computer):
    """This function gives the dealer cards

    :param computer: the dealer
    :return: the dealers total cards
    """
    dtotal = random_card()
    #print("computer drew a", dtotal)
    computer = computer + dtotal
    return computer

def third_card(user):
    """This function asks the user if it wants a third card. If they do it gives them it and adds it to their total if not it just uses their previous total

    :param user: The  user's total cards
    :return: The users total with the thrid card if they wanted it
    """
    choice = input("Do you want another card? Type 'yes' or 'no'")
    if choice == "yes":
        brown = random_card()
        print("you drew a", brown)
        print("Your current total is", brown + user)
        return brown
    else:
        print("Your holding total is", user)
        return user



def main():
    """
    This function puts the game together. It takes all the other functions and prints out the result of the game
    :return: Who wins, and the game
    """
    user = random_card()
    print("your first card is", user)
    second_card = random_card()
    print("your second card is", second_card)
    user = user + second_card
    print("your total is", user)


    computer = 0
    dealers_total = dealers_cards(computer)
    #print("the computer's total is", dealers_total)

    dealers_total2 = dealers_cards(dealers_total)
    #print("the computer's total is", dealers_total2)


    third_card(user)

    print(who_wins(user, dealers_total2))

main()
