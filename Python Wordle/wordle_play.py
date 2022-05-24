# from joblib import PrintTime
from typing import List
from colorama import Fore
from regex import P
from letter_state import LetterState
from wordle import Wordle
import random

def main():
    # print("Hello Wordle!")
    word_set = load_word_set("data/five_words.txt") # set with a integer index is not possible
    secret = random.choice(list(word_set))
    print(secret)
    wordle = Wordle(secret)

    while wordle.can_attempt: # while(1)
        x = input("\nType your guess:")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!" + Fore.RESET)
            continue 
        if not x.upper() in word_set:
            print(Fore.RED + f"{x} is not a valid word!" + Fore.RESET)
            continue 

        
        wordle.attempt(x)
        display_results(wordle)
        # result = wordle.guess(x)
        # print(*result, sep = "\n")  #* takes all the characters results but GOOGLE IT
    if wordle.is_solved:
        print("You have solved the puzzle")
    else:
        print("You failed to solve the puzzle.")
        print(f"The secret word was: {wordle.secret}")

def display_results(wordle: Wordle):
    print("\nYour results so far...\n")
    print(f"You have {wordle.remaining_attempts} attempts remaining...\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    for _ in range(wordle.remaining_attempts): # _: Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))
    draw_border_around(lines)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines(): # return all lines in a file as list
            word = line.strip().upper() 
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)

def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom_border)


if __name__ == "__main__":  # any explcit import of this program will not cause the content of main function to be printed
    main()