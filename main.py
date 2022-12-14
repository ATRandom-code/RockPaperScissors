# The function takes in the player's choice as an input
# and returns the result of the game as a string
def rock_paper_scissors(player_choice: str):
  # Convert the player's choice to lowercase
  # to make it case-insensitive
  player_choice = player_choice.lower()
  
  # Create a list of choices that the computer can make
  choices = ["rock", "paper", "scissors"]
  
  # Use the random module to randomly choose one of the options
  import random
  computer_choice = random.choice(choices)
  
  # Check the result of the game and return the result as a string
  if player_choice == computer_choice:
    return "It's a tie!"
  elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "Computer wins!"

# Run the function with the player's choice as an input
print(rock_paper_scissors("rock"))
