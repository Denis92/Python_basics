#!/usr/bin/python3
import random
import re
import os


class Wrong_answer(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"You have entered {self.value} but you must enter: y/n"


class End_game(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Game over"


class New_barrel():
    itteration = 0

    def barrel_gen(self):
        barrel_new = list(range(1, 91))
        random.shuffle(barrel_new)
        return barrel_new


class Generation_card():

    def print_card(self):
        card = list(range(1, 91))
        random.shuffle(card)
        res = []
        for x in range(0, 3):
            temp_list = list(map(str, sorted(card[x * 5:x * 5 + 5])))
            res.append(f"  {'  '.join(temp_list)}")

        return ''.join(res), card[:15]


class Game_class(Generation_card, New_barrel):
    flag_end_game = False
    user_name = ""

    def check_barrel_in_card(self, barrel_check, sud_card_numbers, card_chek, ask_user="no_ask"):

        if barrel_check in card_chek:
            sud_card_numbers = re.sub(r'\s{}\s'.format(barrel_check), r' X ', str(sud_card_numbers))
            if ask_user == "n":
                print(f'You Lose {barrel_check}')
                raise End_game(barrel_check)
            return sud_card_numbers
        if ask_user == "y":
            print(f'You lose because your card does not have this {barrel_check}')
            raise End_game(barrel_check)
        return sud_card_numbers

    def chek_winner(self, game_card, name_gamer):
        flag_chek = True
        card_chek = "".join(list(re.findall(r"[0-9]", str(game_card))))
        if not (card_chek.isdigit()):
            flag_chek = False
        return flag_chek

    def winner(self, user_card, bot_card):
        flag_u = self.chek_winner(user_card, self.user_name)
        flag_b = self.chek_winner(bot_card, "Bot")

        if not (flag_u) and not (flag_b):
            print("no winner")
            raise End_game(user_card)

        if not (flag_u):
            print(f"{self.user_name} Win")
            raise End_game(user_card)

        if not (flag_b):
            print("Bot Win")
            raise End_game(bot_card)

    def star_game(self):
        os.system("CLS")
        print("Enter your name:")
        self.user_name = input()
        self.user_card, self.user_numbers = self.print_card()
        self.bot_card, self.bot_numbers = self.print_card()
        self.itteration = 0
        print(f"bot_card\n {self.bot_card}")
        print(f"{self.user_name}\n {self.user_card}")
        self.barrel = self.barrel_gen()
        return self.user_card, self.bot_card, self.barrel, self.flag_end_game, self.user_name, self.itteration, self.user_numbers, self.bot_numbers


def main():
    game = Game_class()
    user_print_card, bot_print_card, barrel_new, flag_end_game, user_name, itteration, user_numbers, bot_numbers = game.star_game()

    while not (flag_end_game):
        try:

            print("Number: " + str(barrel_new[itteration]))
            print("Зачеркнуть цифру? (y/n)")
            ask_user = input()
            os.system("CLS")
            if not (ask_user == 'y' or ask_user == 'n'):
                raise Wrong_answer(ask_user)
            user_print_card = game.check_barrel_in_card(barrel_new[itteration], user_print_card, user_numbers, ask_user)
            bot_print_card = game.check_barrel_in_card(barrel_new[itteration], bot_print_card, bot_numbers)

            game.winner(user_print_card, bot_print_card)
            print(f"bot \n {bot_print_card}")
            print(f"{user_name} \n {user_print_card}")

            itteration += 1

        except Wrong_answer as e:
            print(e)
            print(f"{user_name} \n {user_print_card}")

        except End_game as e:
            print(e)
            flag_end_game = True
            print(f"{user_name} \n {user_print_card}")

    print("Would you like to play again? (y/n)")
    ask_user = input()
    main() if ask_user == 'y' else print("Goodbye")


if __name__ == '__main__':
    main()
