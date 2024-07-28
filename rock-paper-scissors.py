import random

def get_computer_choice():
    """Generate a random choice for the computer"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice"""
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    return 'computer'

def play_game():
    """Play a round of Rock, Paper, Scissors"""
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following options:")
    print("1. Rock ")
    print("2. Paper ")
    print("3. Scissors ")
    print("4. Lizard ")
    print("5. Spock ")
    
    user_choice = input("Enter your choice (1/2/3/4/5): ")
    if user_choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please try again.")
        return play_game()
    
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_choice = choices[int(user_choice) - 1]
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Sumit's Mac wins!")
    
    play_again = input("\nDo you want to play again? (yes/no): ")
    while True:
        if play_again.lower() == 'yes':
            play_game()
            break
        elif play_again.lower() == 'no':
            print("You played very well👏🏻and Thanks for playing Dear👍🏻!!")
            break
        else:
            print("Invalid choice. Please try again.")
            play_again = input("\nDo you want to play again? (yes/no): ")

def determine_winner_with_lizard_spock(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice with lizard and spock"""
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'rock' and computer_choice == 'lizard') or \
       (user_choice == 'lizard' and computer_choice == 'spock') or \
       (user_choice == 'spock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'lizard') or \
       (user_choice == 'lizard' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'spock') or \
       (user_choice == 'spock' and computer_choice == 'rock'):
        return 'user'
    return 'computer'

def get_computer_choice_with_lizard_spock():
    """Generate a random choice for the computer with lizard and spock"""
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    return random.choice(choices)

def play_game_with_lizard_spock():
    """Play a round of Rock, Paper, Scissors with lizard and spock"""
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("Please choose one of the following options:")
    print("1. Rock ")
    print("2. Paper ")
    print("3. Scissors ")
    print("4. Lizard ")
    print("5. Spock ")
    
    user_choice = input("Enter your choice (1/2/3/4/5): ")
    if user_choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please try again.")
        return play_game_with_lizard_spock()
    
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_choice = choices[int(user_choice) - 1]
    computer_choice = get_computer_choice_with_lizard_spock()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    winner = determine_winner_with_lizard_spock(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Sumit's Mac wins!")
    
    play_again = input("\nDo you want to play again? (yes/no): ")
    while True:
        if play_again.lower() == 'yes':
            play_game()
            break
        elif play_again.lower() == 'no':
            print("You played very well👏🏻and Thanks for playing Dear👍🏻!!")
            break
        else:
            print("Invalid choice. Please try again.")
            play_again = input("\nDo you want to play again? (yes/no): ")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("Do you want to play with lizard and spock? (yes/no): ")
        response = input().lower()
        if response == 'yes':
            play_game_with_lizard_spock()
            break
        elif response == 'no':
            play_game()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()