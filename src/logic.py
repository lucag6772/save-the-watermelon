from src.utility import print_divider, prompt_input

#This variable is in all caps to designate it as a globally accessible variable
DIFFICULTIES = [
    "EASY",
    "MEDIUM",
    "HARD"
]

game_response_to_difficulty = {
    "EASY": "I see, you must be a cadet. I will station you somewhere not so dangerous!",
    "MEDIUM": "Ah! From the reserve! The fruits await!",
    "HARD": "So you're the toughest of the tough, huh? MOVE IT!"
}

def run_main_menu():
    print_divider(dospacing=True)

    print("Welcome to Luca's Edition of SAVE THE WATERMELON")
    print("You are an elite fruit sorter and you are on a top secret mission. Are you ready?")
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