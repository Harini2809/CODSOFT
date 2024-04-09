import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
