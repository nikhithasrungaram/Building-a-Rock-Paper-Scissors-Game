import random
possible_actions = ["rock" , "paper", "scissors"]
while True:
    user_action=input("Enter a choice(rock, paper, scissors): ").lower()
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's tie!")
    elif user_action == "rock":
        if(computer_action == "scissors"):
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif  user_action == "paper":
        if(computer_action == "rock"):
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif  user_action == "scissors":
        if(computer_action == "paper"):
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid input, please enter rock, paper, or scissors.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower()!="yes":
        break
              
