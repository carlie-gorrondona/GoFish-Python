#--------------------------------------------LIBRARIES & IMPORTS--------------------------------------------#
import random


#--------------------------------------------ARRAYS AND FUNCTIONS--------------------------------------------#

userPlayerCards = []
userPlayerBooks = []
computerPlayerCards = []
computerPlayerBooks = []
cardDeck = [
    "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
    "AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
    "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
    "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S"
]

def option1():
    shuffle()
    deal()
    play()

def shuffle():
    i = 0
    n = 51

    while i < 51:
        shuffledCard = random.randint(0, n)
        
        for x in range(len(cardDeck)):
            if x == shuffledCard:
                pulledcard = cardDeck.pop(x)
                cardDeck.append(pulledcard)

        n -= 1
        i += 1

    print(cardDeck)

def deal():
    i = 0

    while i < 14:

        if i % 2 == 0:
            dealtCard = cardDeck.pop()
            userPlayerCards.append(dealtCard)
        else:
            dealtCard = cardDeck.pop()
            computerPlayerCards.append(dealtCard)

        i += 1


    print("These are your cards: \n")
    print(userPlayerCards)
    print(computerPlayerCards)

def play():
    counter = 0

    while len(cardDeck) > 0:
        if counter % 2 == 0:
            print("Your cards: ")
            print(userPlayerCards)
            print("Opponent's card count: ")
            print(len(computerPlayerCards))

            print("Options:")
            print("1. Request a card")
            print("2. Make a book")
            print("3. Quit")
            roundOption = input("Select an option: ")

            match roundOption:
                case "1":
                    if len(computerPlayerCards) == 0:
                        print("No cards to request. Please select another option.")
                        break
                    else:
                        requestACard()
                case "2":
                    makeABook()
                case "3":
                    print("Thanks for playing!")
                    break
                case _:
                    return "Invalid Input"
    
        counter += 1

def requestACard():
    notFound = True
    print("Your cards: ") 
    print(userPlayerCards)
    print("Opponent's card count: ")
    print(len(computerPlayerCards))
    cardRequested = input("Enter a card to request: ")

    for card in computerPlayerCards:
        if cardRequested in card and cardRequested != None:
            computerPlayerCards.remove(card)
            userPlayerCards.append(card)
            notFound = False

    if notFound:
        print("Go fish!")

def makeABook():
    bookCards = input("Enter the number or letter of the cards you'd like to book: ")

    # for card in userPlayerCards:
    #     if bookCards in card 


#--------------------------------------------MAIN CODE--------------------------------------------#

print("****************** WELCOME TO GO FISH! ******************\n")

print("MENU")
print("1. Play Game")
print("2. Exit")

userSelection = input("Enter 1 or 2 to select an option: ")

if userSelection == "1":
    option1()
elif userSelection == "2":
    print("Thanks for playing!")
else:
    print("Invalid input")