# -*- coding: utf-8 -*-
"""Wordle Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d7e8shV_JGIWDhzBQ2gTedSw7eSTvHQP
"""

import random

class Wordle():
    def __init__(self):
        self.word_bank = ["GATES", "LATER", "JAILS", "STARE", "HEART",
                          "LOVER", "TEARS", "REACH", "PIOUS", "SANDY",
                          "DRIVE", "PINKY", "EARLY", "THINK", "DATES",]
        self.keyboard = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        self.word = random.choice(self.word_bank) # randomly choose target word
        self.board = [["-" for _ in range(5)] for _ in range(6)]

    # make text red
    def red(self, word):
        r, b, e = "\033[91m", "\033[1m", "\033[0m"
        return b + r + word + e

    # make text green
    def green(self, word):
        g, b, e = "\033[92m", "\033[1m", "\033[0m"
        return b + g + word + e

    # make text black
    def black(self, word):
        bl, b, e = "\033[30m", "\033[1m", "\033[0m"
        return b + bl + word + e

    def show_game(self):
        # indents to align game elemnts properly
        indent_guess = " " * 5
        indent_all = " " * 10
        # stores rightly guessed letters
        seen = set()
        # show previous guesses
        for row in self.board:
            # break after last guess
            if row == ["-" for _ in range(5)]:
                print(indent_all + indent_guess + " ".join(row))
                break
            
            # color the letters in each previous guess
            else:
                letters = ""
                for i in range(len(self.word)):
                    # green for correctly placed
                    if row[i] in self.word and row[i] == self.word[i]:
                        letters += self.green(row[i])+  " "
                        seen.add(row[i]) # mark as rightly guessed (seen)
                    
                    # black for incorrectly placed
                    elif row[i] in self.word and row[i] != self.word[i]:
                        letters += self.black(row[i])+  " "
                        seen.add(row[i]) # mark as rightly guessed (seen)

                    # red for letter not in word
                    else:
                        letters += self.red(row[i])+  " "
                        # block off wrongly guessed letters on keyboard
                        for k in range(len(self.keyboard)):
                            self.keyboard[k] = self.keyboard[k].replace(row[i], "🀫")
                
                # display color-coded previous guess
                print(indent_all + indent_guess + letters)
            print()
        print()

        # show keyboard
        for i in range(len(self.keyboard)):
            indent_keyboard = " " * i
            # color seen keys black
            keys = ""
            for key in self.keyboard[i]:
                if key in seen:
                    keys += self.black(key)+  " "
                else:
                    keys += key + " "
            # display row of keys
            print(indent_all + indent_keyboard + keys)
        
    def play_game(self):
        # show previous guesses
        self.show_game()
        # loop over game for 6 tries
        for i in range(6):
            guess = input("Guess: ").upper() # user inputs a guess
            self.board[i] = list(guess) # 
            print("\n\n")
            self.show_game()
            if guess == self.word:
                print(f"\nYou win!!!\n\n")
                break
            print(f"\nWrong word! {6-i-1} guess(es) left\n\n")
        print(f"The correct word was {self.word}")

if __name__ == '__main__':
    wordle = Wordle()
    wordle.play_game()