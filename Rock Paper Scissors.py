import random

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please choose Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer
