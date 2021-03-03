#!usr/bin/env python3

import termcolor
from art import *
import random
import time

art = text2art("JANKEN", font='small', chr_ignore=True)
print(termcolor.colored(art, 'green'))
print(termcolor.colored("ROCK SCISSOR PAPER, THE GAME!", 'blue'))


player_name = input(termcolor.colored("Input Player name: ", "green"))


def game(player_score=0, computer_score=0):
    while True:
        player = input(termcolor.colored("\n\nCHOOSE: ROCK, SCISSOR or PAPER: ", "blue")).lower()
        if player in ("rock", "scissor", "paper"):
            pass
        else:
            print(termcolor.colored("Wrong INPUT! Try again! \n"), "blue")
            game()

        possible_actions = ["rock", "paper", "scissor"]
        computer = random.choice(possible_actions)
        print(termcolor.colored("1..", 'green'))
        time.sleep(1)
        print(termcolor.colored("2..", 'yellow'))
        time.sleep(1)
        print(termcolor.colored("(ง •̀_•́)ง JANKEN! ง(•̀_• ́)ง ", 'red'))
        time.sleep(1)

        print(termcolor.colored(f"\n{player_name} chose {player}, Computer chose {computer}.\n", "blue"))
        time.sleep(1)

        if player == computer:
            print(termcolor.colored(f"Both players selected {player}. It's a tie! (-__-) \n\n", "red"))
        elif player == "rock":
            if computer == "scissor":
                print(termcolor.colored(f"Rock smashes scissors! {player_name} WINS! ٩(^‿^)۶ \n\n", "green"))
                player_score += 1
                print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
                print(termcolor.colored(f"Computer has {computer_score} points!", "green"))
            else:
                print(termcolor.colored(f"Paper covers rock! {player_name} LOST! ┌П┐(ಠ_ಠ) \n\n", "red"))
                computer_score += 1
                print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
                print(termcolor.colored(f"Computer has {computer_score} points!", "green"))
        elif player == "paper":
            if computer == "rock":
                print(termcolor.colored(f"Paper covers rock! {player_name} WINS! ٩(^‿^)۶ \n\n", "green"))
                player_score += 1
                print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
                print(termcolor.colored(f"Computer has {computer_score} points!", "green"))
            else:
                print(termcolor.colored(f"Scissors cuts paper! {player_name} LOST! ┌П┐(ಠ_ಠ) \n\n", "red"))
                computer_score += 1
                print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
                print(termcolor.colored(f"Computer has {computer_score} points!", "green"))
        elif player == "scissor":
            if computer == "paper":
                print(termcolor.colored(f"Scissors cuts paper! {player_name} WINS! ٩(^‿^)۶ \n\n", "green"))
                player_score += 1
                print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
                print(termcolor.colored(f"Computer has {computer_score} points!", "green"))
            else:
                print(termcolor.colored(f"Rock smashes scissors! {player_name} LOST! ┌П┐(ಠ_ಠ) \n\n", "red"))
                computer_score += 1
                print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
                print(termcolor.colored(f"Computer has {computer_score} points!", "green"))

        answer = input("Want to play again?: Y/N ")
        if answer in ("Y", "y", "yes", "YES", "Yes"):
            continue
        else:
            print(termcolor.colored(f"Thanks for playing {player_name}! Bye", "blue"))
            print(termcolor.colored(f"{player_name} has {player_score} points!", "green"))
            print(termcolor.colored(f"Computer has {computer_score} points!", "green"))
            exit()


game()
