from art import logo
import random
import os

def checking(guess,guessed_number,attempt): 
    if guess>guessed_number and attempt!=0:
        return "Too High"
    elif guess<guessed_number and attempt!=0:
        return "Too Low"
    elif  guess==guessed_number:
        return "You Win"
    elif attempt==0:
        return "You ran out of chances. You Loose"
    else:
        return "You Loose"
    
def game_start():
    os.system("CLS")
    game()
    
def game():  
    print(logo)
    print("Welcome To Guess the Numer Game")
    guessed_number=random.randint(0,100)
    print(guessed_number)
    level=input("Select Level of difficulty 'easy' or 'hard':")
    if level=='easy':
        attempt=10
        
    else:
        attempt=5
    should_continue=False
    while not should_continue:
         print(f"You have {attempt} Attempts")
         guess=int(input("Guess the Number Between 0-100:"))
         attempt=attempt-1
         print(checking(guess,guessed_number,attempt))
         if guess==guessed_number or attempt==0:
            should_continue=True
            if input("Do You Want to Play again Type 'y' or 'n':")=='y':
                game_start()
            else:
                os.system("CLS")
                print("Thanks For Playing")
game_start()