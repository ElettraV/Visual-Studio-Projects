# Importing Libraries (useful functions so you don't have to write code from scratch)
import random

# A function is a set of code that runs only when it is called. 
# Pay attention to INDENTATION: in Python it is very important (TAB). 
# Everything indented is gonna be part of the function. 

def get_choices(): 
  # Input function: when I want that a variable is the user input. 
  # It is going to print the message in the console, and then, the user input will be stored in the variable. 
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  # Lists: to store multiple items in a single variable
  options = ["rock", "paper", "scissors"]
  # Arguments: functions can receive data when they are called. I can specify arguments inside the brackets:
  computer_choice = random.choice(options)
  # Dictionaries: used to store data values in key value pairs. Values can be also variables. And a variable can be a dictionary. 
  choices = {"player": player_choice, "computer": computer_choice}

  return choices

def check_win(player, computer):
  # Concatenate: to put together strings and variables. 
  print(f"You chose {player}, computer chose {computer}.")

  # Remember to use two equal signs. If different, use !=
  if player == computer:
    return "It's a tie!"
  elif player == "rock": 
    if computer == "scissors": 
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":  
      return "Paper covers rock! You win!"
    else:
      return "Scissors cut paper! You lose."
  elif player == "scissors": 
    if computer == "paper": 
      return "Scissors cut paper! You win!"
    else:
      return "Rock smashes scissors! You lose."
    #Nested if statements: to make the code more readable. 
  

choices = get_choices()
# Choices is a dictionary, because the function get_choices returns a dictionary
# To extract values from a dictionary, use brackets and the corresponding key:
result = check_win(choices["player"], choices["computer"])
print(result) 