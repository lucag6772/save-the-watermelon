import random
from pathlib import Path

from src.utility import print_divider, prompt_input

# This variable is in all caps to designate it as a globally accessible variable
DIFFICULTIES = [
    "EASY",
    "MEDIUM",
    "HARD"
]

game_response_to_difficulty = {
    "EASY": "I see, you must be a cadet. I will give you a training watermelon first!",
    "MEDIUM": "Ah! From the reserve! I gave the watermelon some armor to help you out!",
    "HARD": "So you're the toughest of the tough, huh? MOVE IT AND KEEP THE MELON SAFE!"
}

difficulty_to_file = {
    "EASY": "words_easy.txt",
    "MEDIUM": "words_medium.txt",
    "HARD": "words_hard.txt"
}

def run_main_menu():
    print_divider(dospacing=True)
    print("Welcome to Luca's Edition of SAVE THE WATERMELON")
    print("You are an elite fruit operator and your assignment is to protect our VIP watermelon from being sliced by hostiles!")
    result = prompt_input("ARE YOU READY?")
    if result == "no":
        print("You're a failure, operator... Goodbye")
        return False
    elif result == "yes":
        print("Great, how much of an expert are you, soldier?")
        return True
    else:
        print("I don't copy operator! Could you repeat?")
        return False

def run_difficulty_select():
    print_divider(text="DIFFICULTY SELECTION", dospacing=False)
    print("Select a difficulty:")
    print("[Easy, Medium, Hard)")
    difficultyResponse = prompt_input().upper()
    if difficultyResponse in DIFFICULTIES:
        print(game_response_to_difficulty[difficultyResponse])
        return difficultyResponse, True
    else:
        print("I don't understand, did you type the right difficulty, soldier?")
        return "", False

def choose_random_word_from_difficulty(difficulty):
        return random.choice(get_possible_words_from_difficulty(difficulty))

def get_possible_words_from_difficulty(difficulty):
    filename = difficulty_to_file[difficulty]
    # We use "r" to specify we are reading from the file
    with open("data/" + filename, "r") as file:
        # Get each line and remove the line break so the string isnt set to something with a line break
        possible_words = [line.strip() for line in file]
        return possible_words
