
# This is the main file... please Execute here
# from cgitb import reset
from art import *
from typing import List
from colorama import Fore
from cv2 import split
from letter_state import LetterState
from wordle import Wordle
import random


tprint("--------WORDLE---------")

print(Fore.LIGHTRED_EX + "Welcome to the Wordle Game!!!" + Fore.RESET)
print("\n")
print("RULES")
print(Fore.CYAN + "Here you have to guess a five letter word . At Max 6 attempts will be given\n"+ Fore.RESET)
print(Fore.GREEN + "If the letter is of GREEN color: it means that the letter is in the word and is in correct position" + Fore.RESET)
print(Fore.LIGHTYELLOW_EX + "If the letter is of YELLOW color: it means that the letter is in the word but in the wrong spot" + Fore.RESET)
print(Fore.LIGHTBLACK_EX + "If the letter is of WHITE color: it means that the letter is not in the word on any spot" + Fore.RESET)

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def main():
    
    word_set = load_word_set("data/five_words.txt") 
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input(Fore.YELLOW + "\nType your guess:" + Fore.YELLOW) 

        if len(x) != wordle.LENGTH_WORD:
            print(Fore.RED + f"Word must be {wordle.LENGTH_WORD} characters long!" + Fore.RESET)
            continue 
        if not x.upper() in word_set:
            print(Fore.RED + f"{x} is not a valid word!" + Fore.RESET)
            continue 

        
        wordle.attempt(x)
        display_results(wordle)
        
    if wordle.is_solved:
        tprint("Hurray")
        print(Fore.LIGHTYELLOW_EX + "You have solved the puzzle" + Fore.RESET)
    else:
        print(Fore.BLUE + "You failed to solve the puzzle." + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + f"The secret word was: {wordle.secret}" + Fore.RESET)

def display_results(wordle: Wordle):
    print(Fore.LIGHTMAGENTA_EX + "\nYour results so far...\n" + Fore.RESET)
   
    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        
        colored_result_str = convert_result_to_color(result)
        
        lines.append(colored_result_str)
    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.LENGTH_WORD))
    draw_border_around(lines)
    demo = letter_history(wordle)

    print(Fore.BLUE + f"You have {wordle.remaining_attempts} attempts remaining...\n" + Fore.RESET)

def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper() 
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.LIGHTYELLOW_EX
        else:
            color = Fore.LIGHTBLACK_EX
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)

colored_letters = []
final_colored_letters = []

def letter_history(wordle: Wordle):
    
    curr_res = wordle.attempts[-1]
    result = wordle.guess(curr_res)
    

    for letter in result:
        letter_b4_color = letter.character
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.LIGHTYELLOW_EX
        else:
            color = Fore.LIGHTBLACK_EX
        colored_letter = color + letter.character + Fore.RESET
        
        if letter_b4_color in letters:
            letter_index = letters.index(letter_b4_color)
            letters[letter_index] = colored_letter

    print("LETTER HISTORY : " + " ".join(letters))
    

    return " ".join(letters)

    
    


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom_border)


if __name__ == "__main__":  
    main()