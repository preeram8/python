user1 = input("What is player1's name: ")
user2 = input("What is player2's name: ")

while True:
    user1_answer = input(user1 + ", Do you want to choose Rock,Paper or Scissors? ").lower()
    user2_answer = input(user2 + ", Do you want to choose Rock,Paper or Scissors? ").lower()

    if user1_answer==user2_answer:
        print("Its a tie")
    elif user1_answer=='rock' and user2_answer=='scissors':
        print(user1 + "wins the game")
    elif user1_answer=='scissors' and user2_answer=='paper':
        print(user1 + "wins the game")
    elif user1_answer=='paper' and user2_answer=='rock':
        print(user1 + "wins the game")
    elif user2_answer=='rock' and user1_answer=='scissors':
        print(user2 + "wins the game")
    elif user2_answer=='scissors' and user1_answer=='paper':
        print(user2 + "wins the game")
    elif user2_answer=='paper' and user1_answer=='rock':
        print(user2 + "wins the game")
    else:
        
        print("Invalid input! You have not entered rock, paper or scissors, try again.")

    repeat = input("Do you want to continue the game. Type Yes/No: ").lower()

    if(repeat == "yes"):
        pass
    elif(repeat == "no"):
        raise SystemExit
    else:
        print("You entered an invalid option. Exiting now.")
        raise SystemExit