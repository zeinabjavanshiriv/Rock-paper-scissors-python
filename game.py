import random

print("---------------------\nCHOOSING GAME\n---------------------")
name = input("Enter your name: ")
name = name.capitalize()
print(f"---------------------\nHello {name}\nWelcome to our game")


def play_friends():
    player2 = input("---------------------\nEnter second player name: ")
    player2 = player2.capitalize()
    print(f"---------------------\nOk {name} and {player2} let's start!")
    while True:
        player1wins = 0
        player2wins = 0
        draw2 = 0
        player2_win2 = 0
        player_win2 = 0
        draws_win2 = 0
        while True:
            rounds2 = int(input("How many rounds? (numbers only)  "))
            for i in range(rounds2):
                print(f"Round: {i + 1}")
                choose1 = input(f"{name} choose: ")
                choose1 = choose1.title()
                choose2 = input(f"{player2} choose: ")
                choose2 = choose2.title()
                if choose1 == choose2:
                    print("Same choose!\nCongratulations :> \n---------------------")
                    draw2 += 1
                    draws_win2 += 1
                elif choose1 == "Paper" and choose2 == "Rock":
                    print(
                        f"{name} won!this round\nCongratulations :> \n---------------------"
                    )
                    player1wins += 1
                    player_win2 += 1
                elif choose1 == "Rock" and choose2 == "Paper":
                    print(
                        f"{player2} won! this round \nCongratulations :>\n---------------------"
                    )
                    player2wins += 1
                    player2_win2 += 1
                elif choose1 == "Scissor" and choose2 == "Paper":
                    print(
                        f"{name} won! this round\nCongratulations :> \n---------------------"
                    )
                    player1wins += 1
                    player_win2 += 1
                elif choose1 == "Paper" and choose2 == "Scissor":
                    print(
                        "{player2} won! this round \nCongratulations :>\n---------------------"
                    )
                    player2wins += 1
                    player2_win2 += 1
                elif choose1 == "Scissor" and choose2 == "Rock":
                    print(
                        f"{player2} won! this round \nCongratulations :>\n---------------------"
                    )
                    player2wins += 1
                    player2_win2 += 1
                elif choose1 == "Rock" and choose2 == "Scissor":
                    print(
                        f"{name} won! this round\nCongratulations :> \n---------------------"
                    )
                    player1wins += 1
                    player_win2 += 1
                else:
                    print("Invalid input\nTry again! :< \n---------------------")

            print(
                f"RESULTS:\n{name} Wins: {player1wins}\n{player2} Wins: {player2wins}\nDraws: {draw2}"
            )
            if player_win2 < player2_win2:
                print(f"{player2} is winner!\n---------------------")

            elif player_win2 > player2_win2:
                print(f"{name} is winner!\n---------------------")

            elif player_win2 < draws_win2 and player2_win2 < draws_win2:
                print(f"{name} and {player2} are winners!\n---------------------")
            else:
                print(f"{name} or {player2} didn't choose in some rounds")
            break
        break


def again():
    while True:
        again = input("-------------------- \nPlay again? (1.Yes/2.No)")
        if again == "1":
            play_game()
        elif again == "2":
            break
        else:
            print("Invalid input")


def play_game():
    while True:
        win = 0
        lose = 0
        draw = 0
        pc_win = 0
        player_win = 0
        draws_win = 0
        while True:
            rounds = int(input("How many rounds? (numbers only)  "))
            for i in range(rounds):
                print(f"Round: {i + 1}")
                pc = random.choice(game)
                print("Choose Rock , Paper , Scissor")
                player = input("You choose: ")
                player = player.title()
                print(f"Pc chooses: {pc}")
                if player == pc:
                    print("Same choose!\nTry again! :< \n---------------------")
                    draw += 1
                    draws_win += 1
                elif player == "Paper" and pc == "Rock":
                    print(
                        "You won! this round\nCongratulations :> \n---------------------"
                    )
                    win += 1
                    player_win += 1
                elif player == "Rock" and pc == "Paper":
                    print("Pc won! this round\nTry again! :< \n---------------------")
                    lose += 1
                    pc_win += 1
                elif player == "Scissor" and pc == "Paper":
                    print(
                        "You won! this round\nCongratulations :> \n---------------------"
                    )
                    win += 1
                    player_win += 1
                elif player == "Paper" and pc == "Scissor":
                    print("Pc won! this round\nTry again! :< \n---------------------")
                    lose += 1
                    pc_win += 1
                elif player == "Scissor" and pc == "Rock":
                    print(f"Pc won! this round\nTry again! :< \n---------------------")
                    lose += 1
                    pc_win += 1
                elif player == "Rock" and pc == "Scissor":
                    print(
                        "You won!this round\nCongratulations :> \n---------------------"
                    )
                    win += 1
                    player_win += 1
                else:
                    print("Invalid input\nTry again! :< \n---------------------")

            print(f"RESULTS:\nWins: {win}\nLosses: {lose}\nDraws: {draw}")
            if player_win < pc_win:
                print("Pc is winner!\n---------------------")

            elif player_win > pc_win:
                print(f"{name} is winner!\n---------------------")
                again()

            elif player_win < draws_win and pc_win < draws_win:
                print(f"{name} and Pc are winners!\n---------------------")
                again()
            else:
                print(f"{name} didn't choose in some rounds\n---------------------")
                again()
            break
        break


game = ["Rock", "Paper", "Scissor"]
while True:
    choice = input("1.Play\n2.Exit\n3.Play with your friend\nPlease choose number: ")
    if choice == "1":
        play_game()

    elif choice == "2":
        print(f"Good bye! {name}, have good time")
        break
    elif choice == "3":
        play_friends()
        if choice != "3":
            print("Invalid input")
    else:
        print("Invalid input")
