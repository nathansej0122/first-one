#Create a rock/paper/scissors game where the user plays against the computer.

import random

def main():
    #Call function that starts program and asks user to input their choice.
    input_user_choice()

#Initial function that allows user to input choice
def input_user_choice():

    #User input of rock/paper/scissors
    choice = input("Please choose rock, paper, or scissors to play. ")

    #check to make sure rock/paper/scissors is entered.
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        print(f"You have entered something other than rock, paper, or scissors. Please try again")
        choice = input("Please choose rock, paper, or scissors to play. ")
        continue

    #If rock, paper, or scissors is entered, program continues to determine the winner, which includes generating the computer choice
    else:
       determine_winner(choice, generate_computer_play())   

#converts random integer 1-3 into rock/paper/scissors
def generate_computer_play():
    computer_play = random.randint (1, 3)

    if computer_play == 1:
        return "rock"

    elif computer_play == 2:
        return "paper"
    
    elif computer_play == 3:
        return "scissors"

#accepts the initial input of choice and the result of the funciton generate_computer_play to determine the winner.
def determine_winner(player, computer):
    #Patter for dramatic effect
    print(f'Computer is making its choice.')
    print('3')
    print('2')
    print('1')
    print('Shoot!')
    
    #Displays the computer choice accepted from generate_computer_player
    print(f'The computer chooses {computer}')

    #Condition for rock/scisor
    if (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "rock"):
        print(f'Rock smashes scissors!')
        would_you_like_to_play_again()
    
    #Condition for scissor/paper
    elif (player == "scissors" and computer == "paper") or (player == "paper" and computer == "scissors"):
        print(f'Scissors cuts paper!')
        would_you_like_to_play_again()
    
    #Condition for rock/paper
    elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "rock"):
        print(f'Paper wraps rock!')
        would_you_like_to_play_again()

    #Condition for same choice. Condition returns the user to the input_user_choice function if the same choice is made. 
    else:
        print(f'Both players chose {player}. Please go again.')
        input_user_choice()

#I dislike pressing the run button every time, so I created a condition that asks the user if they want to play again and restarts the game if yes. If not, prints a thank you message. 
def would_you_like_to_play_again():
    play = input("Would you like to play again? Press 'y' to continue or 'n' to end. ")

    if play == 'y':
        input_user_choice()
    else:
        print('Thank you for playing. Goodbye!')

#Call main function   
if __name__ == '__main__':
    main()