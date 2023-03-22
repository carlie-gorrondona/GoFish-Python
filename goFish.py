#--------------------------------------------LIBRARIES & IMPORTS--------------------------------------------#
import random


#--------------------------------------------ARRAYS AND FUNCTIONS--------------------------------------------#

userPlayerCards = []
userPlayerBooks = []
computerPlayerCards = []
computerPlayerBooks = []
#stores all of the cards of a 52 card deck. The format is the first letter of a face card followed by the suit or the card number followed by the suit. 
#EX: Queen of Diamonds = QD, King of Spades = KS, 3 of Clubs = 3C, 7 of Hearts = 7H, etc.
cardDeck = [
    "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
    "AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
    "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C",
    "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S"
]

#This function is activated if the user selects option 1 from the main menu. Holds the shuffle(), deal(), and play() functions
def option1():
    shuffle()
    deal()
    play()

#This function shuffles the cardDeck array by selecting a random number between 0 and n (n initially equals 51), locates the index in cardDeck equal to the random number, 
#and then removes the card from its place in the array and appends it. Variable n is then decremented by 1 so the card appended to the array are not selected again.
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

#This function deals the shuffled cardDeck array. The loop runs 14 times for the 7 cards dealt to each player (the user and the computer). If the loop counter is even, 
#then the card is dealt to the user. If the loop counter is odd, then the card is dealt to the computer.
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

#This function determines player turn, gives the user game options to select from, and loops until cardDeck no longer contains cards. The user's turn is designated 
#by an even counter. If it is the user's turn, then the terminal prints the userPlayerCards array to show them what cards they have and it prints the opponent's card count.
#It then prints an Options menu that gives them a choice to request a card that they think the other player has, make a book with 4 cards of the same face or numerical 
#value, or quit the game. Selecting option 1 will run a check to make sure the opponent has cards in their hand and will run the requestACard() function if the check passes.
#Selecting option 2 will run the makeABook() function, and selecting option 3 will print a goodbye message and end the program. 
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

#This function prints the user's cards, the opponent's card count, and asks them to enter a card they think the opponent has. Since suit doesn't matter, the user
#only needs to enter the first letter of a face card or the number of a numerical card; suit does not matter. A for loop then checks if the user's submission is in 
#the opponent's hand. If the card is found in the opponent's hand, then it is removed from the computerPlayerCards array and added to the userPlayerCards array. If the 
#card is not found in the opponent's hand, then "Go fish!" prints to the terminal. 
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

print("MAIN MENU")
print("1. Play Game")
print("2. Exit")

userSelection = input("Enter 1 or 2 to select an option: ")

if userSelection == "1":
    option1()
elif userSelection == "2":
    print("Thanks for playing!")
else:
    print("Invalid input")