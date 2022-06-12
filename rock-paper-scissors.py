import random
score1 = 0
score2 = 0
while True:
    print("Welcome to the game, you can choose...")
    print("r for rock")
    print("p for paper")
    print("s for scissors")

    player = input("pick from r, p or s. ")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        print("It's a Tie!")
        score1 = score2
    elif player == 'r' and computer == 's':
        print("You win!")
        score1 += 1
    elif player == 'p' and computer == 'r':
        print("You win!")
        score1 += 1
    elif player == 's' and computer == 'p':
        print("You win!")
        score1 += 1
    elif computer == 'r' and player == 's':
        print("You lose, computer won")
        score2 += 1
    elif computer == 'p' and player == 'r':
        print("You lose, computer won")
        score2 += 1
    elif computer == 's' and player == 'p':
        print("You lose, computer won")
        score2 += 1
    else:
        print("Invalid entry, try again!")
    print("Would you like to play again?")
    print('1. Yes')
    print('2. No')
    choice = input("Choose 1 or 2. ")
    if choice == '2':
        print(f"you won {score1} game(s) and the computer won {score2} game(s).")
        if score1 > score2:
            print("Congrats, You are the winner")
        elif score1 < score2:
            print("The computer won most games, you lost")
        else:
            print("It's a Tie between you two.")
        print("Thanks for playing.")
        break    
